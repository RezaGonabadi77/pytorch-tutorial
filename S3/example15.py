import torch

t1 = torch.arange(20).reshape(2,-1)
print(t1, t1.size())

t2 = torch.split(t1, split_size_or_sections=2, dim=1)
print(t2)