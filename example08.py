import torch
from torch.utils.data import Dataset

import glob
from typing import Any
import pandas as pd

class CustomDataset(Dataset):
    def __init__(self,pathname,transform=None,target_transform=None):
        self.file_names= glob.glob(pathname+ '\*\*.txt')
        self.class_map= {'S':0,'Z':1}
        self.transform= transform
        self.target_transform= target_transform
        
    def __len__(self):
        return len(self.file_names)
    
    def __getitem__(self,indx):
        filename= self.file_names[indx]
        df= pd.read_csv(filename,header=None)
        chr= filename.split('\\')[-1][0]
        
        sample= df.iloc[:,0].to_numpy()
        label= self.class_map[chr]
        if self.transform:
            sample= self.transform(sample)
        if self.target_transform:
            label= self.target_transform(label)   
        return sample,label

class ToTensor:
    def __call__(self, sample):
        sample = torch.from_numpy(sample).type(torch.float32)
        return sample

pathname='EEG'
transfrom= ToTensor()
ds= CustomDataset(pathname,transfrom)

sample,label=ds[2]