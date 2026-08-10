def CallByAddress(ptr):
    ptr = ptr + 1
    return ptr

def main():
    iValue = 11

    iValue = CallByAddress(iValue)

    print("Value After function call : ",iValue)

if __name__ == "__main__":
    main()