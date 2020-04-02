# Program To Read video
# and Extract Frames
import cv2,os


# Function to extract frames
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0
    if not os.path.exists('temp'):
        os.makedirs('temp')
    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
        #cv2.imwrite(f'EightXEight{str(i)+str(j)}/{newname}' + ".jpg", roi)

        # Saves the frames with frame-count
        cv2.imwrite(f'temp/frame{count}.jpg', image)

        count += 1


# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("C:/Users/ankit/OneDrive/Desktop/output.mp4")
