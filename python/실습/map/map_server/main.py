
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__) 


@app.route('/') 
def index():
    return render_template("index.html")



@app.route("/map/", methods=["POST"])
def map():
    _map = request.form["address"] # id 키 값을 받아 옴
    # _menu = request.form["menu"]
    
    
    # _db = pymysql.connect(
    # user = "root",
    # password= "dkrkwk18!",
    # host = "localhost",
    # db = "coffee"
    # )
    # cursor = _db.cursor(pymysql.cursors.DictCursor)
    # sql = """
    #         SELECT * FROM brand_coffee WHERE brand = %s
    #         """
    # _values = [_coffee]
    # cursor.execute(sql, _values)
    # result = cursor.fetchall()
    # print(result)
    # asd = result[0][_menu] #어떻게 가격이 뜨는지 
    map = _map
    return render_template("map.html")#, price=asd
    
@app.route("/map/", methods=["POST"])
def map_1():
    
    return redirect(url_for('index'))

app.run(port=8080, debug = True)