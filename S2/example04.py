import torch
from matplotlib import pyplot as plt

torch.manual_seed(2)
t1 = torch.randn(2,100)
#print(t1, t1.ndim, t1.size())


num = 5
x = torch.randperm(t1.size(1))
sel = t1[:,x[:num]]
print(sel)


plt.plot(t1[0,:],t1[1,:],'.b')
plt.plot(sel[0,:],sel[1,:],'or', fillstyle = 'none')
plt.show()