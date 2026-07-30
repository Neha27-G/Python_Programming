Arr = [0] * 7
def main():

    Arr[0]= 10
    Arr[3]= 20
    Arr[6]= 30

    print(len(Arr))

    print(Arr[0])
    print(Arr[3])
    print(Arr[6])

    print(Arr[2])        #garbage value
    print(Arr[5])
    
if __name__ == "__main__":
    main()