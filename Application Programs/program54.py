def DisplayDigits(iNo):
    iDigit = 0

    while(iNo != 0):
        iDigit = iNo % 10
        print(iDigit)
        iNo = iNo // 10
   
def main():
    iValue = 0

    iValue = int(input("Enter the number:"))

    DisplayDigits(iValue)
    
if __name__ == "__main__":
    main()