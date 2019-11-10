def Factioral(no):
  if no==0:
    return 1;
  else:
    return no*Factioral(no-1);


def Decorator(Nfactioral):
 def Modifier(no):
  if no<0:
   no=-no;
  return Nfactioral(no);
 return Modifier;


Fact=Decorator(Factioral);

def main():
  no=int(input("Enter a number:"))
  print("Factioral is:",Fact(no));

if __name__=="__main__":
  main();
