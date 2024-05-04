import torch

t1 = torch.rand(32,1,5,5)
print(t1.size(), t1.ndim)

t2 = torch.flatten(t1, end_dim =2)
print(t2.size(), t2.ndim)