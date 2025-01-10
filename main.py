from complaint import Complaint

while True:
    choose = int(input("\nSelect Option\n(1) View Complaint List\
                       \n(2) Search for complaint\n(3) Add New Complaint\
                       \n(4) Update Complaint Status\n(5) Delete A Complaint\n(0) Exit\n\nEnter Selection: "))
    if choose == 0:
        print("Goodbye!")
        break
    elif choose == 1:
        Complaint.view_info()
    elif choose == 2:
        Complaint.search_info()
    elif choose == 3:
        Complaint.create_info()
    elif choose == 4:
        Complaint.update_info()
    elif choose == 5:
        Complaint.delete_info()
    else:
        print("\nInvalid Input!")