import torch

t = torch.empty(4,2,5)

t[0] = 0
t[1] = 1
t[2] = torch.randn(2,5)
t[3] = torch.rand(2,5)

print(t)