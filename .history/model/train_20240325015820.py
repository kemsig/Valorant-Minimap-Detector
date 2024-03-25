import ultralytics
from ultralytics import YOLO
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = YOLO('yolov8n.pt')
model.to(device)

results = model.train(
    data="model\\yoloset_lesscomp\\data.yaml",
    lr0=0.01,
    imgsz=256,
    epochs=20,
    batch=5,
    name='vct_vision_v8_with_daug'
)
