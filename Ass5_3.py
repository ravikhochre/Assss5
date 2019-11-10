def fun(no):
    if(no!=0):
        print(no,end=" ")
        fun(no-1)
       

def main():
    print(" Enter a Number")
    fun(int(input(" Input :")));
    print("")
if __name__=="__main__":
    main()

