def Display(Arr, Size):

    print("Entered elements are :")
    for i in range(Size):
        print(Arr[i])

def main():
    iLength = 4

    Brr = [0] * iLength

    print("Enter the element :")

    for i in range(iLength):
        Brr[i] = input()

    Display(Brr, iLength)
    
if __name__ == "__main__":
    main()