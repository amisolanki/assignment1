
print ("""Enter 1 for Addition

         Enter 2 for Substraction

         Enter 3 for multiplication

         Enter 4 for division
  
         Enter 5 for modulodivision""")

ch=int(input("Enter ur choice:"))

if ch==1:
    num=int(input("Enter the total numbers for the operations:"))
    ans=0
    for num in range(num):
        a=int(input("Enter the number:"))
        
        ans=ans+a
        print(ans)

       
elif ch==2:
     num=int(input("Enter the total numbers for the operations:"))
     ans=0 
     for num in range(num):
        a=int(input("Enter the number:")
        ans=a-ans 
        print(ans)

elif ch==3:
     num=int(input("Enter the total numbers for the operations:"))
   
     ans=1
     for num in range(num):
        a=int(input("Enter the number:"))
        
        ans=ans*a
        print(ans)

elif ch==4:
     num=int(input("Enter the total numbers for the operations:"))
    
     ans=1
     for num in range(num):
        a=int(input("Enter the number:"))
        
        
        ans=a/ans
        print(ans)

else:

     print "Enter proper choice..."










 















































