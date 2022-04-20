from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/coffee/",  methods=["POST"])
def coffee():
    _coffee = request.form["brand"] #브랜드의 역할은 뭐지
    # _menu = request.form["menu"]
    

    _db = pymysql.connect(
                        user = "root",
                        password = "dkrkwk18!",
                        host = "localhost",
                        db = "coffee"
    )
    cursor = _db.cursor(pymysql.cursors.DictCursor)
    sql = """
            SELECT * FROM brand_coffee WHERE brand = %s
            """
    _vlaues = [_coffee]
    cursor.execute(sql, _vlaues)
    result = cursor.fetchall()
    print(result)
    # _price = result[0][_menu]
    # return render_template("next.html", price = _price)

app.run(port=8080)


