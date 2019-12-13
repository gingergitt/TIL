from flask import Flask, render_template , request
from decouple import config
import requests

app = Flask(__name__)


base = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
#PAPAGO API
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

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
    # print(request.get_json()) 
    from_telegram = request.get_json()

    #step2. 그대로 돌려보내기
    if from_telegram.get('message') is not None : # NoneType일 경우만 예외처리.
        chat_id = from_telegram.get('message').get('from').get('id')
         #.get()으로 받아오는것이 get['']보다 낫다. 
        #[]는 값이 없을 경우에 에러가 날 가능성이 크기 때문.
        
        text = from_telegram.get('message').get('text')
       
        

        if text[0:4] == '/번역 ':  #text에 첫 4글자가 번역결과로 나오도록.
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
             } #decouple로 숨겨놓았던..

            data = {'source':'ko', 'target':'ja', 'text':text[4:]} #text에 4번째 뒤로, 받아온 번역문을 집어넣겠다
            #개발자센터의 주소를 받아오면서 헤더정보와 data정보를 같이 넘겨주도록 한다.
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')
        requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

       


        # if text[0:4] == '/로또 ': 
        #     num = text[4:]
        #     res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwtNo={num}')
        #     lotto = res.json()

        #     winner = []
        #     for i in range(1,7):
        #         winner.append(lotto[f'drwtNo{i}'])
        #     bonus_num =lotto['bnusNo']
        #     text = f'{num}회차 로또 당첨번호는 {winner}입니다.'

         
    return '', 200


#ngrok를 cmd창에서 켰을 때, 끄지말것(해쉬값이 바뀜)
#ngrok : 사용자의 데이터(값)을 받아올 때, 방화벽에 막히지 않도록 알려주는 기능
#webhook: 이벤트가 발생했다는 것을 알려줌