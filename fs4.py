import datetime
import os
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def load_data():
    try:
        with open('doctors.txt', 'r') as file:
            data = file.readlines()
            data = [line.strip().split(',') for line in data]
    except FileNotFoundError:
        data = []
    return data

def save_data(data):
    with open('doctors.txt', 'w') as file:
        for entry in data:
            line = ','.join(entry)
            file.write(line + '\n')

def admin_login():
    admin_username = input("Admin Username: ")
    admin_password = input("Admin Password: ")

   
    if admin_username == 'admin' and admin_password == 'password':
        return True
    else:
        return False

def doctor_login():
    doctor_username = input("Doctor Username: ")
    doctor_password = input("Doctor Password: ")


    try:
        with open('doctors.txt', 'r') as file:
            data = file.readlines()
            for line in data:
                line = line.strip().split(',')
                if line[0] == doctor_username and line[2] == doctor_password:
                    return True
    except FileNotFoundError:
        pass

    return False

def add_doctor():
    doctor_name = input("Doctor Name: ")
    doctor_specialization = input("Doctor Specialization: ")
    doctor_password = input("Doctor Password: ")


    data = load_data()

    
    for entry in data:
        if entry[0] == doctor_name:
            print("Doctor already exists.")
            return

    
    data.append([doctor_name, doctor_specialization, doctor_password])

   
    save_data(data)

    print("Doctor added successfully!")

def remove_doctor():
    doctor_name = input("Doctor Name: ")

    
    data = load_data()

    
    removed = False
    for entry in data:
        if entry[0] == doctor_name:
            data.remove(entry)
            removed = True
            break

    
    save_data(data)

    if removed:
        print("Doctor removed successfully!")
    else:
        print("Doctor not found!")



def view_doctor():
    #
    with open('doctors.txt', 'r') as file:
            data = file.readlines()
            if data:
                print("Doctor Details:")
                for _ in range(36):
                    print("*", end="")
                print("\n")
                print("{:<20} {:<20}".format("Name", "Specialization"))
                for _ in range(36):
                    print("*", end="")
                print("\n")
                for line in data:
                    doctor = line.strip().split(',')
                    name = doctor[0]
                    specialization = doctor[1]
                    print("{:<20} {:<20}".format(name, specialization))
                for _ in range(36):
                    print("*", end="")
            else:
                print("No doctors found.")

    

def main():
    while True:
        print("--- Login ---")
        print("1. Admin Login")
        print("2. Doctor Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            if admin_login():
                print("Admin login successful.")
                while True:
                    print("\n--- Admin Menu ---")
                    print("1. Add Doctor")
                    print("2. Remove Doctor")
                    print("3. View Doctor")
                    print("4. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == '1':
                        add_doctor()
                    elif admin_choice == '2':
                        remove_doctor()
                    elif admin_choice == '3':
                        view_doctor()
                    elif admin_choice == '4':
                        break
                    else:
                        print("Invalid choice. Try again.")
            else:
                print("Admin login failed.")

        elif choice == '2':
            if doctor_login():
                print("Doctor login successful.")


                info_li = []
                treatment_li = []
                medicines = []
                foods_to_eat = []

                ans=True

                def Add():

                    print("           ~~~~~~~~ FAITH HOSPITAL ~~~~~~~~            ")

                    td = datetime.date.today()

                    name = input("Name : ")          

                    file = open("{}.txt".format(name),'w') 

                    age = input("Age : ")
                    weight = input("Weight : ")
                    address = input("Address : ")
                    phone = input("Mobile : ")
                    sex = input("Sex : ")
                    illness = input("Illness in Breif : ")
                    medical_history = input("Medical History : ")

                    treatment_explain = input("Describe about treatment and illness : ")
                    treatment_li.append(treatment_explain)

                    info_li.extend((name, age,sex,weight,address,illness,medical_history,phone,td) )

                    while True:
                        medicine = input("Enter name of Medicines Given : ")
                        if medicine == "/":
                            break
                        else:
                            medicines.append(medicine)

                    while True:
                        foods = input("Enter name of foods to eat most : ")
                        if foods == "/":
                            break
                        else:
                            foods_to_eat.append(foods)


                    noteli = []
                    note = input("Give Special Note : ")
                    noteli.append(note)

                #************************** Prescription Format *******************************************

                    file.write(("                  FAITH HOSPITAL          \n"
                                "Phone : +91 987655432           Email : faith@hospital.com\n"
                                "__________________________________________________________\n"
                                "                   Patient Details             \n"
                                "       Name : {}      Age : {}     Sex : {}    \n"         
                                "       Weight : {}        Address : {}\n"
                                "       Phone : {}          Date : {}\n"  
                                "       Illness : {}     Medical History : {}\n"
                                "__________________________________________________________\n"
                                "About illness : {} \n"
                                "\n"
                                "Medicines Given :\n"

                                ).format(info_li[0],info_li[1],info_li[2],info_li[3],info_li[4],info_li[7],info_li[8],info_li[5],info_li[6],treatment_li[0]))


                    for i in range(0,len(medicines)):
                        file.write(("- {} \n").format(medicines[i]))


                    file.write((  "\n" "Foods to Eat : \n"))


                    for i in range(0,len(foods_to_eat)):
                        file.write(("- {} \n".format(foods_to_eat[i])))

                    file.write(("\n Note : {} \n").format(noteli[0]))

                    file.write(("            ~~~~ Get Well Soon ~~~~            "))
                    info_li.clear()
                    treatment_li.clear()
                    medicines.clear()
                    foods_to_eat.clear()
                    noteli.clear()

                def view():

                    try:

                        file_names = input("Enter the patient name: ")
                        file_name=file_names+".txt"
                
                        if os.path.isfile(file_name):
                    
                            file = open(file_name, 'r')

                        
                            contents = file.read()

                    
                            print("File contents:")
                            print(contents)

                        
                            file.close()
                        else:
                            print("File not found.")

                    except PermissionError:
                        print("Permission denied. Unable to open the file.")

                    except Exception as e:
                        print("An error occurred:", str(e))

                def delete():
                    file_nam = input("Enter the patient name: ")
                    file_nams=file_nam+".txt"
                
                    if os.path.isfile(file_nams):
                        os.remove(file_nams)
                
                
                        print("Prescription deleted !") 
                
                    else:
                        print("Prescription doesnot exist !") 

                def send_email():
                    sender_email = 'varunrajmdb@gmail.com'
                    sender_password = 'awcqsijugagopden'
                    receiver_email = input("Enter the patient email address:")
                    fileepath=input("Enter the patient name:")
                    file_path = fileepath+".txt"
                    subject = 'Prescription'
                    message = 'Thank you Visiting, the below is your prescription. Hope you have a good life.'
                
                    
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = receiver_email
                    msg['Subject'] = subject

                
                    msg.attach(MIMEText(message, 'plain'))

                    
                    attachment = open(file_path, 'rb')
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{file_path}"')
                    msg.attach(part)

                    
                    server = smtplib.SMTP('smtp.gmail.com', 587)  
                    server.starttls()

                    try:
                    
                        server.login(sender_email, sender_password)

                    
                        server.sendmail(sender_email, receiver_email, msg.as_string())
                        print("Email sent successfully!")
                    except Exception as e:
                        print(f"An error occurred while sending the email: {str(e)}")
                    finally:
                    
                        server.quit()
                
                def modify():
                    names=input("Enter the name of the patient to modify")
                    namer=names+".txt"
                    if os.path.isfile(namer):
                        os.remove(namer)
                        Add()
                        print("Prescription Modified successfully") 
                
                    else:
                        print("Prescription doesnot exist !") 




                while ans:
                    print ("""
                    1.Add Prescription
                    2.view prescription
                    3.delete prescription
                    4.modify prescription
                    5.send prescription
                    6.exit
                    """)
                    ans=input("What would you like to do? ") 
                    if ans=="1": 
                        Add()
                        print("\n Prescription added") 
                    elif ans=="2":
                        view()
                    elif ans=="3":
                        delete()
                    elif ans=="4":
                        modify()
                    elif ans=="5":
                        send_email()
                    elif ans=="6":
                        break
                    elif ans !="":
                        print("\n Not Valid Choice Try again") 

  
            else:
                print("Doctor login failed.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
