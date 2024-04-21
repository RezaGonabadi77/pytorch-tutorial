import torch

t1 = torch.tensor([1,2,3])
print(t1)
print('The shape of the tensor is :', t1.shape, 'the number of dimension is :', t1.ndim)

t2 = torch.tensor([[1],[2],[3]])
print(t2)
print('The shape of the tensor is :', t2.shape, 'the number of dimension is :', t2.ndim)

t3 = torch.tensor([[1,2,3],[4,5,6]])
print(t3)
print('The shape of the tensor is :', t3.shape, 'the number of dimension is :', t3.ndim)

t4 = torch.tensor([[1,0,0],[0,1,0],[0,0,1]])
print(t4)
print('The shape of the tensor is :', t4.shape, 'the number of dimension is :', t4.ndim)