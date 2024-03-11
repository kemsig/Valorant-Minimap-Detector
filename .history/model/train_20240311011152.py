import ultralytics
from ultralytics import YOLO
import torch


model = YOLO('yolov8n.pt')

results = model.train(
    data="./yoloset/data.yaml",
    imgsz=226,
    epochs=10,
    batch=5,
    name='vct_vision_v8'
)