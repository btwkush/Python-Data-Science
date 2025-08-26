from ultralytics import YOLO

# Pre-trained YOLOv8 Nano model (fast aur lightweight)
model = YOLO("yolov8n.pt")

# Webcam se live detection (source=0 matlab default camera)
model.predict(
    source=0,   #webcam
    show=True   #live window dikhayega
    conf=0.5    #confidence threshold(50%)
)

