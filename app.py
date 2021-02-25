from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS light_meta (
    id SERIAL,
    state integer NOT NULL DEFAULT 0
    );""")

conn.commit()
cursor.close()
conn.close()
print("table made")



@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)


    # A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # app.run(port=5000, workers=2, debug=True)
    app.run(host='0.0.0.0', port=port)
