def CalculateTicketPrice(iAge):

    # Filter
    if(iAge < 0):
        print("Invalid Input\n")
        return 0

    if(iAge >= 0  and  iAge <=5):
        return 0

    elif(iAge >= 6  and  iAge <=18):
        return 500

    elif(iAge >= 19  and  iAge <=50):
        return 900

    else:
        return 400


def main():
    iValue = 0
    iRet = 0

    iValue = int(input("Please Enter the Age to Calculate Ticket Price: "))

    iRet = CalculateTicketPrice(iValue)
    
    print("Your Ticket price will be",iRet, "rupees")

if __name__== "__main__":
    main()