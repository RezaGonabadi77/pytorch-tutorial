import torch
import numpy as np

arr = np.arange(6)
print(arr)

t = torch.from_numpy(arr).to(torch.float32)
print(t)

arr2 = t.numpy()
print(arr2)