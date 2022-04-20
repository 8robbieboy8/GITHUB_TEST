from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')

def index():
    return render_template('index.html')

@app.route('/second/') #같은 피씨기 때문 세컨페이지에 아이디, 페스워드 만들어 주는 이유는 url이 받는 페이지는 세컨드기 때문
def second():          #같은 피씨기 때문 인덱스에 아이디 페스워드는 그냥 표시일 뿐/ 실제 받는 페이지는 세컨드
    _id = request.args.get("id")
    _pass = request.args.get("pass")
    print(_id, _pass)
    return render_template("second.html", id = _id, _pass = _pass )
    
    
    # if _id == "asd" and _pass == "qwe":
    #    return render_template('second.html')
    #else:
    #    return "로그인에 실패하였습니다"
        # return render_template("")


@app.route('/third/', methods=['POST']) #포스트 형식의 url만 받는다. 직접 쳐서는 못들어 간다. 
def third():
    _id =  request.form['id']
    _pass = request.form['pass']
    print(_id, _pass) #갈호 안에 request.form를 넣으면, 
    return "hello"




app.run