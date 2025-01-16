import cv2
import os
import time

# 저장 디렉토리 설정
save_directory = "img_capture"  # 저장할 디렉토리
os.makedirs(save_directory, exist_ok=True)

# 절대 경로 설정
base_dir = r'/home/happy/Desktop/rocky/mand'

os.makedirs(base_dir, exist_ok=True)
dir = os.path.join(base_dir, "man")
os.makedirs(dir, exist_ok=True)

print(f"이미지가 저장될 디렉토리: {dir}")

def capture_images():
    file_prefix = input("Enter a file prefix to use: ")
    file_prefix = f'{file_prefix}_'
    print(file_prefix)

    cap = cv2.VideoCapture(0)  # 카메라 열기
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("스페이스를 눌러 ROI를 설정하세요.")
    print("'c' -> 이미지 캡처, 'q' -> 종료")

    cnt = 0
    target_cnt = 10  # 저장할 최대 이미지 수
    roi = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        img_draw = frame.copy()

        if roi:  # ROI가 설정된 경우
            x, y, w, h = roi
            if w > 0 and h > 0:  # ROI 크기가 유효한 경우만
                roi_frame = frame[y:y + h, x:x + w]
                file_name = os.path.join(dir, f'{file_prefix}img_{cnt}.jpg')
                cv2.imwrite(file_name, roi_frame)  # ROI만 저장
                print(f"이미지 저장 완료 (ROI): {file_name}")
                cnt += 1
                if cnt >= target_cnt:
                    print("최대 수집 이미지에 도달했습니다.")
                    break

            # ROI에 사각형 그리기
            cv2.rectangle(img_draw, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 결과 출력
        cv2.putText(img_draw, f"Captured: {cnt}/{target_cnt}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Hand Capture", img_draw)

        # 키 입력 대기
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC 키
            break
        elif key == ord(' '):  # 스페이스바 눌렀을 때 ROI 설정
            roi = cv2.selectROI("Hand Capture", frame, False, False)
            if sum(roi) == 0:  # ROI를 선택하지 않은 경우
                roi = None
        elif key == ord('c'):  # 이미지 캡처
            while cnt <= target_cnt:
                file_name = os.path.join(dir, f'{file_prefix}img_{cnt}.jpg')
                cv2.imwrite(file_name, frame)
                print(f"이미지 저장 완료: {file_name}")
                cnt += 1
                time.sleep(0.5)
                if cnt >= target_cnt:
                    print("최대 수집 이미지에 도달했습니다.")
                    break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images()
