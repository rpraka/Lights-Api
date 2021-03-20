from auth_keys import auth_keys
from flask import Flask, request, jsonify
from setup_db import setup_db

app = Flask(__name__)

conn, cursor = setup_db()

@app.route('/set_status/', methods=['POST'])
def status():
    response = {'message':''}
    new_status = int(request.args.get("new_status", None))
    id  = request.args.get('id', None)
    auth_key  = request.args.get('auth_key', None)

    if id is None:
        response['message'] += "[ERROR] No id was passed."
        response["code"] = False
        return jsonify(response)
    if new_status is None:
        response['message'] += "[ERROR] No new status was passed."
        response["code"] = False
        return jsonify(response)
    
    if (auth_key == auth_keys.get(id, None)):
        response['message'] += "[AUTH] auth valid."
        try:
            cursor.execute("UPDATE light_meta SET status = %s WHERE id = %s", (new_status, id))
            conn.commit()
            response["code"] = True
        except:
            cursor.execute("ROLLBACK")
            conn.commit()
            print("ROLLBACK")
            response['message'] += "[ERROR] Database rollback"
            response["code"] = False

        cursor.execute("SELECT * FROM light_meta;")
        current_status = cursor.fetchone()[1]

        response["message"] += f"Got new status {new_status}, current: {current_status}"
    
    else:
        response['message'] += "[ERROR] invalid auth."

    return jsonify(response)
        
@app.route('/get_status/', methods=['GET'])
def get_status():
    # Retrieve the name from url parameter
    response = {}
    id  = request.args.get('id', None)
    auth_key  = request.args.get('auth_key', None)

    if id is None:
            response['message'] = "[ERROR] No id was passed."
    elif auth_key == auth_keys.get(id, None):
        cursor.execute("SELECT * FROM light_meta WHERE id=%s;", (id,))
        current_status = cursor.fetchone()[1]

        response["current_status"] = current_status
    
    return jsonify(response)

@app.route('/')
def index():
    return "<h1>lights_api</h1>"
#allow close on worker termination

if __name__ == '__main__':
    app.run(port=5000, workers=3, debug=False)
