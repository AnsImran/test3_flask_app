# Class - 10 RestAPI ( Part 2) - AI Education (720p, h264)
# 2:05 hr:min


# How to Create a Database, Add Tables and Import Data in MySQL Workbench
# https://www.youtube.com/watch?v=OnXB3ZRrOW0


# CREATE DATABASE mydb;
# USE mydb;
# CREATE TABLE Students (
# 	studentID int,
#     LastName varchar(255),
#     FirstName varchar(255),
#     Address varchar(255),
#     City varchar(255)
# );

from flask import Flask, request, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)     # app k sath connect kr k object bna dia ...


app.config['MYSQL_HOST']      = 'localhost'      # local host hoga, ye bta dia/ config kr dia
app.config['MYSQL_USER']      = 'root'           # mysql workbench ko root user access kray ga
app.config['MYSQL_PASSWORD']  = '1538879Aa.'     # 
app.config['MYSQL_DB']        = 'mydb'           # mysql work.. k andar ye vli data base


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        id       =  request.form['studentID']
        lname    =  request.form['LastName']
        fname    =  request.form['FirstName']
        address  =  request.form['Address']
        city     =  request.form['City']

        # 1
        # cursor object bnaya
        cur      =  mysql.connection.cursor()   # data receive krnay k bad mysql say connection bnaya | cursor ka object aya

        # 2
        # query bna k execute krnay lagy hain
        query = "INSERT INTO students (studentID, LastName, FirstName, Address, City) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (id, lname, fname, address, city))
        # %s: a string value.

        # 3
        # query execute honay k baad commit kia hum nay
        mysql.connection.commit()      
        # connection closed
        cur.close()

        return render_template("index.html") #'Successfully updated record in database'
    return render_template("index.html")

@app.route("/students")
def getusers():
    cur   = mysql.connection.cursor()
    students = cur.execute("SELECT * FROM students")
#    print(students)
    if students > 0:
        studentDetails = cur.fetchall() # fetch all records, not 1-by-1
    return render_template('students.html', students=studentDetails)

if __name__ == "__main__":
    app.run(debug=True)
