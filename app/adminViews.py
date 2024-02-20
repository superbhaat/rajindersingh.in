from app import app

from flask import render_template
import pymysql

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASS"] = "Think360#"
app.config["MYSQL_DB"] = "rajinderSingh"
app.config["MYSQL_CHAR"] = "utf8mb4"
app.config["MYSQL_CURSOR"] = pymysql.cursors.DictCursor
connection = pymysql.connect(
    host=app.config["MYSQL_HOST"],
    user=app.config["MYSQL_USER"],
    password=app.config["MYSQL_PASS"],
    database=app.config["MYSQL_DB"],
    charset=app.config["MYSQL_CHAR"],
    cursorclass=app.config["MYSQL_CURSOR"]
)


@app.route("/admin")
def adminIndex():
    return render_template("admin/index.html")
    #return "<p>Hello, Admin View!</p>"

@app.route("/admin/database")
def database():
    cur = connection.cursor()
    # cur.execute(''' CREATE DATABASE rajinderSingh ''')
    # cur.execute(''' SHOW DATABASES ''')
    query = ''' 
            CREATE TABLE IF NOT EXISTS `employee` (
            `id` int(11) NOT NULL auto_increment,       
            `fname` varchar(250)  NOT NULL default '',
            `lname` varchar(250)  NOT NULL default '',
            `email` varchar(250)  NOT NULL default '', 
            PRIMARY KEY  (`id`));
        '''
    cur.execute(query)
    result_data = cur.fetchall()
    cur.close()
    print(result_data)

    return "Database Installed!"