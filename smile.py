import cv2
from PIL import ImageDraw

smile_classify = cv2.CascadeClassifier('C:/Python39/Lib/site-packages/cv2/haar-cascade-files-master/haar-cascade-files-master/haarcascade_smile.xml')
face_classify = cv2.CascadeClassifier('C:/Python39/Lib/site-packages/cv2/haar-cascade-files-master/haar-cascade-files-master/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
ret,img = cap.read()
i=0
while(True):

    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    face = face_classify.detectMultiScale(gray, 1.3, 5)
    #print(smile)
    #i+=1
    for (xf,yf,wf,hf) in face:
        cv2.rectangle(img,(xf,yf),(xf+wf,yf+hf),(255,0,0),2)
        roi = gray[yf:yf+hf, xf:xf+wf]

        smile = smile_classify.detectMultiScale(roi, 1.7, 20)
        for (xs,ys,ws,hs) in smile:
            cv2.rectangle(img,(xs,ys),(xs+ws,ys+hs),(0,255,0),2)

    cv2.imshow("FEED",gray)
    if(cv2.waitKey(1)==13):
        break

cap.release()
cv2.destroyAllWindows()