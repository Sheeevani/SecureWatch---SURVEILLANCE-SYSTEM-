# SecureWatch---SURVEILLANCE-SYSTEM-

Device Connectivity: The program should be able to connect to various video recording devices, such as a mobile phone, external camera, or laptop webcam. This can be achieved using appropriate libraries or APIs.

Face Detection: Utilize a face detection algorithm or library (such as OpenCV) to identify and locate human faces within the video stream.

Timestamping: Capture and store the exact date and time when a human face enters the camera's field of view. This information can be saved alongside the recorded video or in a separate log file.

Activity Monitoring: Record all activities performed by the detected human face. This can include movements, gestures, or any other relevant actions that you wish to track. Store this information alongside the recorded video or in a separate log file.

Video Recording: Continuously record the video stream from the connected device. When a human face is detected, store the recorded video, including the period before and after the face appeared. This enables capturing complete footage of the activities performed by the individual.

Storage Management: Implement a mechanism to manage storage efficiently. Consider options such as automatically deleting old recordings to free up space or compressing video files to reduce storage requirements.

User Interface: Design a user-friendly interface for starting and stopping the surveillance program, displaying the video stream, and providing access to stored recordings and activity logs.






Here's an explanation of the code:

Importing Libraries: The required libraries are imported, including cv2 for computer vision operations, time for time-related functions, datetime for timestamping, argparse for command-line argument parsing, and os for file and directory operations.

Loading Cascade Classifier: The Haar cascade classifier XML file (haarcascade_frontalface_default.xml) is loaded, which contains the properties of a human face for detection.

Video Capture Initialization: The program starts capturing video from the default camera (index 0) using cv2.VideoCapture(0).

Main Loop: The program enters a continuous loop to read frames from the video capture.

Frame Processing: Each frame is checked for validity (check) and converted to grayscale using cv2.cvtColor().

Face Detection: The face_cascade.detectMultiScale() function is used to detect faces in the grayscale frame. It returns the coordinates and dimensions of the detected faces.

Drawing Rectangles: For each detected face, a rectangle is drawn on the color frame using cv2.rectangle(). Additionally, the current date and time are obtained using datetime.now() and saved in the format of YYYY-Mmm-DD-HH-MM-SS-ms.

Saving Face Images: The color frame with the detected face rectangle is saved as a JPEG image file with the name "face detected" followed by the timestamp.

Displaying the Frame: The processed frame with the detected faces and rectangles is displayed using cv2.imshow().

Key Press Handling: The program waits for a key press (cv2.waitKey(1)). If the 'q' key is pressed, the program proceeds to generate a video file and exits the loop.

Video File Generation: The program uses command-line argument parsing to define the extension of the images (-ext) and the output video file (-o). It retrieves the list of image files in the current directory with the specified extension.

Setting Video Parameters: The height, width, and number of channels (color channels) of the first image in the list are extracted to define the video dimensions.

Video Writer Initialization: A cv2.VideoWriter object is initialized with the output file name, video codec (forcc), frames per second (5.0), and dimensions obtained from the image.

Writing Frames to Video: The program iterates through the list of image files, reads each image, and writes it to the video file using the out.write() function.

Cleanup: After all images are processed, the video capture is released (video.release()) and all OpenCV windows are closed (cv2.destroyAllW
