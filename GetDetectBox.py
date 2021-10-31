import os
def GenerateBox(imagePath):
    flag = os.system("python3 PaddleOCR-release-2.3/tools/infer/predict_det.py --det_algorithm=\"SAST\" --image_dir=\"{}\" --det_model_dir=\"PaddleOCR-release-2.3/inference/det_sast_tt/\" --det_sast_polygon=True --use_gpu=False".format(imagePath))
    if flag == 1:
        print("generate box failed")

GenerateBox("./images/panel.jpeg")
