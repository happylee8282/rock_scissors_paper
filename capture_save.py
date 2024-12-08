import cv2
import numpy as np
import os

# 절대 경로 설정
base_dir = r'C:\\Users\\leejh\\Desktop\\capture'  # 저장할 경로를 명확히 지정
cnt = 0  # 저장된 이미지 수
target_cnt = 10  # 저장할 최대 이미지 수
roi = None  # ROI 초기화

# 디렉토리 생성
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# 저장 디렉토리 설정
dir = os.path.join(base_dir, "rock")
if not os.path.exists(dir):
    os.makedirs(dir)

# 저장 경로 출력
print(f"이미지가 저장될 디렉토리: {dir}")

# 카메라 열기
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("스페이스를 눌러 ROI를 설정하세요.")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    img_draw = frame.copy()

    if roi:  # ROI가 설정된 경우
        x, y, w, h = roi
        if w > 0 and h > 0:  # ROI 크기가 유효한 경우만
            roi_frame = frame[y:y + h, x:x + w]
            file_name_path = os.path.join(dir, f'rock_{cnt}.jpg')
            cv2.imwrite(file_name_path, roi_frame)  # ROI만 저장
            cnt += 1
            if cnt >= target_cnt:
                print("최대 수집 이미지에 도달했습니다.")
                break

        # ROI에 사각형 그리기
        cv2.rectangle(img_draw, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img_draw, f"Captured: {cnt}/{target_cnt}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 결과 출력
    cv2.imshow("Hand Capture", img_draw)

    # 키 입력 대기
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키
        break
    elif key == ord(' '):  # 스페이스바 눌렀을 때 ROI 설정
        roi = cv2.selectROI("Hand Capture", frame, False, False)
        if sum(roi) == 0:  # ROI를 선택하지 않은 경우
            roi = None

cap.release()
cv2.destroyAllWindows()
print("프로그램 종료.")
print(f"이미지가 저장된 디렉토리: {dir}")
