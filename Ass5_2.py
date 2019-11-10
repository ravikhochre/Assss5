def fun(no):
    if(no!=0):
        fun(no-1)
        print(no,end=" ")

def main():
    print(" Enter a Number")
    fun(int(input(" Input :")));
    print("")
if __name__=="__main__":
    main()

