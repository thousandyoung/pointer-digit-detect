# coding: utf8
import requests
import json
import cv2
import base64
import numpy as np


def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tobytes()).decode('utf8')

#输出[{},{}...]
def getOcrResult(r):
    r_list = r.json()['results'][0]['data']
    # sort by 'text'
    r_list = filter(lambda dict: dict['text'].isdigit(), r_list)
    r_list = list(r_list)
    r_list.sort(key=lambda dict: int(dict['text']))
    return r_list



if __name__ == '__main__':
    # 发送HTTP请求
    data = {'images': [cv2_to_base64(cv2.imread("5.jpg"))]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/chinese_ocr_db_crnn_mobile"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    print(getOcrResult(r))




