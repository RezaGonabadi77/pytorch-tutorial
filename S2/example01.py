# getting two number from user and create tensor with them
# with 1 step and then print the result
import torch

num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))

#Create tensor manualy
t1 = torch.tensor([i for i in range(num1,num2+1)], dtype=torch.float32)
#Print the result
print(t1, t1.dtype)

#Create tensor using linspace
t2 = torch.linspace(num1,num2,num2-num1, dtype=torch.float32)
#Print the result
print(t2, t2.dtype)

#Create tensor using arange
t3 = torch.arange(num1,num2+1,dtype=torch.float32)
#Print the result
print(t3, t3.dtype)