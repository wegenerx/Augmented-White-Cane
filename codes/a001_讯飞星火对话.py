import _thread as thread
import base64
import datetime
import hashlib
import hmac
import json
from urllib.parse import urlparse
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import websocket  # 使用websocket_client

global answer
answer = ""
import time


def func():
    print('func start')
    time.sleep(1)
    print('func end')






class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, Spark_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(Spark_url).netloc
        self.path = urlparse(Spark_url).path
        self.Spark_url = Spark_url

    # 生成url
    def create_url(self):
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 拼接鉴权参数，生成url
        url = self.Spark_url + '?' + urlencode(v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        return url


# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)


# 收到websocket关闭的处理
def on_close(ws, one, two):
    print(" ")


# 收到websocket连接建立的处理
def on_open(ws):
    thread.start_new_thread(run, (ws,))


def run(ws, *args):
    data = json.dumps(gen_params(appid=ws.appid, domain=ws.domain, question=ws.question))
    ws.send(data)


# 收到websocket消息的处理
def on_message(ws, message):
    global answer
    # print(message)
    data = json.loads(message)
    code = data['header']['code']
    if code != 0:
        print(f'请求错误: {code}, {data}')
        ws.close()
    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]
        print(content, end="")
        answer += content  # 原来是 +=
        # print(1)
        if status == 2:
            ws.close()


def gen_params(appid, domain, question):
    """
    通过appid和用户的提问来生成请参数
    """
    data = {
        "header": {
            "app_id": appid,
            "uid": "1234"
        },
        "parameter": {
            "chat": {
                "domain": domain,
                "random_threshold": 0.5,
                "max_tokens": 2048,
                "auditing": "default"
            }
        },
        "payload": {
            "message": {
                "text": question
            }
        }
    }
    return data


def main(appid, api_key, api_secret, Spark_url, domain, question):

    # 以下密钥信息从控制台获取
    appid = "f1f8e784"  # 填写控制台中获取的 APPID 信息
    api_secret = "NjNlY2YyOTIxZmRhNWRlOGQzMjRlZjJm"  # 填写控制台中获取的 APISecret 信息
    api_key = "7e0856a5d8023644862059179e2bc02c"  # 填写控制台中获取的 APIKey 信息

    # 版本与api地址：https://www.xfyun.cn/doc/spark/Web.html#%E5%BF%AB%E9%80%9F%E8%B0%83%E7%94%A8%E9%9B%86%E6%88%90%E6%98%9F%E7%81%AB%E8%AE%A4%E7%9F%A5%E5%A4%A7%E6%A8%A1%E5%9E%8B-python%E7%A4%BA%E4%BE%8B
    domain = 'generalv3.5'  # 云端环境的服务地址
    Spark_url = "ws://spark-api.xf-yun.com/v3.5/chat"  # v3.0环境的地址

    # print("星火:")
    wsParam = Ws_Param(appid, api_key, api_secret, Spark_url)
    # websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.question = question
    ws.domain = domain
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})




text = []


# length = 0

def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text


def process_input_and_get_answer(input_text, appid, api_key, api_secret, Spark_url, domain):

    global answer

    # 假设 `text` 是一个具有 `clear` 方法的对象
    text.clear()  # 如果text是一个列表或其他容器，那么使用 text.clear() 清除内容

    # 检查输入长度，这里我们假设 `checklen` 函数返回一个有效的问题字符串
    question = checklen(getText("user", input_text))

    # 初始化answer变量
    answer = ""

    # 打印星火前缀，这可能是与AI助手的交互提示
    print("星火:", end="")

    # 调用主逻辑函数处理问题，这里我们假设它改变了answer变量的值
    main(appid, api_key, api_secret, Spark_url, domain, question)

    # 从助手获取答案，这里我们假设getText会返回助手的回答并更新answer
    getText("assistant", answer)

    answer_temp = answer
    answer = ''

    # 返回答案
    return str(answer_temp)



if __name__ == '__main__':
    text.clear
    time_list = []
    while 1:
        Input = input("\n我:")
        t = time.time()

        question = checklen(getText("user", Input))
        answer = ""
        print("星火:", end="")
        main(appid, api_key, api_secret, Spark_url, domain, question)
        print(answer)
        print(f'coast:{time.time() - t:.4f}')
        time_list.append(float(f'{time.time() - t:.4f}'))
        print(time_list)
        # getText("assistant", answer)
        # 现在我在导盲雷达上与你对话，请生成‘人行横道上障碍物密集’的语音播报
        # a = [1.6838,1.6665,1.7309 ]
