def Display(iNo):
    
    # Filter
    if(iNo < 0):
        print("Invalid Input")
        return

    for i in range(iNo):
        print("Jay Ganesh...")

def main():

    iValue = int(input("Enter the Frequency :"))

    Display(iValue)
  
if __name__== "__main__":
    main()