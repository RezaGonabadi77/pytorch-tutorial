import torch

t = torch.rand(2,5,4)
print(t, t.size(), t.ndim)

t1 = torch.unsqueeze(t, dim=3)
print(t1, t1.size(), t1.ndim)