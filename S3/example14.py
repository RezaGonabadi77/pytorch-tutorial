import torch

t = torch.arange(4).reshape(2,-1)
print(t, t.size())

t1 = torch.repeat_interleave(t,repeats=2,dim=0).repeat_interleave(repeats=2, dim=1).tile(dims=(1,2))
print(t1)