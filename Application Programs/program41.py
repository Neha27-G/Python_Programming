# Input : 5
# Output : -5  -4  -3  -2  -1

def Display(iNo):
    iCnt = 0

    for iCnt in range( -iNo ,0):
        print(iCnt, end = "\t")
       
def main():

    iValue = 0

    iValue = int(input("Enter the Number :"))

    Display(iValue)
    
if __name__ == "__main__":
    main()
