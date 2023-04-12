from flask import Flask, request
import hashlib
from config import *
from utils import *
import receive
import reply
from functools import wraps

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def check_req_source(req: request) -> bool:
    try:
        if len(request.args) == 0:
            return False

        sig = request.args.get("signature")
        timestamp = request.args.get("timestamp")
        nonce = request.args.get("nonce")

        token = TOKEN  # 请按照公众平台官网\基本配置中信息填写
        list = [token, timestamp, nonce]
        list.sort()

        sha1 = hashlib.sha1()
        for str in list:
            sha1.update(str.encode("utf-8"))
        hashcode = sha1.hexdigest()

        return hashcode == sig
    except Exception as Argument:
        print("[ERROR] Exception: {}".format(Argument))
        return False


def check_req_source_decorator():
    def out_wrapper(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            if not check_req_source(request):
                return "hello world!"
            return f(*args, **kwds)
        return wrapper
    return out_wrapper


@app.route("/wx", methods=['GET'])
@check_req_source_decorator()
def wx_check_handler():
    if check_req_source(request):
        return request.args.get("echostr")
    return "hello world!"


@app.route("/wx", methods=['POST'])
@check_req_source_decorator()
def wx_msg_handler():
    try:
        if not check_req_source(request):
            return "hello world!"

        rec_msg = receive.parse_xml(request.data)

        if isinstance(rec_msg, receive.Msg) and rec_msg.msg_type == 'text':
            to_user = rec_msg.from_user_name
            from_user = rec_msg.to_user_name
            content = "你好呀，傻猪儿！"
            reply_msg = reply.TextMsg(to_user, from_user, content)
            return reply_msg.send()
        return "hello world!"
    except Exception as Argument:
        print("[ERROR] Exception: {}".format(Argument))
        return "hello world!"


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)
