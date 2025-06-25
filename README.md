# Flappy_Bird_Hand_gesture
# 🐦 Gesture-Controlled Flappy Bird

This project is a creative twist on the classic Flappy Bird game — instead of pressing keys, you flap by showing **all five fingers** to your webcam! The game uses **MediaPipe** for real-time hand tracking and **Pygame** for rendering the gameplay.

---

## 🎮 How It Works

- Show **five fingers** to make the bird flap upward.
- Avoid the green pipes as the bird automatically falls due to gravity.
- Score increases as you pass through pipes.
- The game ends if the bird hits a pipe or the screen boundary.

---

## 🛠 Requirements

Install the necessary Python libraries using pip:

```bash
pip install opencv-python mediapipe pygame
🚀 How to Run
Save the code in a file called gesture_flappy_bird.py.

Run the script:

bash
python gesture_flappy_bird.py
Make sure your webcam is connected and has proper lighting.

A window will appear for the game, and the webcam will track your hand.

Use an open palm (five fingers) to make the bird flap.

⚙️ Game Controls
Gesture	Action
🖐 Five fingers	Bird flaps upward
✊ Fist / others	Bird falls (default)
❌ Escape or close window	Quit the game
📌 Notes
Best used in a well-lit environment with a clear hand in view.

Only one hand is tracked at a time.

You can tweak the flap_strength, gravity, or even colors for personalization.

📷 Dependencies
OpenCV: For webcam feed and frame handling.

MediaPipe: For detecting and counting fingers.

Pygame: For game logic and rendering.

📄 License
This project is free to use for learning and development purposes. Contributions and customizations are welcome!
