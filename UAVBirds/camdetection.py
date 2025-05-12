from ultralytics import YOLO
import cv2
import time
import psutil
import os

# Load YOLO model
model = YOLO("best.pt")

# Open webcam (use 0 for default camera)
cap = cv2.VideoCapture(0)

# Get frame dimensions
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
color = (0, 255, 0)
thickness = 2

# Frame timing
prev_time = 0

# Start inference stream from webcam
results_generator = model.predict(source=0, stream=True, imgsz=640, conf=0.5, iou=0.3, device=0)

for result in results_generator:
    # FPS calculation
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time else 0
    prev_time = current_time

    # System usage
    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent

    # Plot detection results
    frame = result.plot()

    # Overlay FPS, CPU, RAM info
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 25), font, font_scale, color, thickness)
    cv2.putText(frame, f"CPU: {cpu_percent:.1f}%", (10, 50), font, font_scale, color, thickness)
    cv2.putText(frame, f"RAM: {ram_percent:.1f}%", (10, 75), font, font_scale, color, thickness)

    # Show output
    cv2.imshow("YOLO Live Detection", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
