from flask import Flask

app = Flask(__name__) #네임은 파일명

@app.route('/') #localhost5000 뒤에 아무것도 없을때 이 함수를 실행하겠다.
def index():
    return "Hello, World"

#url를 추가해서 def를 실행을 하려면? 어떻게?

@app.route('/second/') #세컨드 뒤에 / 붙여주는게 좋다.
def second():  #함수명 같게 하지 마라 오류 날 수 있음
    return 'Second Page first'

app.run #http://127.0.0.1:5000/ 127.0.0.1 = localhost와 같다. 


