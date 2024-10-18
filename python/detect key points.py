import cv2
import sys
import os

try:
    sys.path.append('path_to_openpose/build/python/openpose/Release')
    os.environ['PATH'] += 'path_to_openpose/build/x64/Release;' + \
                         'path_to_openpose/build/x64/Debug;' + \
                         'path_to_openpose/build/bin;'
    import pyopenpose as op
except ImportError as e:
    print("Error: OpenPose library not found.")
    raise e

params = {
    "model_folder": "path_to_openpose/models/",
    "hand": False,
    "face": False,
    "net_resolution": "-1x368",
    "num_gpu_start": 0,
}

opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        datum = op.Datum()
        datum.cvInputData = frame
        opWrapper.emplaceAndPop([datum])

        cv2.imshow("OpenPose - Keypoint Detection", datum.cvOutputData)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "path_to_your_test_video.mp4"
    process_video(video_path)
