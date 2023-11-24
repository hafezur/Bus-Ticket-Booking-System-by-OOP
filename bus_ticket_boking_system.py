# bus ticket booking system:
 

# Admin
""" 
1. add a new bus
2. check available buses
3. can check bus info

"""

# User
""" 
1.check available buses
2.can check bus info
3.can reserve seat

"""

class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_add,to_add) -> None:
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.departure=departure
        self.from_add=from_add
        self.to_add=to_add
        self.seat=["Empty" for i in range(20)]

""" check=Bus(2,'kalo',8.30,7.00,'nator','mohammadpur')
print(vars(check)) """

class Hafiz:
    total_bus=5
    total_bus_list=[]

    
    def add_bus(self):
        bus_no=int(input('Enter Bus No: '))
        flag=1
        for w in self.total_bus_list:
            if bus_no ==w['coach']:
                print('The bus already added')
                flag=0
                break
        
        if flag:
            bus_driver=input("Enter Bus Driver Name")
            bus_arrival=input('Enter bus arrival time')
            bus_departure=input('Enter Bus Departure Time')
            bus_from=input("Enter Bus Start From")
            bus_to=input("Enter Bus Destination")
            self.new_bus=Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_list.append(vars(self.new_bus))# vars is used to convert dictionary that means to create key --> value pair 
            print("\n Bus Added Successfully")

""" first_add=Hafiz()
first_add.add_bus() """

class Counter(Hafiz):
    user_list=[]
    def reservation(self):
        bus_no=int(input('Enter Bus No: '))
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                passenger_name=input('Enter your name ')
                seat_no=int(input("Enter seat No: "))

                if seat_no>20:
                    print('No seats Available')
                elif w['seat'][seat_no-1]!='Empty':
                    print("Seat already Booked")
                else:
                    w["seat"][seat_no-1]=passenger_name
            else:
                print('No bus Available')
        """ for bus in self.total_bus_list:
            print(bus['seat']) """
    
    def show_ticket(self):
        bus_no=int(input("Enter Bus Number: "))

        for w in self.total_bus_list:
            if bus_no ==w['coach']:
                print('*'*50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number : {bus_no}\t\t\t Driver:{w['driver']}")
                print(f"Arrival : {w['arrival']} \t\t\t Departure Time : {w['departure']} \n From \t{w['from_add']}\t\t\t To:\t{w['to_add']}")
                print()

                a=1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}.{w['seat'][a-1]}",end="\t")
                        a+=1
                    for j in range(2):
                        print(f"{a}.{w['seat'][a-1]}",end="\t")
                        a+=1
                    print()
                print('*'*50)
    
    def get_user(self):
        return self.user_list
    
    def create_account(self):
        name=input("Enter Your Username: ")
        password=input("Enter Your Password: ")
        self.new_user=User(name,password)
        self.user_list.append(vars(self.new_user))
    
    def available_buses(self):
        if len(self.total_bus_list)==0:
            print("No buses are Available\n")
        else:
            print('*'*50)
            for bus in self.total_bus_list:
                print()
                print(f"{' '*10}{'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(f"Bus Number: {bus['coach']} \t Driver: {bus['driver']}")
                print(f"Arrival : {bus['arrival']}\t Departure Time: {bus['departure']}\n from:\t{bus['from_add']} \t\t To_add:\t{bus['to_add']}")
                print('*'*50)
                    
while True:
    company=Hafiz()
    b=Counter()
    print("1. Create an account \n2. login to your account \n3.Exit")

    user_input=int(input("Enter your Choice: "))
    if user_input==3:
        break
    elif user_input==1:
        b.create_account()
    elif user_input==2:
        name=input("Enter Your Username : ")
        password=input("Enter Your Password : ")
        flag=0
        isAdmin=False

        if name=='admin' and password=='123':
            isAdmin=True
        if isAdmin==False:
            for user in b.get_user():
                if user['username']==name and user['password']==password:
                    flag=1
                    break
            if flag:
                while True:
                    print(f"\n{''*10}Welcome to Bus Ticket Boking System ")
                    print("1.Available Buses \n 2.Show Bus Info \n 3.Reservation\n 4.Exit")
                    a=int(input("Enter Your Choice : "))
                    if a==4:
                        break
                    elif a==1:
                        b.available_buses()
                    elif a==2:
                        b.show_ticket()
                    elif a==3:
                        b.reservation()
            else:
                print("No Username Found")
        else:
            while True:
                print(f"\n{''*10} Hello ADMIN welcome to bus ticket booking system")
                print("1.Add Bus \n 2.Available Buses \n3>Show Bus Info \n 4.EXIT")
                a=int(input("Enter Your Choice: "))
                if a==4:
                    break
                elif a==1:
                    b.add_bus()
                elif a==2:
                    b.available_buses()
                elif a==3:
                    b.show_ticket()
                
""" compani=Hafiz()
compani.add_bus()

cout=Counter()
cout.reservation() """