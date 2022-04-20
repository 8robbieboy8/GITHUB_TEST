from flask import Flask, redirect, render_template, request, redirect, url_for
# from pymysql_sever.modules.mod_sql import Database
from modules import mod_sql

app = Flask(__name__) #지금 내가 실행시키고 있는 파일명이 들어감

#localhost로 접속 했을때
@app.route('/') #빈 url
def index():
    return render_template("index.html")

#localhost/signup로 접속했을때
@app.route("/signup/", methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/signup/", methods=["POST"])
def signup_2():
  
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]
    _regitdate = request.form["_regitdate"]
    sql ='''
            INSERT INTO user_info VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    _values = [_id, _password, _name, _ads, _gender, _age, _regitdate, _phone]
    _db = mod_sql.Database()
    _db.execute(sql, _values)
    _db.commit()

    return redirect(url_for('index'))

@app.route("/login/", methods=["POST"])
def login():
    _id = request.form["_id"] # id 키 값을 받아 옴
    _password = request.form["_password"]
    # print(_id, _password)    
    # # 1. index.html -> login url에 post형식으로 접속
    # ID, PASSWORD print출력
    
    sql = """
            SELECT * FROM user_info WHERE ID = %s AND password = %s
            """
            # WHERE ID = %s AND password = %s
    _values = [_id, _password]
    _db = mod_sql.Database()
    result = _db.executeAll(sql, _values)
    #print(result)

    if result:
        return render_template("welcome.html", 
                                name = result[0]["name"], 
                                id = result[0]["ID"]) #"Login"

    else:
        return redirect(url_for('index')) #"Fail" 
        

@app.route("/update")
def update():
    id = request.args["_id"]
    sql = """
            SELECT * FROM user_info WHERE ID = %s
            """
    values = [id]
    _db = mod_sql.Database()
    result = _db.executeAll(sql, values)
    return render_template("update.html", info = result[0])

@app.route("/update", methods = ["POST"])
def update_2():
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]
    sql = """
            UPDATE user_info SET 
            password = %s,
            name = %s,
            phone = %s,
            gender = %s,
            age = %s,
            ads = %s
            WHERE ID = %s
        """
    values = [_password, _name, _phone, _gender, _age, _ads, _id]
    _db = mod_sql.Database()
    _db.execute(sql, values)
    _db.commit()
    return redirect(url_for("index"))
    
    
    # return redirect(url_for('index'))
# 2. DB에서 SELECT문을 실행해서 uer_info table 정보를 print()출력
    
    
    
    #DB -> SELECT문을 사용 -> INDEX page input ID, PASSWORD 받아와서
    #SLECET문으로 조회
    #결과 값이 존재하면 return "login" 존재하지 않으면 return "Fail"
    # index.html 수정 main.py 수정
    

    
    # 3. SELECT문에 조건식을 추가하여 데이터의 유무 판별
app.run(port=8080)