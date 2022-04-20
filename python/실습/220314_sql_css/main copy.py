from flask import Flask, redirect, render_template, request, redirect, url_for
import pymysql

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
    _db = pymysql.connect(
    user = "root",
    password= "dkrkwk18!",
    host = "localhost",
    db = "ubion"
    )
    cursor = _db.cursor()
    
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
    cursor.execute(sql, _values)
    _db.commit()
    _db.close()

    return redirect(url_for('index'))

@app.route("/login/", methods=["POST"])
def login():
    _id = request.form["_id"] # id 키 값을 받아 옴
    _password = request.form["_password"]
    # print(_id, _password)    
    # # 1. index.html -> login url에 post형식으로 접속
    # ID, PASSWORD print출력
    
    _db = pymysql.connect(
    user = "root",
    password= "dkrkwk18!",
    host = "localhost",
    db = "ubion"
    )
    cursor = _db.cursor()
    sql = """
            SELECT * FROM user_info WHERE ID = %s AND password = %s
            """
    _values = [_id, _password]
    cursor.execute(sql, _values)
    result = cursor.fetchall()
    _db.close()
    print(result)

    if result:
        return "Login"

    else:
        return "Fail"
        


    # return redirect(url_for('index'))
# 2. DB에서 SELECT문을 실행해서 uer_info table 정보를 print()출력
    
    
    
    #DB -> SELECT문을 사용 -> INDEX page input ID, PASSWORD 받아와서
    #SLECET문으로 조회
    #결과 값이 존재하면 return "login" 존재하지 않으면 return "Fail"
    # index.html 수정 main.py 수정
    

    
    # 3. SELECT문에 조건식을 추가하여 데이터의 유무 판별
app.run(port=8080)