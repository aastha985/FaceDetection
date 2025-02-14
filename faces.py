import cv2

capture = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, frame = capture.read()
    if ret:
        faces = classifier.detectMultiScale(frame)
        for face in faces:
            x, y, w, h = face
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)
        cv2.imshow("My window", frame)
    key = cv2.waitKey(30)
    if key == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
