from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS light_meta (
    id integer,  
    status integer NOT NULL
    );
    """)

conn.commit()
cursor.execute(""" INSERT INTO light_meta (id, status) values (1,-1); """)
cursor.execute(""" INSERT INTO light_meta (id, status) values (2,-1); """)
conn.commit()


@app.route('/set_status/', methods=['POST'])
def status():
    response = {}
    # Retrieve the name from url parameter
    new_status = int(request.args.get("new_status", None))
    id  = request.args.get('id', None)

    if id is None:
        response['message'] = "[ERROR] No id was passed."
        response["code"] = False
    elif new_status is None:
        request['message'] = "[ERROR] No new status was passed."
        response["code"] = False
    else:
        try:
            cursor.execute("UPDATE light_meta SET status = %s WHERE id = %s", (new_status, id))
            conn.commit()
        except:
            cursor.execute("ROLLBACK")
            conn.commit()
            print("ROLLBACK")
        cursor.execute("SELECT * FROM light_meta;")
        current_status = cursor.fetchone()[1]

        
        response["message"] = f"Got new status {new_status}, current: {current_status}"
        response["code"] = (new_status == current_status)
        
    return jsonify(response)

@app.route('/get_status/', methods=['GET'])
def get_status():
    # Retrieve the name from url parameter
    response = {}
    id  = request.args.get('id', None)
    if id is None:
            response['message'] = "[ERROR] No id was passed."
    else:
        cursor.execute("SELECT * FROM light_meta WHERE id=%s;", (id,))
        current_status = cursor.fetchone()[1]

   
        response["current_status"] = current_status
    
    return jsonify(response)


@app.route('/')
def index():
    return "<h1>lights_api</h1>"

#allow close on worker termination
# cursor.close()
# conn.close()
if __name__ == '__main__':
    app.run(port=5000, workers=3, debug=False)
