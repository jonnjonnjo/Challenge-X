from tkinter import *

root = Tk()



def clik():
    import pathlib
    import cv2
    import numpy as np
    font = cv2.FONT_HERSHEY_COMPLEX
    count = 0

    cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

    clf = cv2.CascadeClassifier(str(cascade_path))

    camera = cv2.VideoCapture(0)

    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
            if(count <= 100):
                cv2.putText(frame, str(count) + "% CAKEP" , (x-50, y ), font , 1, (2555,255,255),1 )
            else:
                cv2.putText(frame, "1000000% CAKEP:D", (x - 50, y), font, 1, (2555, 255, 255), 1)

        cv2.imshow("Faces", frame)
        if (cv2.waitKey(1) == ord("q")):
            break

        count+=1

    camera.release()
    cv2.destroyAllWindows()

clicked = Button(root, text = "mau liat orang tercakep ga? (* ^ ω ^) ", command = clik)
clicked.pack()


root.mainloop()