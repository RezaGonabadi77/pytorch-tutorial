import torch

t = torch.rand(1,3,5,1,1)
print(t, t.size(), t.ndim)

t1 = torch.squeeze(t)
print(t1, t1.size(), t1.ndim)