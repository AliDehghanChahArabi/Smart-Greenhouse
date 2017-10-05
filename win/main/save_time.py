from datetime import datetime


class Save_Time():
    def __init__ (self, name_page, time = str(datetime.now())):
        self.name_page = name_page
        self.time = time
    def ST(self):
        with open("../Data/time_run_app.txt", "r") as file:
            old_data = str(file.read())
            file.close()
        with open("../Data/time_run_app.txt", "w") as file:
            new_data = str(self.name_page + " --> " +self.time)
            file.write (old_data + "\n" + new_data)

if __name__ == "__main__":
    save = Save_Time("ali")
    save.ST()
