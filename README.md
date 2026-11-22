# Bubble Pop

pygame game. Tap the bubbles before they float off the top. You have 30 seconds; tap again to replay.

- **Play:** tap or click. No keyboard needed.
- **On desktop:** `pip install pygame` then `python main.py`.

**Tests in Olive:** the game loop is a `while True:` at the **top level of the file** (no function), it exits
with `sys.exit()`, and it uses `pygame.display.update()` instead of `flip()`. It only uses touch, so **no
on-screen buttons** should appear.
