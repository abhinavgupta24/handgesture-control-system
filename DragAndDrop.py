import HandTrackingModule as HandDetector
import cv2
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 1080)     #width of video
cap.set(4, 720)     #height of video
detector = HandDetector.handDetector(detectionCon=0.8)
colorR = (250, 0, 250)   #default color of rectangle
cx, cy, w, h = 100, 100, 200, 200

class DragRect():
    def __init__(self,posCenter,size=[150, 150]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # if th index finger tip in the rectangle region
        if (cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2):
            self.posCenter = cursor

rectList = []
for x in range(5):
    rectList.append(DragRect([x*250+150, 150]))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)          #horizontal flip=1, vertical flip=0
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if lmList:
        l, _, _ = detector.findDistance(8, 12,lmList, img)
        if l < 30:
            cursor = lmList[8][1], lmList[8][2]
            for rect in rectList:
                rect.update(cursor)
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), colorR, cv2.FILLED)     # (x,y),(width,height),color,
        cvzone.cornerRect(img, (cx-w//2, cy-h//2, w, h), 20, rt=0)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
        break
cv2.destroyAllWindows()
