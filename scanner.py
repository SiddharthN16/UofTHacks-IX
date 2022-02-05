import cv2 as cv
import pyzbar.pyzbar as pyzbar
import ast


def scanQR():
    cap = cv.VideoCapture(0)
    data = ""

    while True:
        _, frame = cap.read()

        decoded = pyzbar.decode(frame)
        if (decoded):
            data = ast.literal_eval(str(decoded[0].data)[2:-1])

        if (len(data) > 0):
            print(data)
            break

        cv.imshow("Scanner", frame)

        if (cv.waitKey(1) == ord("q")):
            break


if (__name__ == "__main__"):
    scanQR()
