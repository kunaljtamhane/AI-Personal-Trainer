# Personal AI Gym Trainer
**Personal AI Gym Trainer** is a computer vision-based virtual fitness assistant that helps you monitor and improve your workout form. This project focuses on tracking and analyzing dumbbell curls, providing real-time feedback on your exercise performance. By leveraging OpenCV and a custom Pose Detection module, it detects key body landmarks, calculates arm angles, and counts the number of repetitions, all while giving you visual feedback during your workout.

## Features
Real-Time Pose Detection: Accurately tracks key body landmarks, ensuring precise monitoring of your movements.
Repetition Counting: Automatically counts the number of dumbbell curls based on your arm’s movement direction.
Angle Calculation: Measures the angle of your arm during curls to determine the percentage of each rep's completion.
Visual Progress Bar: Displays a progress bar and repetition count on your screen, providing immediate feedback.
Performance Monitoring: Shows frames per second (FPS) to help you keep track of the system’s performance.

## Technologies Used
OpenCV: For video capture, image processing, and overlaying visual feedback.
NumPy: For efficient mathematical calculations, including interpolation of angles.
Custom Pose Detection Module: A specialized module that detects and analyzes human poses using key body landmarks.

## How It Works
Pose Detection: Captures your workout session through a video feed. The custom pose detection module identifies key landmarks like shoulders, elbows, and wrists.

Angle Measurement: Calculates the angle between the shoulder, elbow, and wrist to monitor your arm's movement during curls.

Repetition Counting: As you perform curls, the system counts your repetitions based on the direction of your arm movement (up or down).

Visual Feedback: The screen displays a progress bar indicating how much of the curl is completed, along with the total repetition count.
