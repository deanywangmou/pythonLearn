#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
aa=sys.path.append("../")
print(sys.path)
import json
import requests


def send_data_all(adaptorfile, interface, cnt):
    with open(adaptorfile) as ADA:
        count = 0
        for line in ADA:
            print(">>>>")
            print(line)
            r = requests.post(url=interface, data=line)
            print("<<<<\n" + r.text)
            count += 1
            if count >= cnt:
                break


if __name__ == '__main__':
    cnt = sys.argv[1]
    cnt = int(cnt)
    gen = sys.argv[2]
    fed = sys.argv[3]
    if cnt > 10:
        url = "http://10.4.1.156:10102/yibot-receiver/receiver/adaptor"
        send_data_all(gen, url, cnt)
        url = "http://10.4.1.156:10102/yibot-receiver/receiver/feedback"
        send_data_all(fed, url, cnt)
    else:
        url = "http://10.4.1.156:10102/yibot-receiver/receiver/adaptor"
        send_data_all(gen, url, cnt)
        url = "http://10.4.1.156:10102/yibot-receiver/receiver/feedback"
        send_data_all(fed, url, cnt)
