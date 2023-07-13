
import pygame, sys, time
from button import Button
pygame.init()


SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background2.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)
                    
def play():
	
    pygame.init()

    # Ustawienie wymiarów okna
    width = 1300
    height = 800
    screen = pygame.display.set_mode((width, height))

    # Ustawienie tytułu okna
    pygame.display.set_caption("Akronim")

    # Ustawienie tekstu
    font = pygame.font.SysFont('Arial', 36)
    text_input = ""
    text_output = ""

    # Główna pętla gry
    running = True
    while running:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                # Dodanie wprowadzonego tekstu do zmiennej text_input
                if event.key == pygame.K_RETURN:
                    text_output = "  ".join(word[0].upper() for word in text_input.split())
                    text_input = ""
                else:
                    text_input += event.unicode

        # Wyświetlanie tekstu
        screen.fill((0, 0, 0))
        input_surface = font.render(text_input, True, (255, 255, 255))
        output_surface = font.render(text_output, True, (255, 255, 255))

        # Justowanie tekstu na środku
        input_rect = input_surface.get_rect()
        input_rect.center = (width // 2, height // 2 - 50)
        output_rect = output_surface.get_rect()
        output_rect.center = (width // 2, height // 2 + 50)

        screen.blit(input_surface, input_rect)
        screen.blit(output_surface, output_rect)
        pygame.display.flip()


    # if __name__ == '__main__':
    #     play()

    pygame.display.update()
    
def options():
    

    pygame.init()

# Definicja kolorów
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

# Definicja rozmiaru ekranu
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

# Definicja rozmiaru czcionki
    FONT_SIZE = 24

# Inicjalizacja ekranu
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Inicjalizacja czcionki
    font = pygame.font.Font(None, FONT_SIZE)

# Tekst wejściowy
    input_text = ""

# Tabela
    table = []

# Główna pętla gry
    while True:
    # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                # Rozdzielenie tekstu na słowa
                    words = input_text.split()
                # Tworzenie tabeli z rozdzielonymi słowami
                    table = [words[i:i+6] for i in range(0, len(words), 6)]
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Wypełnienie ekranu kolorem białym
        screen.fill(WHITE)

    # Rysowanie tabeli z rozdzielonymi słowami
        if table:
            x, y = 50, 50
            for row in table:
                for word in row:
                    text_surface = font.render(word, True, BLACK)
                    text_rect = text_surface.get_rect()
                    text_rect.topleft = (x, y)
                    screen.blit(text_surface, text_rect)
                    x += text_rect.width + 10
                x = 50
                y += text_rect.height + 10

    # Rysowanie tekstu wprowadzanego przez użytkownika
        text_surface = font.render(input_text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, SCREEN_HEIGHT - text_rect.height - 50)
        screen.blit(text_surface, text_rect)
        # Rysowanie tabeli z rozdzielonymi słowami
        if table:
            x, y = 50, 50
            for row in table:
                for i, word in enumerate(row):
                    if i in (0, 1, 4, 5):  # columns 1, 2, 5, and 6
                        color = GRAY
                    else:
                        color = BLACK
                    text_surface = font.render(word, True, color)
                    text_rect = text_surface.get_rect()
                    text_rect.topleft = (x, y)
                    screen.blit(text_surface, text_rect)
                    x += text_rect.width + 10
                x = 50
                y += text_rect.height + 10
    # Rysowanie linii oddzielającej wprowadzany tekst od tabeli
        pygame.draw.line(screen, GRAY, (0, SCREEN_HEIGHT - 50), (SCREEN_WIDTH, SCREEN_HEIGHT - 50), 2)
    # Aktualizacja ekranu
        pygame.display.update()




def rozjasnienie():

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
    main_menu()


def main_menu():
    while True:
        SCREEN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("PRZECZYTANE", True, "#910369")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 40))

        PLAY_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 175), 
                            text_input="AKRONIM (prosze nie)", font=get_font(32), base_color="#f2edf1", hovering_color="#043302")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 425), 
                            text_input="PERYFERIE(hell nah)", font=get_font(35), base_color="#f2edf1", hovering_color="#043302")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 600), 
                            text_input="WYJŚCIE", font=get_font(200), base_color="#a60c11", hovering_color="#2fff05")
        funkcja_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 300), 
                            text_input="ROZJAŚNIENIE", font=get_font(35), base_color="#f2edf1", hovering_color="#043302")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, funkcja_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if funkcja_BUTTON.checkForInput(MENU_MOUSE_POS):
                    rozjasnienie()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()

main_menu()