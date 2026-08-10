def Display(Arr):

    for i in range(0,8):
        print(Arr[i])

def main():
    Brr = [10,20,30,40]    # issue index out of range

    Display(Brr)
    
if __name__ == "__main__":
    main()