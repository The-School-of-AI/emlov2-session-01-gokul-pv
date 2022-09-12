#!/usr/bin/env python3
"""
    PyTorch Inference Script
"""

import requests
from PIL import Image
import io

from timm.models import create_model
from timm.utils import setup_default_logging
import torch
import torchvision.transforms as transforms

import hydra
from omegaconf import DictConfig
import logging
import json



@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):
    # setup_default_logging(default_level=logging.CRITICAL, log_path='/dev/null')

    model = create_model(cfg.model, in_chans=3, pretrained=True)
    model.eval()

    # https: //github.com/pytorch/hub/raw/master/images/dog.jpg
    response = requests.get(cfg.image).content
    im = Image.open(io.BytesIO(response))

    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        normalize,
    ])

    # PIL image undergoes transforms.
    img = transform(im)
    img = img.unsqueeze(0)

    with torch.no_grad():
        pred = model(img)
        probs = torch.nn.functional.softmax(pred, dim=1)
        conf, classes = torch.max(probs, 1)


    idx2label = []
    cls2label = {}

    with open("imagenet_class_index.json", "r") as read_file:
        class_idx = json.load(read_file)
        idx2label = [class_idx[str(k)][1] for k in range(len(class_idx))]
        cls2label = {class_idx[str(k)][0]: class_idx[str(k)][1]
                    for k in range(len(class_idx))}

    out_dict = {}
    out_dict["predicted"] = str(idx2label[classes.cpu().numpy()[0]])
    out_dict["confidence"] = float(conf.cpu().numpy()[0] * 100)


    # Serializing json
    json_object = json.dumps(out_dict, indent=4)
    print(json_object)

if __name__ == '__main__':
    logging.disable(logging.CRITICAL)
    main()
