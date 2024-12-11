import csv
names = []
phone_numbers = []
emails = []
addresses = []
contacts = []
num = 999

def add_contact():
    print("*****ADD CONTACT*****")
    for i in range(num):
        name = input("Name: ")
        while True:
            phone_number = input('Phone number: ')
            if phone_number.isdigit():
                phone_number = int(phone_number)
                break
            else:
                print("Please Enter valid phone number!")
        email = input("Email: ")
        address = input("Address: ")

        names.append(name)
        phone_numbers.append(phone_number)
        emails.append(email)
        addresses.append(address)

        print(f"{'Serial No.':<10}{'Name':<25}{'Phone Number':<15}{'Email':<30}{'Address':<30}")
        print("*" * 100)
        for i in range(len(names)):
            print(f"{i + 1:<10}{names[i]:<25}{phone_numbers[i]:<15}{emails[i]:<30}{addresses[i]:<30}")
        break

def save_contact():
    with open('contacts.csv', 'w', newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['Serial No.','Name', 'Phone Number', 'Email', 'Address'])
        for i in range(len(names)):
            writer.writerow([i + 1,names[i], phone_numbers[i], emails[i], addresses[i]])
    print("Contacts are added!")

def view_contact():
    print("*****VIEW CONTACTS*****")
    try:
        with open ('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            contacts = list(reader)
            if len(contacts) <= 1:
                print("No contacts found. Please add contacts first!")
                print("*" * 150)
                main()
            print(f"{'Serial No.':<15}{'Name':<25}{'Phone Number':<15}{'Email':<30}{'Address':<30}")
            print("*" * 100)
            for row in contacts[1:]:
                print(f"{row[0]:<15}{row[1]:<25}{row[2]:<15}{row[3]:<30}{row[4]:<30}")
    except FileNotFoundError:
        print("No contacts found. Please add some contacts first.")

def search_contact():
    print("*****SEARCH CONTACT*****")
    with open ('contacts.csv','r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        if len(contacts) <= 1:
            print("No contacts available to search")
            print('*' * 150)
            main()
    keyword = input("Enter keyword to search(Name, Phone number, Email, Address): ").strip().lower()
    print(f"{'Serial No.':<10}{'Name':<25}{'Phone Number':<15}{'Email':<30}{'Address':<30}")
    print("*" * 100)
    for row in contacts[1:]:  # Skip the header row
        if any(keyword in str(cell).lower() for cell in row):
            print(f"{row[0]:<10}{row[1]:<25}{row[2]:<15}{row[3]:<30}{row[4]:<30}")

def update_contact():
    print("*****UPDATE CONTACT*****")
    with open ('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        if len(contacts) <= 1:
            print("No contacts available to update")
            print('*' * 150)
            main()
        print(f"{'Serial No.':<10}{'Name':<25}{'Phone Number':<15}{'Email':<30}{'Address':<30}")
        print("*" * 100)
        for row in contacts[1:]:
            print(f"{row[0]:<10}{row[1]:<25}{row[2]:<15}{row[3]:<30}{row[4]:<30}")
        index = input("Enter Serial No. of the contact to update: ").strip()
        flag = False
        for row in contacts[1:]:
            if row[0] == index:
                name = input("Enter new name(or press Enter to keep current): ").strip() or row[1]
                phone_number = input("Enter new phone number(or press Enter to keep current):  ").strip() or row[2]
                email = input("Enter new email(or press Enter to keep current): ").strip() or row[3]
                address = input("Enter new Address(or press Enter to keep current): ").strip() or row[4]
                row[1], row[2], row[3], row[4] = name, phone_number, email, address
                print("Contact updated successfully!")
                flag = True
                break
        if not flag:
            print("Invalid Serial No. Please Try Again")
            return
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)  
        print("Contacts file updated successfully!")

def delete_contact():
    print("*****DELETE CONTACT*****")
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        if len(contacts) <= 1: 
            print("No contacts to delete.")
            print('*' * 150)
            main()
        print(f"{'Serial No.':<10}{'Name':<25}{'Phone Number':<15}{'Email':<30}{'Address':<30}")
        print("*" * 100)
        for row in contacts[1:]: 
            print(f"{row[0]:<10}{row[1]:<25}{row[2]:<15}{row[3]:<30}{row[4]:<30}")
        index = input("Enter the Serial No. of the contact you want to delete: ").strip()
        for i, row in enumerate(contacts[1:], start=1):
            if row[0] == index:
                confirm = input(f"Contact '{row[1]}' will be deleted. Are you sure? (Y/N): ").strip().lower()
                if confirm == 'y':
                    contacts.pop(i)
                    print("Contact deleted successfully!")
                    break
                else:
                    print("Deletion canceled.")
                    return
        else:
            print("Invalid Serial No. Please try again.")
            return
        for i, row in enumerate(contacts[1:], start=1): 
            row[0] = str(i)
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
        print("Contacts file updated successfully!")

def main():               
    print("**CONTACT BOOK**")
    for i in range(10):
        print('*')
    print("1. ADD CONTACT \n2. VIEW CONTACT LIST \n3. SEARCH CONTACT \n4. UPDATE CONTACT \n5. DELETE CONTACT \n6. Exit")
    a = int(input("Choose to perform: "))

    if a not in range(1,7):
        a = input("Enter valid choice: ")
    #Add Contact
    if a == 1:
        while True:
            add_contact()

            another_contact=input("Do you want to add another contact?(Y/N): ").strip().lower()
            if another_contact != 'y':
                save_contact()
                main()

    #View Contact
    if a == 2:
        while True:
            view_contact()
            main()

    #Search Contact
    if a == 3:
        while True:
            search_contact()

            search_again = input("Do you want to search again?(Y/N): ").strip().lower()
            if search_again != 'y':
                main()

    #Update Contact
    if a == 4:
        while True:
            update_contact()

            update_again = input("Do you want to update another contact?(Y/N): ").strip().lower()
            if update_again != 'y':
                main()

    #Delete Contact
    if a == 5:
        while True:
            delete_contact()

            delete_again = input("Do you want to Delete another contact?(Y/N): ").strip().lower()
            if delete_again != 'y':
                main()

    #Exit
    if a == 6:
        exit()

main()