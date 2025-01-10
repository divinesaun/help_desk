import re

text_file_path = "case.txt"

class Complaint:
    
    @staticmethod
    def create_info():
        
        with open(text_file_path, 'r') as f:
            reading = f.read()

        data = []
        count = len(reading.split("\n\n")[:-1])

        for i in range(count):
            data.append(reading.split("\n\n")[i].split("\n"))
        
        
        ticket_no = 1
        
        for i in data:
            while str(ticket_no) in i[0][11:]:
                ticket_no += 1
                
        comp_name = input("Enter the complainant's name: ")
                
        while True:
            email = input("Enter the complainant's email: ")
            if (re.search("[a-zA-Z0-9]+@[a-zA-Z]+.(com|uz)", email)):
                break
            else:
                print("Please Enter An Appropriate Email Address")
        while True:
            date = input("Enter the date (DD-MM-YY): ")
            if (re.search("[0-9]+[-]+[0-9]+[-]+[0-9]", date)):
                break
            else:
                print("Please Enter The Date As Instructed")
        while True:
            status = input("Enter the status of the complaint: ")
            if (status.lower() == "high") | (status.lower() == "medium") | (status.lower() == "low"):
                break
            else:
                print("Please Enter Appropriate Info (High) or (Medium) or (Low)")
        details = input("Enter the complaint details: ")
        
        print("\nThe complaint has been created successfully")

        with open(text_file_path, "a+") as f:
            f.write(f"Ticket No: {str(ticket_no)}\nComplainant's Name: {comp_name}\nEmail: {email}\nDate: {date}\nStatus: {status.capitalize()}\nDetails: {details}\n\n")
            
    @staticmethod       
    def view_info():
        with open(text_file_path, 'r') as f:
                        reading = f.read()

        data = []
        count = len(reading.split("\n\n")[:-1])

        for i in range(count):
            data.append(reading.split("\n\n")[i].split("\n"))

        new_list = []
        for i in data:
            if i[4][8:].lower() == "high":
                new_list.append(i)
        for i in data:
            if i[4][8:].lower() == "medium":
                new_list.append(i)
        for i in data:
            if i[4][8:].lower() == "low":
                new_list.append(i)
        for i in data:
            if i[4][8:].lower() == "pending":
                new_list.append(i)
        for i in data:
            if i[4][8:].lower() == "solved":
                new_list.append(i)

        with open(text_file_path, 'w') as f:
            for i in new_list:
                written = f.write("\n".join(i) + "\n\n")

        with open(text_file_path, 'r+') as f:
            print("\n" + f.read()[:-2])    
            
    @staticmethod        
    def search_info():
        with open(text_file_path, 'r') as f:
                reading = f.read()

        found = False  # Comes in handy when printing the "item not found message". Check the if-statement later on
        search_key = input("What are you looking for: ").lower()  # user input that is compared with info in-hand/file
        data = []
        count = len(reading.split("\n\n")[:-1])

        for i in range(count):
            data.append(reading.split("\n\n")[i].split("\n"))

        print("\nSearch Results: ")

        for i in range(count):
            a = search_key in data[i][0][11:].lower()
            b = search_key in data[i][1][20:].lower()
            c = search_key in data[i][2][7:].lower()
            d = search_key in data[i][3][6:].lower()
            e = search_key in data[i][4][8:].lower()
            f = search_key in data[i][5][9:].lower()
            if a | b | c | d | e | f:
                print("-----------------------------------------------------------------------------------------------")
                #print(f"{data[i][0][11:]} | {data[i][1][20:]} | {data[i][2][7:]}| {data[i][3][6:]} | {data[i][4][8:]}| {data[i][5][9:]}\n")
                print(f"Ticket No: {data[i][0][11:]}\nComplainant's Name: {data[i][1][20:]}\nEmail: {data[i][2][7:]}\nDate : {data[i][3][6:]}\nStatus: {data[i][4][8:]}\nDetails: {data[i][5][9:]}\n")
                found = True
        if not found:
            print("-----------------------------------------------------------------------------------------------")
            print("Sorry, we could not find an item that matches your description")

        data = []
        
    @staticmethod   
    def update_info():
        with open(text_file_path, 'r') as f:
                    reading = f.read()

        data = []
        count = len(reading.split("\n\n")[:-1])

        for i in range(count):
            data.append(reading.split("\n\n")[i].split("\n"))

        id_val = input("Enter the Ticket Number of the complaint you want to update status of: ")

        for i in data:
            if i[0][11:] == id_val:
                print(f"The current status is: {i[4][8:]}")
                while True:
                    new_status = input("Enter the new status: ").lower()
                    if (new_status == "high")|(new_status == "medium")|(new_status == "low")|(new_status == "pending")|(new_status == "solved"):
                        i[4] = "Status: " + new_status.capitalize()
                        break
                    else:
                        print("Please Enter Valid Status e.g high, medium, low, pending, solved")

        print("\nThe update was successful")


        with open(text_file_path, 'w') as f:
            for i in data:
                written = f.write("\n".join(i) + "\n\n")
        data = []
        
    @staticmethod   
    def delete_info():
        with open(text_file_path, 'r') as f:
                    reading = f.read()

        data = []
        count = len(reading.split("\n\n")[:-1])

        for i in range(count):
            data.append(reading.split("\n\n")[i].split("\n"))


        id_val = input("Enter the Ticket number of the complaint you want to delete: ")
        new_list = []
        for i in data:
            if i[0][11:] != id_val:
                new_list.append(i)

        print("\nThe item has been successfully deleted")

        with open(text_file_path, 'w') as f:
            for i in new_list:
                written = f.write("\n".join(i) + "\n\n")
                
                

#


# In[ ]:




