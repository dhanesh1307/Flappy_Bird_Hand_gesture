import cv2
import mediapipe as mp
import pygame
import random
import sys

# ============ Gesture Detection ============

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def get_finger_count(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)
    finger_count = 0

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            tips = [4, 8, 12, 16, 20]

            # Thumb
            if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
                finger_count += 1

            # Other fingers
            for tip_id in tips[1:]:
                if landmarks[tip_id].y < landmarks[tip_id - 2].y:
                    finger_count += 1

            break  # Only use one hand
    return finger_count

# ============ Pygame Setup ============

pygame.init()
WIDTH, HEIGHT = 500, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gesture-Controlled Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 40)

# Colors
WHITE = (255, 255, 255)
BIRD_COLOR = (255, 0, 0)
PIPE_COLOR = (0, 200, 0)

# Game variables
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.6
flap_strength = -10
score = 0

pipes = []
pipe_width = 80
pipe_gap = 200
pipe_speed = 4

def create_pipe():
    top = random.randint(100, 400)
    bottom = top + pipe_gap
    return [WIDTH, top, bottom]

pipes.append(create_pipe())

# ============ Main Loop ============

cap = cv2.VideoCapture(0)

running = True
while running:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Handle gesture
    fingers = get_finger_count(frame)
    if fingers == 5:
        bird_velocity = flap_strength

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic
    bird_velocity += gravity
    bird_y += bird_velocity

    # Move pipes
    for pipe in pipes:
        pipe[0] -= pipe_speed

    # Add new pipes
    if pipes[-1][0] < WIDTH - 300:
        pipes.append(create_pipe())

    # Remove offscreen pipes
    if pipes[0][0] < -pipe_width:
        pipes.pop(0)
        score += 1

    # Collision
    for pipe in pipes:
        if pipe[0] < 60 < pipe[0] + pipe_width:
            if bird_y < pipe[1] or bird_y > pipe[2]:
                running = False

    if bird_y > HEIGHT or bird_y < 0:
        running = False

    # Drawing
    win.fill(WHITE)

    # Draw bird
    pygame.draw.circle(win, BIRD_COLOR, (60, int(bird_y)), 20)

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(win, PIPE_COLOR, (pipe[0], 0, pipe_width, pipe[1]))
        pygame.draw.rect(win, PIPE_COLOR, (pipe[0], pipe[2], pipe_width, HEIGHT))

    # Score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)

# Game Over
cap.release()
cv2.destroyAllWindows()
pygame.quit()
sys.exit()