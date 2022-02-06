import firebase_admin
from firebase_admin import db
from datetime import date, datetime

class Database():
    def __init__(self):
        cred_obj = firebase_admin.credentials.Certificate('uofthacksix-36bd1-firebase-adminsdk-qtyvc-e5c215b7f2.json')
        default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://uofthacksix-36bd1-default-rtdb.firebaseio.com/"
        })
        self.reference = self._setRef()

    def addStudent(self, firstName, lastName, studentNum, date):
        self.reference = self._setRef()
        
        currData = self.reference.get().keys()

        if str(studentNum) in currData:
            return "Already checked in"
        
        currRef = self.reference.child(str(studentNum))
 

        if self.currentDate != date:
            return 'Wrong date'

        try:
            currTime = datetime.now().strftime("%H:%M:%S")
            currRef.set({
                'first name': firstName,
                'last name': lastName,
                'student number': studentNum,
                'time': currTime
            })
            
            return 'Success'

        except:
            return 'Error'


    def _setRef(self):
        self.currentDate = date.today().strftime("%m/%d/%y")
        reference = db.reference(f"/{self.currentDate}")
        
        return reference


