from flask import Flask, render_template , request
import datetime
import random
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/t4ir')
def t4ir():
    return 'this is t4ir'

if __name__=='__main__':
    app.run(debug=True)

@app.route('/t4ir')
def t4ir():
    return 'This is T4IR'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end=datetime.datetime(2020, 4, 21)
    td = end - today
    return f'{td.days}일 남았습니다.'

@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route('/greeting/<name>')
    def greeting(name):
        # return f'반갑습니다. {name}님'
        return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 3제곱 {number**3}'


@app.route('/lunch/<int:people>')
def lunch(people):
    menu =['짜장면','짬뽕','볶음밥']
    order = random.sample(menu, people)
    return str(order)

@app.route('/')
def hello():

@app.route('/ping')
def ping():
        return render_template('ping.hmtl')

@app.route('/pong')
def pong() :
    age = request.args.get('age')
    return render_template('pong.html', age_in_html =age)


@app.route('/naver')
def naver():
        return render_template('naver.html')

@app.route('/google')
def google():
        return render_template('google.html')

@app.route('/isitbirth')
def isitbirth():
    today = datetime.now()
    if today.month == 1 and today.day = 3:
        result = True
    else:
        result = False
    return render_template('isitbirth.html', result=result)

@app.route('/vonvon')
def vonvon():
        return render_template('vonvon.html')

@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    first_list=['잘생김','못생김','어중간']

