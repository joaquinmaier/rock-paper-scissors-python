import cv2
import time
import mediapipe as mp

model_path = 'models/gesture_recognizer.task'

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = GestureRecognizerOptions(
    base_options = BaseOptions( model_asset_path=model_path ),
    running_mode = VisionRunningMode.LIVE_STREAM,
    result_callback = lambda result, _, __: print(f'{result.gestures}')
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise Exception('VIDEO CAPTURE DID NOT OPEN MOTHERFUCKER')

HERESYOURFUCKINGTIMESTAMP = 0

with GestureRecognizer.create_from_options(options) as recognizer:
    while True:
        ret, frame = cap.read()

        if not ret:
            print('Frame read incorrectly')
            continue

        mp_image = mp.Image( image_format=mp.ImageFormat.SRGB, data=frame )
        

        recognizer.recognize_async( mp_image, HERESYOURFUCKINGTIMESTAMP )

        HERESYOURFUCKINGTIMESTAMP += 1

        cv2.imshow('I FUCKING HATE MEDIAPIPE', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
