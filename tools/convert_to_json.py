import torch
import json
import os

for file in os.listdir("."):
    if file.endswith(".pt"):
        message = torch.load(file)
        json.dump(message, open(file.replace("pt", "json"), "w"))