#!/usr/bin/env python
# coding=utf-8

#
# curl -d '{"sessionId":"1234","question":"生活缴费","account":"1212323","pubkey":"ll/mfInZhwTrMLjGyL4TEBrDpuV43PfK82jk2wHngwk","sign":"53EBFDB952855784017A28E331E2395A","ip":"127.0.0.1","type":"NLU","openId":"12","channel":"ATP","sessionId":"asae","appId":"sfa","version":"v1.0.0","sessionRound":"1", "queryId":"asae","userId":"ergqerq"}'
# 127.0.0.1:8000/Robot/query
#
#
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import urllib
import urllib2
import json
import hashlib
import time
import logging
import thread
import random
import string

# geturl = "http://127.0.0.1:1080/robotv1/query"
# geturl = "http://127.0.0.1:1080/Robot/query"
geturl666 = "http://127.0.0.1:6666/Robot/query"

timeformat = time.localtime(time.time())
timestr = time.strftime("%Y%m%d-%H%M%S", timeformat)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(thread)d -%(relativeCreated)d %(filename)s[line:%(lineno)d] %(levelname)s %(message)s ',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./log/' + timestr + '.log',
                    filemode='a')


def postResultFromServer(reqJson, url):
    request = urllib2.Request(url.encode('utf-8'))
    request.add_data(json.dumps(reqJson))
    try:
        ret = urllib2.urlopen(request, data=None, timeout=10)  # 设置timeout之后read超时会抛出socket.timeout异常
    except:
        return "time out"
    if ret.getcode() != 200:
        return "not 200"
    return ret.read()


def get_md5(pas):
    m2 = hashlib.md5()
    m2.update(pas)
    md5 = m2.hexdigest()
    print
    "md5:" + md5
    return md5


def do_robot_query_666():
    requestinfo = {}
    requestinfo["question"] = "利息多少"
    requestinfo["account"] = "1212323"
    requestinfo["ip"] = "127.0.0.1"
    requestinfo["type"] = "NLU"
    requestinfo["openId"] = "12"
    requestinfo["channel"] = "ATP"
    requestinfo["labels"] = "WeiXin"
    requestinfo["sessionId"] = "asae"
    requestinfo["appId"] = "sfa"
    requestinfo["version"] = "v1.0.0"
    requestinfo["sessionRound"] = "1"
    requestinfo["queryId"] = "asae"
    requestinfo["userId"] = "ergqerq"
    requestinfo["pubkey"] = "STFxLaUA5PrK5Cvf7eYKiujI9P58eeKeBWd8AImzz40"
    requestinfo["sign"] = "53EBFDB952855784017A28E331E2395A"
    # "pubkey":"STFxLaUA5PrK5Cvf7eYKiujI9P58eeKeBWd8AImzz40","sign":"53EBFDB952855784017A28E331E2395A"

    with open('faq_top_16k.txt_bak', 'r') as f:
        for line in f:
            logging.info(">>" + line.strip())
            requestinfo["question"] = line.strip()
            starttime = int(time.time() * 1000)  # ms

            res = postResultFromServer(requestinfo, geturl666)
            endtimetime = int(time.time() * 1000)  # ms
            print
            'cost time:' + str(endtimetime - starttime) + 'ms'
            logging.info('cost time:' + str(endtimetime - starttime) + 'ms')
            try:
                resjson = json.loads(res)
            except:
                print
                'error'
            # print res
            logging.info(res)
    return


def do_robotv1_query(loops, threadnum):
    requestinfo = {}
    requestinfo["sessionId"] = "1234-" + str(threadnum) + "-" + str(time.time())
    print
    requestinfo["sessionId"]
    requestinfo["question"] = "利息多少"
    requestinfo["account"] = "1212323"
    requestinfo["ip"] = "127.0.0.1"
    requestinfo["type"] = "NLU"
    requestinfo["openId"] = "12"
    requestinfo["channel"] = "WeiXin"
    requestinfo["labels"] = "WeiXin"
    requestinfo["sessionId"] = "asae"
    requestinfo["appId"] = "sfa"
    requestinfo["version"] = "v1.0.0"
    requestinfo["sessionRound"] = "1"
    requestinfo["queryId"] = "asae"
    requestinfo["userId"] = "ergqerq"

    j = 0
    for i in range(0, loops):
        with open('faq_top_16k.txt_bak', 'r') as f:
            for line in f:
                logging.info(">>" + line.strip())
                requestinfo["question"] = line.strip()
                j += 1
                if j % 2 == 0:
                    # requestinfo["sessionId"] = ''.join(random.sample(string.ascii_letters + string.digits, 8))
                    requestinfo["sessionId"] = "1212"
                    print
                    requestinfo["sessionId"]
                    # requestinfo["sessionId"] = "1234-" + str(threadnum) + "-" + str(time.time())
                else:
                    # requestinfo["sessionId"] = ''.join(random.sample(string.ascii_letters + string.digits, 8))
                    requestinfo["sessionId"] = "1212"
                starttime = int(time.time() * 1000)  # ms

                res = postResultFromServer(requestinfo, geturl)
                endtimetime = int(time.time() * 1000)  # ms
                print
                'cost time:' + str(endtimetime - starttime) + 'ms'
                logging.info('cost time:' + str(endtimetime - starttime) + 'ms')
                try:
                    resjson = json.loads(res)
                except:
                    resjson = " 1001 "
                # print res
                logging.info(res)
            else:
                f.close()
    return


def print_ret():
    print
    1


if __name__ == "__main__":
    print
    "请输入python yibot_stress_test.py 3[线程数] 10[最多压测时间H] 0[新]/1[旧]/2[人机] "
    threadnum = int(sys.argv[1])
    loops = int(sys.argv[2])
    types = int(sys.argv[3])
    if types == 0:
        for i in range(0, threadnum):
            thread.start_new_thread(do_robotv1_query, (loops, i))
            # thread.start_new_thread( do_robotv1_query, (loops, i) )
            print
            "tread" + str(i) + "....."
            time.sleep(2)  # 10秒
    if types == 1:
        for i in range(0, threadnum):
            thread.start_new_thread(do_robotv1_query, (loops, i))
            print
            "tread" + str(i) + "....."
            time.sleep(5)  # 10秒
    if types == 2:
        for i in range(0, threadnum):
            thread.start_new_thread(do_robot_query_666, ())
            print
            "tread" + str(i) + "....."
            time.sleep(5)  # 10秒
    time.sleep(60 * 60 * loops)



