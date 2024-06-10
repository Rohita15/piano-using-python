import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Define the dimensions of the window
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Virtual Piano")

# Load piano sounds
sounds = {}
for key, filename in {
    pygame.K_a: "A.wav",
    pygame.K_s: "B.wav",
    pygame.K_d: "C.wav",
    pygame.K_f: "D.wav",
    pygame.K_g: "E.wav",
    pygame.K_h: "F.wav",
    pygame.K_j: "G.wav",
    pygame.K_k: "H.wav",
}.items():
    if os.path.exists(filename):
        sounds[key] = pygame.mixer.Sound(filename)
    else:
        print(f"Warning: File {filename} not found.")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in sounds:
                sounds[event.key].play()
        elif event.type == pygame.KEYUP:
            if event.key in sounds:
                sounds[event.key].stop()

    window.fill((255, 255, 255))
    pygame.display.flip()
