import torch

t1 = torch.tensor([3,2,4,1]).reshape(1,4)
t2 = torch.tensor([3,3,1,2]).reshape(1,4).T

print(t1, t1.size())
print(t2, t2.size())

t_multi = t1 * t2
print(t_multi)

t_mat = torch.matmul(t1,t2)
print(t_mat)

t_sum = t1 + t2
print(t_sum)

t_power = t1 ** t2
print(t_power)

t_div = t1 / t2
print(t_div)