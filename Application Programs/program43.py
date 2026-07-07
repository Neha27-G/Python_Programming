# Input : 5
# Output : -5   -3   -1 

def Display(iNo):
    iCnt = 0

    for iCnt in range(-iNo ,1, 2):
        print(iCnt, end = "\t")
       
def main():

    iValue = 0

    iValue = int(input("Enter the Number :"))

    Display(iValue)
    
if __name__ == "__main__":
    main()
