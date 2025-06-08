import torch
import torch.nn as nn
import torch.nn.functional as F

class ResNet(nn.Module):
    def __init__(self):
        super(ResNet, self).__init__()

        expansion = 4

        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3,)