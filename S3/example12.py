import torch

t1 = torch.arange(1,25)
print(t1, t1.size(), t1.ndim)

t2 = torch.reshape(t1, (1,2,4,-1))
print(t2, t2.size(), t2.ndim)