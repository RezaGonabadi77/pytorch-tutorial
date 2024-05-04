import torch

t1 = torch.tensor([[1,0,1], [2,3,4]])
print(t1, t1.size(), t1.ndim)

t2 = torch.ravel(t1)
print(t2, t2.size(), t2.ndim)

t3 = torch.arange(24).reshape(3,2,4)
print(t3, t3.size(), t3.ndim)

t4 = torch.flatten(t3,end_dim=1)
print(t4, t4.size(), t4.ndim)