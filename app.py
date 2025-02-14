# python app.py 
# to run the server


from flask import Flask, render_template, request

app = Flask(__name__) #ye name ka parameter hay # when we create private variables we use __, when we want to create public variable we dont use "underscore". see nasir hussains lecs on OOP in i guess 1st quarter

# # url = route in api
# @app.route("/")  # we use @ to create a route, @: ye aik decorator hay prof nasir k lecs k andar is k baray main hui hay. idk in which quarter
# # /: mean user will write nothing. landing page bnay ga.
# def home():
#     return "Hello Python with Flask"

# # OR

# # ab string response k bajaye, page ko render krvayain gay
# # from flask import render
# @app.route("/")
# def home():
#     return render_template("home.html")

# OR

# # sending data from backend to frontend
# @app.route("/")
# def home():
#     name = input("User please tell me your name") # input lia, (ye terminal(console) k andar input lay ga)

#     return render_template("home.html", data = {'name': name})     # input html ko bhaij dia. | page k sath sath name bhi display kr do
# # Respone: data = {'name': name} : should always be in the form of dictionary
# # How It Works?
# #     The data={'name': name} dictionary is passed from Python to the template.
# #     Jinja2 syntax ({{ data.name }}) is used inside the HTML to dynamically insert the name.



data = {} # khali dictionary bnai
@app.route("/")
def home():
    name = input("User please tell me your name")
    data['name'] = name #jo name input hua osay data-dictionary main daal dia
    return render_template("home.html", data = {'name': name})






# # aik new route/url/page add kr di
# @app.route("/about")
# def about():
#     return "<h1>This is about page</h1>" # <h1>...</h1> html format. h1 level ki heading

# OR

# rendering a template
@app.route("/about")
def about():
    return render_template("about.html")



# sending data from frontend to backend
# from flask import request
@app.route("/f-to-b", methods=['GET', 'POST'])
def ftob():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1+num2
        return render_template("f-to-b.html", result = {'result': result})

# going directly to this page
    else:
        return render_template('f-to-b.html', result = {'result': None}) # otherwise simply render the simple page

# @app.route("/f-to-b", methods=["GET", "POST"])
# def ftob():
#     result = None
#     if request.method == "POST":
#         num1 = request.form.get("num1")
#         num2 = request.form.get("num2")
#         if num1.isdigit() and num2.isdigit():
#             result = int(num1) + int(num2)
#         else:
#             result = "Invalid input. Please enter numbers."
#     return render_template("f_to_b.html", result=result)



@app.route('/pk')
def pak():
    return render_template('pk.html')




if __name__ == "__main__":

    app.run(debug=True) # ab ye error aya tu main browser k andar bhi error message show kray ga. ye na lgatay tu sirf/consol/terminal k andar hi show hona tha
# can use your own port as well, | app.run(debug=True, port=)



