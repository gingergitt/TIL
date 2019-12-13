from flask import Flask, render_template , request
from decouple import config
import requests

app = Flask(__name__)


base = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text= request.args.get('message')

    requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return render_template('send.html')


@app.route(f'/{token}', methods=['POST']) #외부에서의 접근 방지
def telegram():
    # step1. 구조 print해보기 & 변수저장
    print(request.get_json()) 
    from_telegram = request.get_json()

    #step2. 그대로 돌려보내기
    if from_telegram.get('message') is not None : # NoneType일 경우만 예외처리.
        chat_id = from_telegram.get('message').get('from').get('id')
         #.get()으로 받아오는것이 get['']보다 낫다. 
        #[]는 값이 없을 경우에 에러가 날 가능성이 크기 때문.
        
        text = from_telegram.get('message').get('text')
        url=  f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(url)
    return '', 200


#ngrok를 cmd창에서 켰을 때, 끄지말것(해쉬값이 바뀜)
#ngrok : 사용자의 데이터(값)을 받아올 때, 방화벽에 막히지 않도록 알려주는 기능
#webhook: 이벤트가 발생했다는 것을 알려줌