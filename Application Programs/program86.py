def Display(Arr, Size):

    for i in range(Size):
        print(Arr[i])

def main():
    iLength = 4

    Brr = [0] * iLength

    Brr[0] = 10 
    Brr[1] = 20
    Brr[2] = 30
    Brr[3] = 40

    Display(Brr, iLength)
    
if __name__ == "__main__":
    main()