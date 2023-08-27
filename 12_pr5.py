'''
1 2 3 4 5 6 7 8 9 10
'''
class Train:
    def __init__(self, name, fare, seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print("*********")
        print(f"The name of the train are {self.seats}")
        print(f"The seats available in the train are{self.seats}")
        print(f"************")

    def fearInfo(self):
        print(f"The price of ticket is:Rs{self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry this train is ful Try in tatkal")

        def cancelTicket(self,seatNo):
            pass

intercity=Train("Intarcity express:14015",90,2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()