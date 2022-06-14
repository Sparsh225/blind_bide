from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
y=True
while(y==True):
  price={}
  name=input("what is Your name ? ")
  bide=int(input("Whats Your bide ? $"))
  price[name]=bide  
  check=input("Are There any other bidders ? Type 'yes' or 'no' ").lower()
  
  if(check=="yes"):
    y=True
    clear()
    price[name]=bide
  else:
    y=False
    for i in price:
      bit=price[i]
      max=0
      if(max<bit):
        max=bit
      print(f"The winner is {i} with a bide of {max} ")
        
      