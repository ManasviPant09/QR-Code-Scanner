import cv2
import webbrowser
capture = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _,image = capture.read()
    data,one, _= detector.detectAndDecode(image)
    if data:
        a = data
        break
    cv2.imshow('QR Code Scanner',image)
    if cv2.waitKey(1)==ord('q'):
        break
b = webbrowser.open(str(a))
capture.release(a)
cv2.destroyAllWindows()