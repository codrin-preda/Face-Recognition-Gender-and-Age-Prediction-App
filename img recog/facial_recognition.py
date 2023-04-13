import threading
import cv2
from deepface import DeepFace
import pandas as pd

img = cv2.imread("img.jpg")


data = {
    # "Name": [],
    "Age": [],
    "Gender": [],
    # "Race": []
}

res = DeepFace.analyze(cv2.imread("img.jpg"), actions=("gender", "age"))
data["Gender"].append(res[0]["dominant_gender"])
data["Age"].append(res[0]["age"])
# data["Race"].append(res[0]["dominant_race"])

df = pd.DataFrame(data)
print(df)

df.to_csv("data.csv")

# results = DeepFace.analyze(img, actions = ("gender", "age", "emotion"))

# print(results)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
counter = 0

reference_img = cv2.imread("img.jpg")  

face_match = False


def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False


while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1
        if face_match:
            cv2.putText(frame, "MATCH!", (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (160, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()