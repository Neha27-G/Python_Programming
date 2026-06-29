def Display(iNo):
    
    #Updator
    if(iNo < 0):
        iNo = -iNo

    for i in range(iNo, 0 , -1):
        print("Jay Ganesh...")

def main():

    iValue = int(input("Enter the Frequency :"))

    Display(iValue)
  
if __name__== "__main__":
    main()