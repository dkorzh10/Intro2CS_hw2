import torch
import torch.nn as nn
from torchvision.models import resnet50


class Model(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.network = resnet50()

        