# Bubble Pop: tap the bubbles before they float away. 30 seconds.
import math
import random
import sys
import time

import pygame

pygame.init()
W, H = 400, 700
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
small = pygame.font.Font(None, 28)
COLOURS = [(167, 188, 91), (108, 168, 255), (199, 146, 234), (242, 193, 78), (94, 209, 201)]

bubbles = []
score = 0
start = time.time()
pops = []  # little rings where a bubble burst

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            left = 30 - (time.time() - start)
            if left <= 0:
                bubbles, score, start, pops = [], 0, time.time(), []
                continue
            for b in reversed(bubbles):
                if math.dist(event.pos, (b["x"], b["y"])) < b["r"]:
                    bubbles.remove(b)
                    score += 1
                    pops.append({"x": b["x"], "y": b["y"], "r": b["r"], "t": 0, "c": b["c"]})
                    break

    left = 30 - (time.time() - start)
    if left > 0 and random.random() < 0.06:
        r = random.randint(22, 42)
        bubbles.append({"x": random.randint(r, W - r), "y": H + r, "r": r, "v": random.uniform(1.5, 3.5),
                        "c": random.choice(COLOURS), "wob": random.uniform(0, 6.28)})
    for b in bubbles[:]:
        b["y"] -= b["v"]
        b["wob"] += 0.05
        if b["y"] < -b["r"]:
            bubbles.remove(b)

    screen.fill((13, 8, 22))
    for b in bubbles:
        x = b["x"] + math.sin(b["wob"]) * 6
        pygame.draw.circle(screen, b["c"], (int(x), int(b["y"])), b["r"], 3)
        pygame.draw.circle(screen, (255, 255, 255), (int(x - b["r"] / 3), int(b["y"] - b["r"] / 3)), max(3, b["r"] // 6))
    for p in pops[:]:
        p["t"] += 1
        pygame.draw.circle(screen, p["c"], (int(p["x"]), int(p["y"])), p["r"] + p["t"] * 2, 2)
        if p["t"] > 10:
            pops.remove(p)

    screen.blit(font.render(f"{score}", True, (243, 245, 249)), (20, 18))
    screen.blit(small.render(f"{max(0, left):.0f}s", True, (163, 155, 181)), (W - 60, 24))
    if left <= 0:
        msg = font.render(f"Time! You popped {score}", True, (243, 245, 249))
        screen.blit(msg, msg.get_rect(center=(W // 2, H // 2)))
        hint = small.render("Tap to play again", True, (167, 188, 91))
        screen.blit(hint, hint.get_rect(center=(W // 2, H // 2 + 40)))
    pygame.display.update()
    clock.tick(60)
