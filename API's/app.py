from flask import Flask, jsonify, request
from helper import generate_id 

app = Flask(__name__)

info = []

#POST API
@app.route('/add_data', methods=['POST'])
def add_data():
   try:
       body = request.get_json(force=True)

       if "name" not in body or "age" not in body:
          return jsonify({"success": False , "error": "Both Fields are required"})
       name  = body['name']
       age = body['age']
       user_id = generate_id()
       info.append({"id" : user_id, "name": name, "age" : age})
       return jsonify({"success": True , "data": "Shabash Hafsaa"})
   except Exception as error:
       return jsonify({"success": False , "error": error})

#GET API
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
      return jsonify({"success": True , "data" : info})
    except Exception as error:
        return jsonify({"success": False , "error": error })

#GET DATA BY ID API
@app.route("/get-user-by-id/<id>", methods=["GET"])
def get_user_by_id(id):
    try:
      user = next((item for item in info if item["id"] == id), None)
      if user:
       return jsonify({"success": True , "data" : user})
      else:
        return jsonify({"success": False , "error": "User Not Found" }) 
    except Exception as error:
        return jsonify({"success": False , "error": error })


if __name__ == "__main__":
    app.run(debug=True)

