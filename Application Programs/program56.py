def DisplayDigits(iNo):

    while(iNo > 0):
        print( iNo % 10)
        iNo = iNo // 10
   
def main():
    iValue = 0

    iValue = int(input("Enter the number:"))

    DisplayDigits(iValue)
    
if __name__ == "__main__":
    main()