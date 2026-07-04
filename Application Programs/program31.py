def main():
    iValue = 0

    iValue= int(input("Enter The Number :"))

    if((iValue % 3 == 0) and (iValue % 5 == 0)):
        print("Number is Divisible by 3 and 5")
    else:
        print("Number is Not Divisible by 3 and 5")

if __name__ =="__main__":
    main()