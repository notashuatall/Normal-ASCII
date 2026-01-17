import cv2
import numpy as np
import os
import time
import sys

# ASCII characters ordered from darkest to lightest
# This mapping matches the brightness levels of the grayscale pixels
ASCII_CHARS = " .:-=+*#%@"

def frame_to_ascii(frame, width):
    """
    Converts a single video frame into a string of ASCII characters.
    """
    # 1. Convert to grayscale
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 2. Get original dimensions and calculate new height with aspect ratio correction
    # Character height-to-width ratio is roughly 2:1 in terminals, so we halve the height.
    h_orig, w_orig = grayscale_frame.shape
    height = int(h_orig * width / w_orig / 2)
    
    # 3. Resize frame
    resized_frame = cv2.resize(grayscale_frame, (width, height))
    
    # 4. Map pixels to ASCII characters
    # We normalize the pixel values (0-255) to the index range of our ASCII_CHARS (0-9)
    # Using numpy vectorization for high performance
    char_indices = (resized_frame / 255 * (len(ASCII_CHARS) - 1)).astype(int)
    
    # Create the ASCII string
    ascii_rows = []
    for row in char_indices:
        ascii_rows.append("".join([ASCII_CHARS[pixel] for pixel in row]))
        
    return "\n".join(ascii_rows)

def play_video(video_path, width=80):
    """
    Handles the video capture, timing, and terminal rendering.
    """
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Retrieve video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0: fps = 24  # Default if FPS cannot be detected
    frame_time = 1.0 / fps

    try:
        print("Starting playback... Press Ctrl+C to stop.")
        time.sleep(1)

        while True:
            start_tick = time.time()
            
            ret, frame = cap.read()
            if not ret:
                break # End of video

            # Process frame
            ascii_frame = frame_to_ascii(frame, width)

            # Clear terminal and render
            # 'cls' for Windows, 'clear' for Unix/Linux/Mac
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.stdout.write(ascii_frame)
            sys.stdout.flush()

            # Timing control: Calculate how long processing took and sleep the remainder
            elapsed_time = time.time() - start_tick
            sleep_time = frame_time - elapsed_time
            if sleep_time > 0:
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\nPlayback stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        # Resource cleanup
        cap.release()
        print("Video resources released.")

def main():
    """
    User interaction and entry point.
    """
    print("--- Terminal ASCII Video Player ---")
    
    video_path = input("Enter the path to the video file: ").strip()
    
    # Handle paths with quotes (common when dragging files into terminal)
    video_path = video_path.replace('"', '').replace("'", "")

    if not os.path.exists(video_path):
        print(f"Error: The file '{video_path}' does not exist.")
        return

    width_input = input("Enter preferred terminal width (default 80): ").strip()
    width = int(width_input) if width_input.isdigit() else 80

    play_video(video_path, width)

if __name__ == "__main__":
    main() # created by Subh(cherry)