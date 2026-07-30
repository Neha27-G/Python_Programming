
def main():

    Arr = [10,20,30,40,50]

    print("Enter the elements :")

    Arr[0] = int(input())
    Arr[1] = int(input())
    Arr[2] = int(input())
    Arr[3] = int(input())
    Arr[4] = int(input())

    print("Elements of array are :")

    for iCnt in range(5):
        print(Arr[iCnt])

if __name__ == "__main__":
    main()