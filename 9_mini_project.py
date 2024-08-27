import datetime
bookings={}
total_cars=10
code=1
def help():
    help_text = """
        booking : Make a booking
        display : Show all booking
        search : Search booking
        cancle : Cancle booking
        details : Show details of the project
        exit : exit\n"""
    print(help_text)

def validate_date(input_date):
    count1=input_date.count("-")
    if len(input_date) != 10 or input_date[4] != "-" or input_date[7] !="-" or count1 != 2:
        return False,"Invalid Format (YYYY-MM-DD)"
    parts=input_date.split("-")

    if not(parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        return False,"Please Enter Numbers"
    
    year,month,day= list(map(int,parts))
    if year < 1 or not(1<= month <= 12) or not (1<= day <=31):
        return False,"Invalid Date"
    return True,"Valid Date"

def find_days(start_date, end_date):
    if start_date == end_date:
        return 0
    else:
        new_start_date = start_date + datetime.timedelta(days=1)
        return 1 + find_days(new_start_date, end_date)

def booking():
    global total_cars,code
    if len(bookings) >= total_cars:
        print("All cars are booked!")
        return
    name=input("Enter Your name: ")
    start_date=input("Enter Start Date: ")
    end_date=input("Enter End Date: ")
    is_valid,msg=validate_date(start_date)
    if not is_valid:
        print(msg)
        return
    
    is_valid,msg=validate_date(end_date)
    if not is_valid:
        print(msg)
        return
    
    start_date= datetime.datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date= datetime.datetime.strptime(end_date,"%Y-%m-%d").date()
    count_days = end_date - start_date
    count_days = count_days.days
    res = find_days(start_date, end_date)
    print(res, count_days)

    if start_date > end_date:
        print("Error!")
        return
    new_booking={
        "name": name,
        "start_date":start_date,
        "end_date": end_date,
        "days" : count_days
    }
    bookings[code]=new_booking
    code+=1
    print("Done!")

def cancle(code_del):
    if code_del in bookings:
        bookings.pop(code_del)
        print("Cancelled")
    else:
        print("Not Found!")

    

def display():
    if len(bookings) !=0:
        for code,booking in bookings.items():
            print(5*"*" + str(code) + 5*"*")
            print(f"name:{booking['name']}")
            print(f"start date:{booking['start_date']}")
            print(f"end date:{booking['end_date']}")
            print(f"days : {booking['days']}")
    else:
        print("Empty!")
    
def search_by_name(name):
    found = False
    for code,booking in bookings.items():
        if booking["name"]==name:
            print(5*"*" + str(code) + 5*"*")
            print(f"name:{booking['name']}")
            print(f"start date:{booking['start_date']}")
            print(f"end date:{booking['end_date']}")
            print(f"days : {booking['days']}")
            found = True
        if not found:
            print(f"{name} Not Found!")
            


def search_by_code(code_s):
    if code_s in bookings:
        booking=bookings[code_s]
        print(5*"*" + str(code_s) + 5 * "*")
        print(f"name : {booking['name']}")
        print(f"start date : {booking['start_date']}")
        print(f"end date : {booking['end_date']}")
        print(f"days : {booking['days']}")
    else:
        print("Not Found")

def search():
    cmd=input("Search by 'name' or 'code' : ")
    if cmd == "name":
        name= input("Name for search: ")
        search_by_name(name)
    elif cmd == "code":
        code_s=int(input("code for search:"))
        search_by_code(code_s)
    else:
        print("Not Found!!!!!!!!!!!!!!!")

def details():
    num_booked_cars= len(bookings)
    num_available_cars=total_cars-num_booked_cars
    print(f"Total Number of Cars:{total_cars}")
    print(f"Number of booked cars: {num_booked_cars}")
    print(f"Number of available cars: {num_available_cars}")

while True:
    command=input("Insert Your Option: ")
    if command == "help":
        help()
    elif command == "booking":
        booking()
    elif command=="search":
        search()
    elif command=="display":
        display()
    elif command== "cancle":
        code_del=int(input("Insert your code: "))
        cancle(code_del)
    elif command == "details":
        details()
    elif command == "exit":
        break
    elif command == "":
        continue
    else:
        print(f"{command} Not Found!")
