def fun(no):
    if(no!=0):
        fun(no-1)
        print("*",end=" ")

def main():
    print(" Enter a Number")
    fun(int(input(" Input :")));
if __name__=="__main__":
    main()
