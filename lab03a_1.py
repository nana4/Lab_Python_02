###Q1)
num=raw_input("enter a number to send: ")
num=int(num)
while num>0:
    coded=num%10
    print coded,
    num=num/10

print "\n------------------------------------------------"
###Q2)
num=raw_input("enter a number to send: ")
num=int(num)
while num>0:
    coded=(num+7)%10
    print coded,
    num=num/10
print "\n------------------------------------------------"
