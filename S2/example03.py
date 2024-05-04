import torch

t1 = torch.tensor([[[1,2,3],[4,5,6]],[[0,0,0],[0,0,0]]])
print(t1, t1.ndim, t1.size())

t2 = torch.tensor([[[1,2,3],[4,5,6]],[[0,0,0],[0,0,0]],[[1,1,1],[0,0,0]],[[0,0,0],[2,2,2]]])
print(t2, t2.ndim, t2.size())