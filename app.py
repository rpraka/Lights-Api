from flask import Flask, request, jsonify
import os
import psycopg2

# DATABASE_URL = os.environ['DATABASE_URL']
# 
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# cursor = conn.cursor()
# 
# cursor.execute(""" CREATE TABLE IF NOT EXISTS light_meta (
    # id SERIAL,
    # state integer NOT NULL DEFAULT 0
    # );""")
# print("table made")
# app = Flask(__name__)

# @app.route('/getmsg/', methods=['GET'])
# def respond():
#     # Retrieve the name from url parameter
#     name = request.args.get("name", None)

#     # For debugging
#     print(f"got name {name}")

#     response = {}

#     # Check if user sent a name at all
#     if not name:
#         response["ERROR"] = "no name found, please send a name."
#     # Check if the user entered a number not a name
#     elif str(name).isdigit():
#         response["ERROR"] = "name can't be numeric."
#     # Now the user entered a valid name
#     else:
#         response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

#     # Return the response in json format
#     return jsonify(response)


#     # A welcome message to test our server
# @app.route('/')
# def index():
#     return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(port=5000, workers=2)