import pygame
import time


def options():

# Initialize Pygame
    pygame.init()

# Set up the windows
    input_window = pygame.display.set_mode((1300, 800))
    input_window_center = input_window.get_rect().center
    display_window = pygame.display.set_mode((1300, 800))

# Set up the font
    font = pygame.font.SysFont(None, 32)

# Set up the input box
    input_text = ""

# Set up the display box
    display_text = ""

# Game loop
    running = True
    clock = pygame.time.Clock()
    last_time = time.time()
    input_active = True
    words = []
    index = 0
    while running:
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    words = input_text.split()
                    input_text = ""
                    input_active = False
                    index = 0
                    display_text = ""
                elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                # Handle pasting from clipboard
                    clipboard_text = pygame.scrap.get(pygame.SCRAP_TEXT)
                    if clipboard_text:
                        input_text += clipboard_text.decode("utf-8")
                else:
                    input_text += event.unicode

    # Clear the windows
        input_window.fill((255, 255, 255))
        display_window.fill((255, 255, 255))

    # Render the input and display text
        input_render = font.render(input_text, True, (0, 0, 0))
        display_render = font.render(display_text, True, (0, 0, 0))
        input_window.blit(input_render, (10, 10))
        display_window.blit(display_render, (10, 100))

    # If input is complete, display the words
        if not input_active:
            current_time = time.time()
            if current_time - last_time > 0.1 and index < len(words):
                display_text += words[index] + " "
                index += 1
                last_time = current_time
            elif index >= len(words):
                input_active = True

    # Update the display
        pygame.display.update()

    # Set the frame rate
        clock.tick(20)

# Quit Pygame
    pygame.quit()
