# coding: utf8
import requests
import json
import cv2
import base64

def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tobytes()).decode('utf8')


if __name__ == '__main__':
    # 发送HTTP请求

        data = {'images':[cv2_to_base64(cv2.imread("rotated_{}.jpg".format()))]}

        headers = {"Content-type": "application/json"}
        url = "http://127.0.0.1:8866/predict/chinese_ocr_db_crnn_mobile"
        r = requests.post(url=url, headers=headers, data=json.dumps(data))

        # 打印预测结果
        print(r.content)
        print(r.json()["results"])

