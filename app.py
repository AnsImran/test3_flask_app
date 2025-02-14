# python app.py 

# to run the server


from flask import Flask

app = Flask(__name__) #ye nme ka parameter hay # when we create private variables we use __, when we want to create public variable we dont use "underscore". see nasir hussains lecs on OOP in i guess 1st quarter

# url = route in api
@app.route("/")  # we use @ to create a route, @: ye aik decorator hay prof nasir k lecs k andar is k baray main hui hay. idk in which quarter
# /: mean user will write nothing. landing page bnay ga.

def home():
    return "Hello Python with Flask"


if __name__ == "__main__":

    app.run(debug=True) # can use your own port as well = app.run(debug=True, port=)



