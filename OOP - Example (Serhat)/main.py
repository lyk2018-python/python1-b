import os
import sys
from pprint import pprint
from crud import User, DatabaseMethods

class ConsoleProgram:
    def __init__(self):
        self.main_choice = ""
        self.choices_list = ["1", "2", "3", "4"]
    
    def Main_Page(self):
        print("Hoşgeldiniz...")
        while True:
            print("1. Kayıtları Göster")
            print("2. Ekle")
            print("3. Güncelle")
            print("4. Sil")
            self.main_choice = input()
            if self.main_choice in self.choices_list:
                break
            self.Clear_Screen()
            print("Girdiniz değer yanlıştır!")

    def Goto_Choice(self):
        db = DatabaseMethods()

        if self.main_choice == "1": # Get
            pprint(db.get())
        
        elif self.main_choice == "2": # Add
            db.add(self.Get_User())
            pprint(db.get())
        
        elif self.main_choice == "3": # Update
            user_id = input("User ID : ")
            if db.Check_UserID(user_id):
                db.update(user_id, self.Get_User())
                print("Kullanıcı güncellendi.")
            else:
                print("Kullanıcı bulunamadı.")

            pprint(db.get())
        
        elif self.main_choice == "4": # Delete
            user_id = input("Kullanıcı ID giriniz : ")
            
            if db.delete(user_id):
                print("Kullanıcı silindi.")
            else:
                print("Böyle bir kullanıcı bulunamadı.")

            pprint(db.get())

    @staticmethod
    def Clear_Screen():
        os.system("cls" if sys.platform == "nt" else "clear")

    @staticmethod
    def Get_User():
        user = User()
        user.isim    = input("isim    : ")
        user.soyisim = input("soyisim : ")
        user.numara  = input("numara  : ")
        return user

    def Run(self):
        self.Main_Page()
        self.Goto_Choice()

if __name__ == "__main__":
    n = ConsoleProgram()
    n.Run()
