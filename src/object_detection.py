from ultralytics import YOLO
from PIL import Image

def detect(file):
    model = YOLO('models/yolov8x.pt')
    image = Image.open(file)

    detect_results = model(image) 
    results = []

    for r in detect_results:
        boxes = r.boxes.cpu().numpy()

        for idx, cls in enumerate(boxes.cls):
            name = r.names[cls]
            print(name, boxes.conf[idx])
            
            results.append(f"{name}: {boxes.conf[idx]}")

    return results