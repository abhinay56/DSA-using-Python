print("Program for nested if statement")
theater1 = input("Theater1 is Closed or Opened ?")
Ticket1 = input("Is any Movie tickets are available ?")
theater2 = input("Theater1 is Closed or Opened ?")
Ticket2 = input("Is any Movie tickets are available ?")

if(theater1=="Open"):
    print("The theater1 is Opened Book your tickets if available")
    if(Ticket1=="Available"):
        print("Tickets are Available here you can book your show")
elif(theater2=="Open"):
    print("The theater2 is Opened Book your tickets if available")
    if(Ticket2=="Available"):
        print("Tickets are Available here you can book your show")
else:
    print("Sorry All the the theaters are closed ")
