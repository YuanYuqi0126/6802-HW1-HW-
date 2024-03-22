from flask import Flask, request, render_template
import datetime
import sqlite3
from flask import Markup

app = Flask(__name__)

name_flag = 0
name = ""

@app.route("/",methods = ["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods = ["GET","POST"])
def main():
    global name_flag, name
    if name_flag == 0:
        name = request.form.get("name")
        name_flag = 1
        conn = sqlite3.connect("log.db")
        c = conn.cursor()
        timestamp = datetime.datetime.now()
        c.execute("insert into employee (name,timestamp) values(?,?)",(name,timestamp))
        conn.commit()
        c.close()
        conn.close()
    return(render_template("main.html", name=name))

@app.route("/ethical_test",methods = ["GET","POST"])
def ethical_test():
    return(render_template("ethical_test.html"))

@app.route("/query",methods = ["GET","POST"])
def query():
    conn = sqlite3.connect("log.db")
    c = conn.execute("select * from employee")
    r = ""
    for row in c:
        r =r+str(row)+"<br>"
    print(r)
    r = Markup(r)
    c.close()
    conn.close()
    return(render_template("query.html", r=r))

@app.route("/delete",methods = ["GET","POST"])
def delete():
    conn = sqlite3.connect("log.db")
    c = conn.cursor()
    c.execute("delete from employee;")
    conn.commit()
    c.close()
    conn.close()
    return(render_template("delete.html"))



