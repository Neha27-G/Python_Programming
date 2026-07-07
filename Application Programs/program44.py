# Input : 5
# Output : -5  -4  -3  -2  -1  0  1  2  3   4  5  

def Display(iNo):
    iCnt = 0

    for iCnt in range(-iNo , iNo+1):
        print(iCnt, end = "\t")
       
def main():

    iValue = 0

    iValue = int(input("Enter the Number :"))

    Display(iValue)
    
if __name__ == "__main__":
    main()
