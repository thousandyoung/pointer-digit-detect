# coding: utf8
import requests
import json
import cv2
import base64
import numpy as np


def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tobytes()).decode('utf8')


# 返回((x0,y0), (x1,y1))
# 1为0之后的第一个示数
# r = requests.post(url=url, headers=headers, data=json.dumps(data))
def get_0_1_position(r):
    r_list = r.json()['results'][0]['data']
    # print(isinstance(r_list,list))
    # sort by 'text'
    r_list = filter(lambda dict: dict['text'].isdigit(), r_list)
    r_list = list(r_list)
    r_list.sort(key=lambda dict: int(dict['text']))
    text_box_position_0 = r_list[0]['text_box_position']
    text_box_position_1 = r_list[1]['text_box_position']
    position_0 = get_text_box_position(text_box_position_0)
    position_1 = get_text_box_position(text_box_position_1)
    # print(position_0, position_1)
    return position_0, position_1


# 返回[x,y]
def get_text_box_position(l):
    x_sum, y_sum = 0, 0
    for item in l:
        x_sum += item[0]
        y_sum += item[1]
    return x_sum / 4, y_sum / 4


if __name__ == '__main__':
    # 发送HTTP请求
    data = {'images': [cv2_to_base64(cv2.imread("5.jpg"))]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/chinese_ocr_db_crnn_mobile"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    # 打印预测结果
    print(r.content)
    print(r.json()["results"])
    print(get_0_1_position(r))
