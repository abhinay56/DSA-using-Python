yr = int(input("enter year : "))
if(yr % 4 == 0):
    print(f"Given year {yr} is an leap year")
elif(yr % 100 == 0 and yr % 400 == 0):
    print(f"Given year {yr} is an leap year")
else:
    print(f"Given year {yr} is not a leap year")