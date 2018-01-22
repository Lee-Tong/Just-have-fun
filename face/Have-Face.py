import cv2 as cv

import os

classifier = os.getcwd()+'/haarcascade_frontalface_default.xml'

face_casacade = cv.CascadeClassifier(classifier)

windowName = "Object Detection"
	
cap = cv.VideoCapture(0)
# 识别人脸	
def detect(img, cascade):
	rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),flags=cv.CASCADE_SCALE_IMAGE)
	return len(rects)
shot_idx = 0
while True:
	imgs = []
	# 读取摄像头照片
	ret, img = cap.read()
	# 灰度转换
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	gray = cv.equalizeHist(gray)
	# 识别
	rects = detect(gray, face_casacade)
	vis = img.copy()
	imgs.append(img)
	if rects != 0:
		for i, img in enumerate(imgs):
			fn = '%s/shot_%d_%03d.bmp' % ("/", i, shot_idx)
			# 写入图片
			cv.imwrite(fn, img)
			print(fn, 'saved')
			shot_idx += 1
	cv.imshow('facedetect', vis)
	
	# 按q键退出
	ch = cv.waitKey(1)
		
	if cv.waitKey(1) & 0xFF == ord('q'):
		break;
		
cv.destroyAllWindows()