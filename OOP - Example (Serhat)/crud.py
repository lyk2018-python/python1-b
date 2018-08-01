import json
import os
import uuid

class User:
    def __init__(self):
        self.isim = ""
        self.soyisim = ""
        self.numara = ""

class DatabaseMethods:
    def __init__(self):
        self.path = "database.json"
        self.Create_Database_If_Not_Exists()

    def Check_UserID(self, user_id):
        with open(self.path, "r") as f:
            js = json.load(f)

        #if user_id in js:
        #    return True
        #else:
        #    return False

        #return True if user_id in js else False

        return user_id in js

    def Create_Database_If_Not_Exists(self):
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

    def add(self, user):
        with open(self.path, "r") as f:
            js = json.load(f)

        js.update({
            str(uuid.uuid1()) : user.__dict__
        })

        with open(self.path, "w") as f:
            json.dump(js, f)

    def update(self, user_id, user):
        with open(self.path, "r") as f:
            js = json.load(f)
        
        # exist_check = js.get(user_id, False)
        # if not exist_check:
        #     return False
        
        if user_id in js:
            js[user_id] = user.__dict__

        with open(self.path, "w") as f:
            json.dump(js, f)

    def get(self):
        with open(self.path) as f:
            js = json.load(f)
        return js

    def delete(self, user_id):
        result = False
        with open(self.path, "r") as f:
            js = json.load(f)

        if user_id in js:
            del js[user_id]
            result = True

        with open(self.path, "w") as f:
            json.dump(js, f)

        return result