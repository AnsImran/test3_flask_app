# python app.py 
# to run the server


from flask import Flask
from flask import render_template
from flask import request, jsonify

app = Flask(__name__) #ye name ka parameter hay # when we create private variables we use __, when we want to create public variable we dont use "underscore". see nasir hussains lecs on OOP in i guess 1st quarter

@app.route("/")
def home():
    name = 'Ans'
    age = 23
    data = {'name': name, 'age': age}
    return jsonify(data)
app.run(debug=True)

# WITHOUT ANY FRONTEND !
# WILL TEST APIs ON POSTMAN!!