import os
import torch
import numpy as np
import pandas as pd
from skimage import io, transform
from skimage.transform import resize
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

def encode_from_utf8(x):
    return list(map(float,bin(int(x.encode().hex(),16))[2:]))

def decode_from_bin2(x):
    res = ""
    for i in x:
        res+=str(int(i>0))
        pass
    return bytearray.fromhex(hex(int(res, 2))[2:]).decode()

class CNN(nn.Module):
    def __init__(self):
        super(CNN,self).__init__()
        self.avgpool1 = nn.AvgPool2d(2,2) # kernel size 2x2 (32 = 64/2)
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.maxpool1 = nn.MaxPool2d(2,2) # kernel size 2x2 (32 = 64/2)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.maxpool2 = nn.MaxPool2d(2,2) # kernel size 2x2 (16 = 32/2)
        self.linear1 = nn.Linear(1152,378)
        self.relu3 = nn.ReLU()
        self.linear2 = nn.Linear(378,128)
        self.relu4 = nn.ReLU()
        self.linear3 = nn.Linear(128,24)
        pass
    def forward(self,x):
        out = self.avgpool1(x)
        if DEBUG_TRAIN : print('avgpool1: ', out.shape)
        out = self.conv1(out)
        if DEBUG_TRAIN : print('conv1: ', out.shape)
        out = self.relu1(out)
        if DEBUG_TRAIN : print('relu1: ', out.shape)
        out = self.maxpool1(out)
        if DEBUG_TRAIN : print('maxpool1: ', out.shape)
        out = self.conv2(out)
        if DEBUG_TRAIN : print('conv2: ', out.shape)
        out = self.relu2(out)
        if DEBUG_TRAIN : print('relu2: ', out.shape)
        out = self.maxpool2(out)
        if DEBUG_TRAIN : print('maxpool2: ', out.shape)
        out = out.view(out.size(0),-1)
        if DEBUG_TRAIN : print('view: ', out.shape)
        out = self.linear1(out)
        if DEBUG_TRAIN : print('linear1: ', out.shape)
        out = self.relu3(out)
        if DEBUG_TRAIN : print('relu3: ', out.shape)
        out = self.linear2(out)
        if DEBUG_TRAIN : print('linear2: ', out.shape)
        out = self.relu4(out)
        if DEBUG_TRAIN : print('relu4: ', out.shape)
        out = self.linear3(out)
        if DEBUG_TRAIN : print('linear3: ', out.shape)
        if DEBUG_TRAIN : print()
        return out
    
DEBUG_TRAIN = False
DEBUG_DATA = False
TRAIN = False

MODEL_PATH = './saved_model/BCEWithLogitsLoss-Complete-backup-300epoch-new.tar'
IMG = "./image-data/user-input/img.png"

epoch = 0
learning_rate = 0.0001

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = CNN().double().to(device)
optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)
loss_function = nn.BCEWithLogitsLoss()

if(os.path.isfile(MODEL_PATH)):
    checkpoint = torch.load(MODEL_PATH)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    loss = checkpoint['loss']
    if TRAIN:
        model.train()
    else:
        model.eval()
        
with torch.no_grad():
    model.to(device)
    model.eval()
    tmp = io.imread(IMG)[:,:,2]/255.0
    tmp = resize(tmp, (64, 64))
    x = torch.from_numpy(tmp.reshape(1, 1,64,64)).to(device)
    output = model.forward(x)
    out = decode_from_bin2(output[0].tolist())
    print(out)
    pass