def CallByValue(iNo):
    iNo = iNo + 1

def main():
    iValue = 11

    CallByValue(iValue)

    print("Value After function call : ",iValue)

if __name__ == "__main__":
    main()