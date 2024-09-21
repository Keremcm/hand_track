import cv2
import pyautogui
import mediapipe as mp
import numpy as np
import time
import pygetwindow as gw

# Disable PyAutoGUI failsafe
pyautogui.FAILSAFE = False

# Initialize MediaPipe Hand Tracking module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Get screen resolution
screen_width, screen_height = pyautogui.size()

# Video capture object initialization (webcam)
cap = cv2.VideoCapture(0)

# Set a lower resolution for faster processing
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Check if camera can be opened
if not cap.isOpened():
    print("Unable to open camera!")
    exit()

# Mouse movement smoothing
positions = []
def smooth_coordinates(new_pos, positions, max_len=10):
    positions.append(new_pos)
    if len(positions) > max_len:
        positions.pop(0)
    avg_pos = np.mean(positions, axis=0)
    return avg_pos

# Function to check if position update is necessary
def should_update_position(new_pos, last_pos, threshold=5):
    distance = np.hypot(new_pos[0] - last_pos[0], new_pos[1] - last_pos[1])
    return distance > threshold

# Function to map camera coordinates to screen coordinates with non-linear scaling
def map_camera_to_screen(camera_x, camera_y, cam_width, cam_height, screen_width, screen_height, scale_x=2.0, scale_y=2.0, y_offset=0.1):
    # Define the camera's viewable area as a proportion of the camera frame
    viewable_area_x = 0.8  # Adjust this value as needed (0.0 to 1.0)
    viewable_area_y = 0.8  # Adjust this value as needed (0.0 to 1.0)
    
    # Calculate the normalized coordinates within the viewable area
    norm_x = camera_x / cam_width / viewable_area_x
    norm_y = camera_y / cam_height / viewable_area_y
    
    # Clamp the values to ensure they are within [0, 1]
    norm_x = min(max(norm_x, 0.0), 1.0)
    norm_y = min(max(norm_y, 0.0), 1.0)

    # Apply non-linear scaling
    screen_x = screen_width * (1 - np.power(norm_x, scale_x))
    screen_y = screen_height * np.power(norm_y + y_offset, scale_y)
    
    return screen_x, screen_y

# Tracking states
clicking = False
right_clicking = False
selecting = False
alt_tabbing = False
back = False
dragging = False  # New state for dragging

last_pos = (0, 0)
tab_timer = time.time()
tab_active = False

# Main loop
while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_tip = hand_landmarks.landmark[8]
            cam_x, cam_y = int(finger_tip.x * img.shape[1]), int(finger_tip.y * img.shape[0])

            screen_x, screen_y = map_camera_to_screen(cam_x, cam_y, img.shape[1], img.shape[0], screen_width, screen_height)

            smooth_pos = smooth_coordinates((screen_x, screen_y), positions)
            if should_update_position(smooth_pos, last_pos):
                # Constrain the mouse movement within screen boundaries
                constrained_x = min(max(int(smooth_pos[0]), 0), screen_width - 1)
                constrained_y = min(max(int(smooth_pos[1]), 0), screen_height - 1)
                pyautogui.moveTo(constrained_x, constrained_y)
                last_pos = smooth_pos

            index_tip = hand_landmarks.landmark[8]  # Index finger tip
            thumb_tip = hand_landmarks.landmark[4]  # Thumb tip
            middle_tip = hand_landmarks.landmark[12] # Middle finger tip
            ring_tip = hand_landmarks.landmark[16]   # Ring finger tip
            pinky_tip = hand_landmarks.landmark[20] # Pinky finger tip

            index_x, index_y = int(index_tip.x * img.shape[1]), int(index_tip.y * img.shape[0])
            thumb_x, thumb_y = int(thumb_tip.x * img.shape[1]), int(thumb_tip.y * img.shape[0])
            middle_x, middle_y = int(middle_tip.x * img.shape[1]), int(middle_tip.y * img.shape[0])
            ring_x, ring_y = int(ring_tip.x * img.shape[1]), int(ring_tip.y * img.shape[0])
            pinky_x, pinky_y = int(pinky_tip.x * img.shape[1]), int(pinky_tip.y * img.shape[0])

            index_thumb_distance = np.hypot(index_x - thumb_x, index_y - thumb_y)
            middle_thumb_distance = np.hypot(middle_x - thumb_x, middle_y - thumb_y)
            ring_thumb_distance = np.hypot(ring_x - thumb_x, ring_y - thumb_x)
            pinky_thumb_distance = np.hypot(pinky_x - thumb_x, pinky_y - thumb_x)

            if index_thumb_distance < 20:
                if not clicking:
                    clicking = True
                    pyautogui.mouseDown(button='left')
            else:
                if clicking:
                    clicking = False
                    pyautogui.mouseUp(button='left')

            if middle_thumb_distance < 20:
                if not right_clicking:
                    right_clicking = True
                    pyautogui.rightClick()
            else:
                right_clicking = False

            if ring_thumb_distance < 20:
                if not back:
                    back = True
                    pyautogui.hotkey('ctrl', 'z')
            else:
                back = False

            if pinky_thumb_distance < 20:
                if not alt_tabbing:
                    alt_tabbing = True
                    pyautogui.hotkey('alt', 'tab')
            else:
                alt_tabbing = False

    cv2.imshow("Hand Tracking", img) 

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
