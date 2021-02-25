from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS light_meta (
    id integer,
    state integer NOT NULL
    );
    """)

conn.commit()
cursor.execute(""" INSERT INTO light_meta (id, state) values (1,0); """)
conn.commit()
cursor.execute("SELECT * FROM light_meta;")
current_status = cursor.fetchone()
print(f"table made {current_status}")



@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    new_status = request.args.get("new_status", None)

    cursor.execute(""" INSERT INTO light_meta (id, state) values (1,%d);""",(new_status,))
    conn.commit()

    print(f"got new_status {new_status}")
    
    cursor.execute("SELECT * FROM light_meta;")

    current_status = cursor.fetchone()

    response = {}
   
    response["message"] = f"Got new status {new_status}, current: {current_status}!!"

    # Return the response in json format
    return jsonify(response)


@app.route('/')
def index():
    return "<h1>lights_api</h1>"

#allow close on worker termination
# cursor.close()
# conn.close()
if __name__ == '__main__':

    app.run(port=5000, workers=2, debug=False)
