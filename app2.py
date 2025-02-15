# python app.py 
# to run the server

from flask import Flask, render_template, request

app = Flask(__name__) #ye name ka parameter hay # when we create private variables we use __, when we want to create public variable we dont use "underscore". see nasir hussains lecs on OOP in i guess 1st quarter

data = [] # khali dictionary bnai

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name   = request.form['name']
        email  = request.form['email']
        roll   = request.form['roll']
        course = request.form['course']

        record1 = {'name': name, 'email':email, 'roll':roll, 'course': course}
        data.append(record1) # APPEND!!! yani page par bar bar records add krtay jao gay tu vo dictionaries add hoti jayian giiii

    return render_template("home2.html")



@app.route("/about2")
def about2():
    return render_template("about2.html", data=data) # data khali list bhi hua tab bhi atleast list tu hay! isi liye about page phir bhi chlay ga! list jis par loop chlay gi vo empty lits hogi, so no loop.


if __name__ == '__main__':
    app.run(debug=True)

