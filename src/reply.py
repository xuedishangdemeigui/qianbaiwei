# -*- coding: utf-8 -*-#
# filename: reply.py
import time


class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, to_user_name, from_user_name, content):
        self.__dict = dict()
        self.__dict['to_user_name'] = to_user_name
        self.__dict['from_user_name'] = from_user_name
        self.__dict['create_time'] = int(time.time())
        self.__dict['content'] = content

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{to_user_name}]]></ToUserName>
                <FromUserName><![CDATA[{from_user_name}]]></FromUserName>
                <CreateTime>{create_time}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{content}]]></Content>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class ImageMsg(Msg):
    def __init__(self, to_user_name, from_user_name, media_id):
        self.__dict = dict()
        self.__dict['to_user_name'] = to_user_name
        self.__dict['from_user_name'] = from_user_name
        self.__dict['create_time'] = int(time.time())
        self.__dict['media_id'] = media_id

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{to_user_name}]]></ToUserName>
                <FromUserName><![CDATA[{from_user_name}]]></FromUserName>
                <CreateTime>{create_time}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                <MediaId><![CDATA[{media_id}]]></MediaId>
                </Image>
            </xml>
            """
        return XmlForm.format(**self.__dict)
