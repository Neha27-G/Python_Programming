
def main():

    Arr = [0]*5

    print("Enter the elements :")

    for iCnt in range(5):
        Arr[iCnt] = int(input())
   
    print("Elements of array are :")

    for iCnt in range(5):
        print(Arr[iCnt])

if __name__ == "__main__":
    main()