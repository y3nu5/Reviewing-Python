print("Welcome to the game zone")

Height = int(input("How is your height?"))
bill = 0

if Height>120:
    Age = int(input("How is your age"))
    
    if Age < 12:
        bill = 5
        print("Please pay 5$")
    elif Age <= 18:
        bill = 7
        print("Please pay 7$") 
    elif Age >= 45 and Age <= 55:
        bill = 0
        print('You getting free ticket to ride')
    else:
        bill = 12
        print("Please pay 12$")

    wants_photos = input("Do you want take photo? type y for yes and n for no")

    if wants_photos == "y":
        bill += 3
        
    print (f"Please pay bill is {bill}$")

else:
    print("You Can Not Ride")