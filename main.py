import cv2
from cvzone.HandTrackingModule import HandDetector



class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 35, self.pos[1] + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def clicked(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and \
                self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (250, 250, 250), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (50, 50, 50), 3)
            cv2.putText(img, self.value, (self.pos[0] + 20, self.pos[1] + 70),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 5)

            return True
        else:
            return False


# webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Creating Buttons
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', '.', '='],
                    ['00', '%', '**', '<-']]
buttonList = []
for x in range(4):
    for y in range(5):
        xpos = x * 100 + 800
        ypos = y * 100 + 150
        buttonList.append(Button((xpos, ypos), 100, 100, buttonListValues[y][x]))

# variables
myEquation = ' '
delayCnt = 0

# loop0
while True:
    # get image from webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # detection of hand
    hands, img = detector.findHands(img, flipType=False)

    # draw all buttons
    cv2.rectangle(img, (800, 70), (800 + 400, 70 + 120), (500, 500, 500), cv2.FILLED)
    cv2.rectangle(img, (800, 70), (800 + 400, 70 + 120), (50, 50, 50), 3)
    for button in buttonList:
        button.draw(img)

    # check for hand
    if hands:
        lmList = hands[0]['lmList']
        length, _, img = detector.findDistance(lmList[8], lmList[12], img, 1)
        # print(length)
        x, y, z = lmList[8];
        if len(myEquation)<13:
            if length < 50:
                for i, button in enumerate(buttonList):
                    if button.clicked(x, y) and delayCnt == 0:
                        myValue = buttonListValues[int(i % 5)][int(i / 5)]
                        if myValue == "=":
                            myEquation = str(eval(myEquation))
                            break
                        elif myValue == "<-":
                            myEquation = myEquation.rstrip(myEquation[-1])
                            print(myEquation)
                        else:
                            myEquation += myValue
                        delayCnt = 1
    # avoid duplicates
    if delayCnt != 0:
        delayCnt += 1
        if delayCnt > 10:
            delayCnt = 0

    # display result
    cv2.putText(img, myEquation, (810, 120),
                cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    # display image
    cv2.imshow("Image", img)
    keyCode = cv2.waitKey(1)

    if keyCode == ord('c'):
        myEquation = ''

    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE)<1:
        break
cv2.destroyAllWindows()
