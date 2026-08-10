def Display(iptr):
    i = 0  

    print(iptr[i])
    i += 1

    print(iptr[i])
    i += 1

    print(iptr[i])

def main():
    Arr = [10,20,30,40,50]

    Display(Arr)
    
if __name__ == "__main__":
    main()