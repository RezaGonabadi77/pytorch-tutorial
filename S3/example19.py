import torch
from matplotlib import pyplot as plt
torch.manual_seed(1)

a = torch.randn(2,400)
x = torch.tensor([1.5,1.5])
num = 10


sum_ = ((x[0] - a[0,:])**2) + ((x[1] - a[1,:])**2)
sqrt_sum = torch.sqrt(sum_)
sqrt_sum_sort = torch.sort(sqrt_sum)
ind = sqrt_sum_sort.indices
print(ind[0:num])



min_tensors = a[:, ind[0:num]]

plt.plot(a[0,:], a[1,:], '.b')
plt.plot(x[0], x[1], 'or')
plt.plot(min_tensors[0,:], min_tensors[1,:], 'or',fillstyle='none')
plt.show()

