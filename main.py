import mysql.connector as sq
import sys
import math
import random

doctor_name = ""
pat_name = ""
bill_no = None
room_charges = None
room_type = ""
room_no = None


def connection():
    try:
        con = sq.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital_management_system"
        )

        if con.is_connected() == False:
            print("database not connected")
        else:
            return con

    except sq.Error as er:
        print(er)


def doctor_display():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from doctors")

        for i in cur.fetchall():
            print(i)

    except sq.Error as er:
        print(er)


def patient_information():
    try:
        global pat_name
        global doctor_name

        con = connection()
        cur = con.cursor()

        pat_name = input("Enter name of the patient: ")
        age = int(input("enter age of patient: "))
        gender = input("enter gender of patient: ")
        address = input("enter address of patient: ")
        contact_no = input("enter contact number of patient: ")
        date_of_consultancy = input(
            "enter date of consultancy of appointment: "
        )
        doctor_name = input(
            "enter the name of the doctor you want to consult? "
        )

        f = doctor_name

        cur.execute(
            "insert into patients "
            "values('{}',{},'{}','{}','{}','{}','{}')"
            .format(
                pat_name,
                age,
                gender,
                address,
                contact_no,
                date_of_consultancy,
                doctor_name
            )
        )

        print()
        return doctor_name

        con.commit()

    except sq.Error as er:
        print(er)


# room details
def room_information():
    try:
        con = connection()
        cur = con.cursor()

        cur.execute(
            "select * from room_info where room_status like "
            "'{}'".format('Not Booked')
        )

        for i in cur.fetchall():
            print(i)

    except sq.Error as er:
        print(er)


def room_choice():
    con = connection()
    cur = con.cursor()

    global room_charges
    global room_type
    global room_no

    number_days = int(
        input("enter the number of days you will be needing the room for? ")
    )

    room_type = input("enter the room type you want to avail? ")
    room_no = int(input("enter the room number: "))

    cur.execute(
        "select room_charges_per_day from room_info where "
        "room_type='{}'".format(room_type)
    )

    z = cur.fetchone()
    pay = z[0]

    room_charges = pay * number_days


def bill_1():
    global pat_name
    global doctor_name
    global bill_no

    a = random.randint(2010, 2200)
    b = random.randint(1600, 2500)

    con = connection()
    cur = con.cursor()

    bill_no = a
    pathology_fees = b

    x = str(b)

    cur.execute(
        "select fees from doctors where "
        "doctor_name='{}'".format(doctor_name)
    )

    r = cur.fetchone()
    doctor_fees = r[0]

    m = str(doctor_fees)
    total_amount = int(x) + int(m)

    cur.execute(
        "insert into bill_details_2 "
        "values({},'{}',{},'{}',{},{})"
        .format(
            bill_no,
            pat_name,
            pathology_fees,
            doctor_name,
            doctor_fees,
            total_amount
        )
    )

    print()
    con.commit()

    print("bill calculated successfully")


def dis_bill_1():
    try:
        global pat_name

        con = connection()
        cur = con.cursor()

        cur.execute(
            "select * from bill_details_2 where "
            "pat_name='{}'".format(pat_name)
        )

        print()

        for i in cur.fetchall():
            print(i)
            print(" PRIYAMVADA EYE HOSPITAL BILL")
            print("Date: 2022-12-12")
            print("BILL NUMBER:", i[0])
            print("PATIENT NAME:", i[1])
            print("HOSPITAL CHARGES:")
            print("PATHOLOGY FEES:", i[2])
            print(" DOCTOR AND FEES DETAILS:")
            print("DOCTOR NAME:", i[3])
            print("DOCTOR FEES:", i[4])
            print(" TOTAL BILL AMOUNT:")
            print("TOTAL AMOUNT TO BE PAID:", i[5])

    except sq.Error as er:
        print(er)


# bill with room bookings
def bill_2():
    try:
        con = connection()
        cur = con.cursor()

        global pat_name
        global doctor_name
        global bill_no
        global room_charges
        global room_type

        r = str(room_charges)

        bill_no = random.randint(1200, 1740)
        pathology_fees = random.randint(1500, 9800)

        p = str(pathology_fees)

        cur.execute(
            "select fees from doctors where "
            "doctor_name='{}'".format(doctor_name)
        )

        n = cur.fetchone()
        doctor_fees = n[0]

        d = str(doctor_fees)
        total_amount = int(d) + int(r) + int(p)

        cur.execute(
            "insert into bill_details_3 "
            "values({},'{}',{},'{}',{},'{}',{},{})"
            .format(
                bill_no,
                pat_name,
                pathology_fees,
                doctor_name,
                doctor_fees,
                room_type,
                room_charges,
                total_amount
            )
        )

        con.commit()

        print(
            "Thank you for coming to our hospital."
            "Hope you have a speedy recovery!"
        )

    except sq.Error as er:
        print(er)


def bill_3():
    try:
        global pat_name

        con = connection()
        cur = con.cursor()

        pat_name = input("Enter name of patient:")
        doctor_name = input("Enter doctor's name:")
        room_type = input("Enter room type:")
        room_no = int(input("enter the room number: "))

        number_days = int(
            input(
                "enter the number of days you will be "
                "needing the room for? "
            )
        )

        cur.execute(
            "select room_charges_per_day from room_info "
            "where room_type='{}'".format(room_type)
        )

        z = cur.fetchone()
        pay = z[0]

        room_charges = pay * number_days
        r = str(room_charges)

        bill_no = random.randint(1200, 1740)
        pathology_fees = random.randint(1500, 9800)
        p = str(pathology_fees)

        cur.execute(
            "select fees from doctors where "
            "doctor_name='{}'".format(doctor_name)
        )

        n = cur.fetchone()
        doctor_fees = n[0]

        d = str(doctor_fees)
        total_amount = int(d) + int(r) + int(p)

        cur.execute(
            "insert into bill_details_1 "
            "values({},'{}',{},'{}',{},'{}',{},{})"
            .format(
                bill_no,
                pat_name,
                pathology_fees,
                doctor_name,
                doctor_fees,
                room_type,
                room_charges,
                total_amount
            )
        )

        con.commit()

        print(
            "Thank you for coming to our hospital."
            "Hope you have a speedy recovery!"
        )

    except sq.Error as er:
        print(er)


def bill_display2():
    try:
        global pat_name

        con = connection()
        cur = con.cursor()

        cur.execute(
            "select * from bill_details_1 where "
            "pat_name='{}'".format(pat_name)
        )

        for i in cur.fetchall():
            print(" PRIYAMVADA EYE HOSPITAL BILL")
            print("Date: 2022-12-12")
            print("BILL NUMBER:", i[0])
            print("PATIENT NAME:", i[1])
            print("HOSPITAL CHARGES:")
            print("PATHOLOGY FEES:", i[2])
            print(" DOCTOR AND FEES DETAILS:")
            print("DOCTOR NAME:", i[3])
            print("DOCTOR FEES:", i[4])
            print(" ROOM AND REQUIREMENTS:")
            print("ROOM TYPE AVAILED:", i[5])
            print("TOTAL ROOM CHARGES:", i[6])
            print(" TOTAL BILL AMOUNT:")
            print("TOTAL AMOUNT TO BE PAID:", i[7])

    except sq.Error as er:
        print(er)


def bill_display():
    try:
        global pat_name

        con = connection()
        cur = con.cursor()

        cur.execute(
            "select * from bill_details_3 where "
            "pat_name='{}'".format(pat_name)
        )

        for i in cur.fetchall():
            print(" PRIYAMVADA EYE HOSPITAL BILL")
            print("Date: 2022-12-12")
            print("BILL NUMBER:", i[0])
            print("PATIENT NAME:", i[1])
            print("HOSPITAL CHARGES:")
            print("PATHOLOGY FEES:", i[2])
            print(" DOCTOR AND FEES DETAILS:")
            print("DOCTOR NAME:", i[3])
            print("DOCTOR FEES:", i[4])
            print(" ROOM AND REQUIREMENTS:")
            print("ROOM TYPE AVAILED:", i[5])
            print("TOTAL ROOM CHARGES:", i[6])
            print(" TOTAL BILL AMOUNT:")
            print("TOTAL AMOUNT TO BE PAID:", i[7])

    except sq.Error as er:
        print(er)


ans = 'y'

# main program after all functions
while ans == 'y':
    con = connection()
    # cur = con.cursor()

    global a

    print(" PRIYAMVADA EYE HOSPITAL")
    print()

    # doctor_details()

    login_id = 'hospital'
    password = 'helloworld'

    s = input("enter your login id: ")

    if s == login_id:
        u = input("enter your password: ")

        if u == password:
            print(" WELCOME TO THE RECEPTION! ")
            print("1. Make an appointment")
            print("2. Book a room for surgery")

            ch = int(input("enter your choice: "))

            if ch == 1:
                print(" the list of doctors are: ")
                print()

                doctor_display()

                q1 = input("do you have a room requirement? ")

                if q1 == 'yes':
                    patient_information()
                    room_information()
                    room_choice()
                    bill_2()
                    bill_display()

                elif q1 == 'no':
                    patient_information()
                    bill_1()
                    dis_bill_1()

            elif ch == 2:
                doctor_display()
                room_information()
                bill_3()
                bill_display2()