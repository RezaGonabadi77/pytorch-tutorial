import torch

t = torch.rand(size=(2,5))
print('t :',t)

t_sum = torch.sum(t,dim=0)
print('t_sum :',t_sum)

t_mean = torch.mean(t, dim=0)
print('t_mean :',t_mean)

t_max = torch.max(t, dim=0)
print('t_max :',t_max)

t_min = torch.min(t, dim=0)
print('t_min :',t_min)

ind = t[t>1]
print(t>1)

t_sort_mean = t_mean.sort()
print('t_sort_mean :',t_sort_mean)

t_var = torch.var(t)
print('t_var', t_var)

t_std = torch.std(t)
print('t_std', t_std)

t_covv = torch.cov(t)
print('t_covv', t_covv)

