import os
import numpy as np
import torch
from torch.utils import data

vision_dir = './vision_files/'
vocal_dir = './audio_files/'
gt_emotions = './gt_emotions_files/'

def make_dataset(mode):
    vision = vision_dir + mode+ '/'
    vocal = vocal_dir + mode + '/'
    gt = gt_emotions + mode + '/'
    vision_files = os.listdir(vision)
    vocal_files = os.listdir(vocal)
    gt_files = os.listdir(gt)
    items = []
    for file in sorted(vision_files):
        vision_path = os.path.join(vision, file)
        vocal_path = os.path.join(vocal, file)
        gt_path = os.path.join(gt, file)
        items.append((vision_path,vocal_path,gt_path))
    return items

class mosei(data.Dataset):
    def __init__(self, quality, mode):
        self.items = make_dataset(mode)
        if len(self.items) == 0:
            raise RuntimeError('Found 0 items, please check the data set')
        self.quality = quality
        self.mode = mode

    def __getitem__(self, index):
        vision_path, vocal_path, gt_path = self.items[index]
        with open(vision_path,'rb') as f:
            vision_file = pickle.load(f)
        with open(vocal_path,'rb') as f:
            vocal_file = pickle.load(f)
        with open(gt_path,'rb') as f:
            gt_file = pickle.load(f)


        return vision_file, vocal_file, gt_file

    def __len__(self):
        return len(self.items)