import ultralytics
from ultralytics import YOLO
import torch

torch.cuda.set_device(0)

model = YOLO('yolov8n.pt', device='gpu')

results = model.train(
    data="model\\yoloset_lesscomp\\data.yaml",
    lr0=0.01,
    imgsz=256,
    epochs=20,
    batch=5,
    name='vct_vision_v8_less_comp'
)
