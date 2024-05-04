import torch

t1 = torch.arange(0,5)
t2 = torch.arange(5,7)

print(t1, t1.size())    
print(t2, t2.size())

t3 = torch.cat((t1,t2),dim=0)
print(t3, t3.size())

#------------------------------

t4 = torch.arange(6).reshape(2,3)
t5 = torch.arange(6,10).reshape(2,2)
print(t4, t4.size())
print(t5, t5.size())

t6 = torch.cat((t4,t5),dim=1)
print(t6, t6.size())

#------------------------------

t7 = torch.tensor([[0, 1],[3,4]]).reshape(1,2,-1)
t8 = torch.arange(6,10).reshape(1,2,-1)
print(t7, t7.size())
print(t8, t8.size())

t9 = torch.cat((t7,t8),dim=0)
print(t9, t9.size())