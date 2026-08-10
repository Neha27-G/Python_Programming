def Display(iptr):
    print("Value of ptr : ",id(iptr))

def main():
    Arr = [10,20,30,40,50]

    print("Base Address of Arr :",id(Arr))

    Display(Arr)

if __name__ == "__main__":
    main()