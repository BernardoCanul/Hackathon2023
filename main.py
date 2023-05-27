import cv2

cap = cv2.VideoCapture(0)

class_names = ['Cartón', 'Vidrio', 'Metal', 'Papel', 'Plastico', 'Basura']
while True:
    ret, frame = cap.read()

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 