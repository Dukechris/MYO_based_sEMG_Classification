import torch
from torchvision import datasets
from torch.utils.data import Dataset
import pandas as pd
import glob



##################################    CSV Dataset     ##################################
class CSVDataset(Dataset):
    def __init__(self, csv_file_dir, transform=None):
        self.data = PdReadCSVInDir(csv_file_dir)
        self.transform = transform
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        item = self.data.iloc[index, 0:10]
        label = [ int(self.data.iloc[index][10]) ]
        if self.transform:
            item = self.transform(item)
        item = 10.0 * torch.div(torch.Tensor(item), torch.norm(torch.Tensor(item)))
        # item.view_as(torch.zeros(1, 1, 10))
        return item.view_as(torch.zeros(1, 10)), torch.LongTensor(label)
    def GetLabel(self,index):
        return int(self.data.iloc[index][10])

def PdReadCSVInDir(csv_file_dir):
    allFiles = glob.glob(csv_file_dir + "/*.csv")
    DataFrame = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=None)
        list_.append(df)
    DataFrame = pd.concat(list_)
    return DataFrame

##################################    END CSV Dataset     ##################################