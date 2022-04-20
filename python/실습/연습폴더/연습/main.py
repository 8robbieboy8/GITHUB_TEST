
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__) 


@app.route('/') 
def index():
    return render_template("index.html")



@app.route("/coffee/", methods=["POST"])
def coffee():
    _coffee = request.form["brand_coffee"] # id 키 값을 받아 옴
    _menu = request.form["menu"]
    
    
    _db = pymysql.connect(
    user = "root",
    password= "dkrkwk18!",
    host = "localhost",
    db = "coffee"
    )
    cursor = _db.cursor(pymysql.cursors.DictCursor)
    sql = """
            SELECT * FROM brand_coffee WHERE brand = %s
            """
    _values = [_coffee]
    cursor.execute(sql, _values)
    result = cursor.fetchall()
    print(result)
    asd = result[0][_menu] #어떻게 가격이 뜨는지 
    return render_template("next.html", price=asd)

app.run(port=8080)