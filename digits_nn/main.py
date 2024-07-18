import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Initialize the tracker as None
tracker = None

# Initialize the bounding box as None
bbox = None

# Initialize the previous_frame
_, previous_frame = cap.read()
previous_frame = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
previous_frame = cv2.GaussianBlur(previous_frame, (21, 21), 0)

# Initialize the previous position
prev_x, prev_y = None, None

# Motion threshold (consider object as not moving if distance < motion_threshold)
motion_threshold = 2

while True:

    # Capture a new frame
    _, frame = cap.read()

    # Convert to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Compute the absolute difference between the current frame and first frame
    frame_delta = cv2.absdiff(previous_frame, gray)

    # Compute the threshold image
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

    # Apply a series of dilations to fill in the holes
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours on threshold image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If no tracker is initialized, iterate over the contours and find if any of them is large enough
    if tracker is None:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                # If the contour is large enough, start tracking it
                (x, y, w, h) = cv2.boundingRect(contour)
                bbox = (x, y, w, h)
                tracker = cv2.TrackerCSRT_create()
                tracker.init(frame, bbox)
                prev_x, prev_y = x, y
                break

    # If a tracker has been initialized, update it
    if tracker is not None:
        success, bbox = tracker.update(frame)
        if success:
            (x, y, w, h) = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
            # Check if object has moved significantly, if not, consider it as not moving
            if abs(x - prev_x) < motion_threshold and abs(y - prev_y) < motion_threshold:
                cv2.putText(frame, "Object stopped", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                tracker = None
                bbox = None
            else:
                prev_x, prev_y = x, y
        else:
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            tracker = None
            bbox = None

    # Display the frame
    cv2.imshow("Frame", frame)

    # Exit if ESC key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

    # Save the current grayscale frame as the previous frame
    previous_frame = gray

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()