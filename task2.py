n1=input(" enter  the starting range ")
n2=input(" enter the ending range ")
n2=int(n2)
n1=int(n1)

sum = 0
for i in range(n1,n2+1):
 sum+=i
if i==n2:
 print("The addition between",n1 ,n2 ,"is ", sum)


