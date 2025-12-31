class train():
    def book(self , trainNo=1234, from_station="A", to_station="B"):
        print(f"Welcome to Indian Railway")
        print(f"Ticket is booked in train no: {trainNo} from {from_station} to {to_station} ")

    def getstatus(Dhruv, trainNo):
        print(f"train no. {trainNo} is on time and will reach station B at 10:00 AM")

    def getfare(Dhruv , Trainno, from_station , to_station):
        print(f"the fare for train no. {Trainno} from station {from_station} to station {to_station} is Rs. 500")

    def cancel(Dhruv , ticketno):
        print(f"your ticket no. {ticketno} has been cancelled successfully")


p = train()
p.book()
p.getstatus(1234)   # fixed!
p.getfare(1234, "A", "B")
p.cancel(5678)
