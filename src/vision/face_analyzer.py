import cv2
from deepface import DeepFace

def capture_image():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            return None

        try:
            # Analyze the facial expression in real-time
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            if result:
                emotion = result[0]['dominant_emotion']
                cv2.putText(frame, f"Emotion: {emotion}", (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        except:
            cv2.putText(frame, "Emotion: unknown", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the live video
        cv2.imshow('Press Space to Capture Image', frame)

        # Wait for the user to press the space key
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):
            break

    cap.release()
    cv2.destroyAllWindows()
    return frame

def analyze_expression(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if result:
            emotion = result[0]['dominant_emotion']
            return emotion
        return None
    except Exception as e:
        print(f"Error analyzing expression: {e}")
        return None