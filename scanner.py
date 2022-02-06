import cv2 as cv
import pyzbar.pyzbar as pyzbar
import ast
from database import Database

def scanQR(db):
    cap = cv.VideoCapture(0)
    data = ""   
    successful = False
    while True:
        _, frame = cap.read()

        decoded = pyzbar.decode(frame)
        if (decoded):
            try:
                data = ast.literal_eval(str(decoded[0].data)[2:-1])
            except:
                back = "Not functional"
            (x, y, w, h) = decoded[0].rect

            if (len(data) > 0):
                print(data)
                try:
                    firstname = data['firstName']
                    lastname = data['lastName']
                    studentNum = data['num']
                    date = data['date']
                except:
                    back = "Not functional"

                back = db.addStudent(firstname, lastname, studentNum, date)
            if back == "Success" or successful:
                color = (0, 255, 0)
                cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                successful = True
                cv.putText(frame, 'Success', (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            else:
                color = (0, 0, 255)
                cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv.putText(frame, back, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                

        else:
            successful = False
        cv.imshow("Scanner", frame)

        if (cv.waitKey(1) == ord("q")):
            break


if (__name__ == "__main__"):
    newDatabase = Database()
    scanQR(newDatabase)
