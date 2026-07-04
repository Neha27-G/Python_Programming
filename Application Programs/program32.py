def CheckDivisible(iNo):
    if((iNo % 3 == 0) and (iNo % 5 == 0)):
        print("Number is Divisible by 3 and 5")
    else:
        print("Number is Not Divisible by 3 and 5")
    
def main():
    iValue = 0

    iValue= int(input("Enter The Number :"))

    CheckDivisible(iValue)

if __name__ =="__main__":
    main()