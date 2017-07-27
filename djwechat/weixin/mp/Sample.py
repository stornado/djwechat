#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: jonyqin
# Created Time: Thu 11 Sep 2014 03:55:41 PM CST
# File Name: demo.py
# Description: WXBizMsgCrypt 使用demo文件
#########################################################################
from .WXBizMsgCrypt import WXBizMsgCrypt

if __name__ == "__main__":
    """ 
    1.第三方回复加密消息给公众平台；
    2.第三方收到公众平台发送的消息，验证消息的安全性，并对消息进行解密。
    """
    encodingAESKey = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFG"
    to_xml = """ <xml><ToUserName><![CDATA[oia2TjjewbmiOUlr6X-1crbLOvLw]]></ToUserName><FromUserName><![CDATA[gh_7f083739789a]]></FromUserName><CreateTime>1407743423</CreateTime><MsgType>  <![CDATA[video]]></MsgType><Video><MediaId><![CDATA[eYJ1MbwPRJtOvIEabaxHs7TX2D-HV71s79GUxqdUkjm6Gs2Ed1KF3ulAOA9H1xG0]]></MediaId><Title><![CDATA[testCallBackReplyVideo]]></Title><Descript  ion><![CDATA[testCallBackReplyVideo]]></Description></Video></xml>"""
    token = "spamtest"
    nonce = "1320562132"
    appid = "wx2c2769f8efd9abc2"
    # 测试加密接口
    # 


    appid = "wxb5a757fb3a5e159c"
    token = "0a0401007e1cb7ac372e91d53056318b"
    encodingAESKey = "fQ6FDBtJ6brvSxkwdic6MOwzrTpn9Kl2OkLfL1aZ8KB"
    to_xml = """<xml>
  <ToUserName><![CDATA[wxb5a757fb3a5e159c]]></ToUserName>
  <FromUserName><![CDATA[wxb5a757fb3a5e159c]]></FromUserName>
  <CreateTime>1489921033</CreateTime>
  <MsgType><![CDATA[text]]></MsgType>
  <Content><![CDATA[Received: text<br />推荐几篇文章给你看看 <a href="https://zxye.me/rss/">网源解析器</a>]]></Content>
</xml>"""

    to_xml2 = """<xml>
  <ToUserName><![CDATA[wxb5a757fb3a5e159c]]></ToUserName>
  <FromUserName><![CDATA[wxb5a757fb3a5e159c]]></FromUserName>
  <CreateTime>1489921033</CreateTime>
  <MsgType><![CDATA[text]]></MsgType>
  <Content><![CDATA[Received: text<br />To find interesting articles at <a href="https://zxye.me/rss/">FeedParser</a>]]></Content>
</xml>"""

    encryp_test = WXBizMsgCrypt(token, encodingAESKey, appid)
    ret, encrypt_xml = encryp_test.EncryptMsg(to_xml, nonce)
    print(ret, encrypt_xml)

    # 测试解密接口
    timestamp = "1409735669"
    msg_sign = "5d197aaffba7e9b25a30732f161a50dee96bd5fa"

    from_xml = """<xml><ToUserName><![CDATA[gh_10f6c3c3ac5a]]></ToUserName><FromUserName><![CDATA[oyORnuP8q7ou2gfYjqLzSIWZf0rs]]></FromUserName><CreateTime>1409735668</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[abcdteT]]></Content><MsgId>6054768590064713728</MsgId><Encrypt><![CDATA[hyzAe4OzmOMbd6TvGdIOO6uBmdJoD0Fk53REIHvxYtJlE2B655HuD0m8KUePWB3+LrPXo87wzQ1QLvbeUgmBM4x6F8PGHQHFVAFmOD2LdJF9FrXpbUAh0B5GIItb52sn896wVsMSHGuPE328HnRGBcrS7C41IzDWyWNlZkyyXwon8T332jisa+h6tEDYsVticbSnyU8dKOIbgU6ux5VTjg3yt+WGzjlpKn6NPhRjpA912xMezR4kw6KWwMrCVKSVCZciVGCgavjIQ6X8tCOp3yZbGpy0VxpAe+77TszTfRd5RJSVO/HTnifJpXgCSUdUue1v6h0EIBYYI1BD1DlD+C0CR8e6OewpusjZ4uBl9FyJvnhvQl+q5rv1ixrcpCumEPo5MJSgM9ehVsNPfUM669WuMyVWQLCzpu9GhglF2PE=]]></Encrypt></xml>"""

    signature = "d27c7c434476453b6951b337b44968ff3860d8d4"
    timestamp = "1489920496"
    nonce = "114184491"
    encrypt_type = "aes"
    msg_signature = "4bdd9f1c5294c47ef5232302d44e02845672697b"

    msg_sign = msg_signature
    from_xml = """<xml>
    <ToUserName><![CDATA[wxb5a757fb3a5e159c]]></ToUserName>
    <Encrypt><![CDATA[YgnIEAxraL0GJ1ecXws+fszyNgvnjfwgkZQNAwSW8VzUGfzAthGYfIqYaR2pboNaHrZ6yNVOj9lQiYLRduo6q9xtytamrWMbYSf/UpxxLXVris+9jAKS6q1A1MyLU3hD/kl+EDTaSPRUuaq/Ezt239R6Vwt6Q7QkFa+msFWIaSZw3Z7D4dbu1Zf5+cBNg6a4P3iqIBg6N3AJBPMfdMRHvoCgYCC11EGthXpd6eW95iiiAYkbcJNjrlY5uUW/xyyqIDa/YrwqLQKKbHV+JSAEuF6l/LZbU/I++Ke+hE/Aeyswza+bz1LtmZsfvRUQtOTkiTjAD+icS4nRXGDeW57ow7guZRB0KLzN29v4qnkM5nxGJWBaiOTQq9iXCSRYBvH2ydpXepLEzI69S24ASQ4mBDnZF+q15nKObyMfCKtTtN+345mLLpaeO+M2QPSKbbM1simBlr8ZNZTAyvIqcCIpwDQQyZ875DKISu19Sz2jJRbPJr/oJB8t1EwM9jtwh1jL]]></Encrypt>
</xml>"""
    decrypt_test = WXBizMsgCrypt(token, encodingAESKey, appid)
    ret, decryp_xml = decrypt_test.DecryptMsg(
        from_xml, msg_sign, timestamp, nonce)
    print(ret, decryp_xml)
