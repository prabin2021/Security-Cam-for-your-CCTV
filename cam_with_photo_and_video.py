
import cv2
from datetime import datetime

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start the video capture
video = cv2.VideoCapture(0)

# Define the codec for the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_filename = "video.mp4"
fps = 5.0  # Frames per second
out = None
recording = False

while True:
    check, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
        
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
            if not recording:
                height, width, channels = frame.shape
                out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))
                recording = True
            
            out.write(frame)
        
        else:
            if recording:
                out.release()
                recording = False

        # Display the frame
        cv2.imshow("CC TV Camera", frame)
        key = cv2.waitKey(1)

        # Exit when 'e' is pressed
        if key == ord('e'):
            break

# Release the video capture and writer objects
video.release()
if recording:
    out.release()
cv2.destroyAllWindows()
