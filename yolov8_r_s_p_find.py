import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('/content/drive/MyDrive/hw/best.pt')  # 학습된 모델 경로

# Open a connection to the webcam
cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 의미

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Real-time detection loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Perform inference on the frame
    results = model.predict(source=frame, save=False, conf=0.5)  # conf는 신뢰도 임계값

    # Extract predictions from results
    annotated_frame = results[0].plot()  # YOLO에서 시각화된 프레임 생성

    # Display the annotated frame
    cv2.imshow('YOLO Detection', annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
