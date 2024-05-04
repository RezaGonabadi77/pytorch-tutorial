import torch

t1 = torch.arange(6).reshape(2,3)
print(t1, t1.size(), t1.ndim)

t2 = t1.T
print(t2, t2.size(), t2.ndim)

t3 = torch.arange(24).reshape(2,3,4)
print(t3, t3.size(), t3.ndim)

t4 = torch.transpose(t3,dim0=0, dim1=2)
print(t4, t4.size(), t4.ndim)