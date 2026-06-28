def CheckEvenOdd(iNo):

    iRemainder = 0

    iRemainder = iNo % 2

    if(iRemainder == 0):
        print("Number is Even")

    else:
        print("Number is Odd")

def main():
    iValue = 0
    
    iValue = int(input("Enter the number :"))

    CheckEvenOdd(iValue)

if __name__ == "__main__":
    main()
    
