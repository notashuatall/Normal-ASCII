GEMINI PROMPT :   ```
- Maintain the original video FPS for smooth playback, retrieved via:
  ```python
  cap.get(cv2.CAP_PROP_FPS)
  ```
- Use `time.sleep()` for timing control.
- Implement error handling with try-except-finally to ensure resource cleanup on interruption.

### 4. User Interaction

- Prompt the user to input the path of the video file.
- Allow optional input for terminal width, defaulting to **80 characteAs a Python Developer, your task is to create a script that displays any video file directly in the terminal using ASCII characters. This script will help users stream videos in a console environment, making it ideal for low-resource systems or artistic projects.

## Key Requirements and Implementation Details

### 1. Libraries & Setup

- Use **opencv-python (cv2)** for extracting video frames.
- Use **numpy** for efficient manipulation of pixel data.
- Use **os** and **time** for controlling terminal display and synchronization.

### 2. Image Processing Logic

- Convert each video frame to **grayscale**.
- Map pixel brightness to ASCII characters from the string **" .:-=+*#%@"**, ranging from darkest to lightest.
- Resize frames for terminal display with aspect ratio correction: 
  ```python
  height = int(frame_height * width / frame_width / 2)
  ```
  to compensate for character height-to-width ratio.

### 3. Playback Engine

- Clear the terminal before drawing each frame using:
  ```python
  os.system('cls' if os.name == 'nt' else 'clear')
rs**.
- Verify the video file exists before attempting playback.

**Note:** Please include comprehensive comments in your code for clarity.

## Implementation Approach

- Request user input for video path and display width.
- Validate the file path.
- Use OpenCV to open and process the video.
- Loop through video frames, convert to ASCII, and print in terminal.
- Control frame rate for smooth viewing.
- Handle interruptions gracefully to release resources properly.
