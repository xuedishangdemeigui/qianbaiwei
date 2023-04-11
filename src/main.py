from flask import Flask, request
import hashlib
from datetime import datetime
from config import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def parse_unix_time(unix_time: any) -> str:
    return datetime.utcfromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')


@app.route("/wx", methods=['GET'])
def wx_handler():
    try:
        if len(request.args) == 0:
            return "hello, this is handle view"

        signature = request.args.get("signature")
        timestamp = request.args.get("timestamp")
        nonce = request.args.get("nonce")
        echostr = request.args.get("echostr")

        print("[INFO] sig: {}, timestamp: {}, nonce: {}, echostr: {}".format(
            signature, parse_unix_time(timestamp), nonce, echostr), flush=True)

        token = TOKEN  # 请按照公众平台官网\基本配置中信息填写

        list = [token, timestamp, nonce]
        list.sort()

        sha1 = hashlib.sha1()
        for str in list:
            sha1.update(str.encode("utf-8"))
        hashcode = sha1.hexdigest()

        return echostr if hashcode == signature else ""
    except Exception as Argument:
        print("[ERROR] Exception: {}".format(Argument))
        return Argument
