import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

TARGET = "bottle"

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open the camera. ")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive the frame. ")
        break

    results = model(frame, verbose=False)

    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        confidence = box.conf[0].item()
        class_index = int(box.cls[0].item())
        class_name = model.names[class_index]

        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)
        
        if class_name == TARGET:
            print(f"Detected: {class_name}  center_x: {center_x}  center_y: {center_y}  confidence: {confidence:.2f}")



    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()