def AddTwoNumbers(fNo1 , fNo2):
    fAns = 0.0

    fAns = fNo1 + fNo2

    return fAns

def main():
    fValue1 = 0.0
    fValue2 = 0.0
    fResult = 0.0

    fValue1 = float(input("Enter first number :"))
    fValue2 = float(input("Enter Second number :"))

    fResult = AddTwoNumbers(fValue1,fValue2)
    print("Addition is :",fResult)

if __name__ == "__main__":
    main()
    
