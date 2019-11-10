
b=0
def Addition(no):
   
   if no>0:
     global b;
     d=no%10;
     b=b+d;
     return  Addition(int(no/10))
   return b;

def Decorator(Newfun):
 def Modifier(no):
  if no<0:
   no=-no;
  return Newfun(no);
 return Modifier;


Add=Decorator(Addition);

def main():
  no=int(input("Enter a number:"))
  print("Addition:",Add(no));

if __name__=="__main__":
  main();
