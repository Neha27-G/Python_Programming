def main():
    iValue = 0
    iRemainder = 0

    iValue = int(input("Enter the number :"))

    iRemainder = iValue % 2

    if(iRemainder == 0):
        print("Number is Even")

    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()
    
