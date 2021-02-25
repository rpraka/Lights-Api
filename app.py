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
    INSERT INTO light_meta VALUES (1,0) ON CONFLICT UPDATE
    """)

conn.commit()


print("table made")



@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("new_status", None)

    print(f"got new_status {name}")
    
    cursor.execute("SELECT * FROM light_meta;")

    current_status = cursor.fetchone()

    response = {}
   
    response["message"] = f"Got new status {name}, current: {current_status}!!"

    # Return the response in json format
    return jsonify(response)


@app.route('/')
def index():
    return "<h1>lights_api</h1>"

#allow close on worker termination
# cursor.close()
# conn.close()
if __name__ == '__main__':

    app.run(port=5000, workers=2, debug=True)
