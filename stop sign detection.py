import cv2
import os
import numpy as np

# Klasör ayarları
input_folder = "stop_sign_dataset"
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(input_folder, filename)
        img = cv2.imread(path)
        img_copy = img.copy()

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Geniş toleranslı kırmızı aralık (karanlık dahil)
        lower_red1 = np.array([0, 100, 50])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([160, 100, 50])
        upper_red2 = np.array([179, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        red_mask = cv2.bitwise_or(mask1, mask2)

        contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                aspect_ratio = float(w) / h

                if 0.85 < aspect_ratio < 1.15:
                    cx = x + w // 2
                    cy = y + h // 2

                    cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.circle(img_copy, (cx, cy), 5, (255, 0, 0), -1)
                    cv2.putText(img_copy, f"Center: ({cx}, {cy})", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                    print(f"{filename}: Stop işareti bulundu. Merkez: ({cx}, {cy})")

        cv2.imwrite(os.path.join(output_folder, filename), img_copy)
