import pygame
import pygame_gui
import openai

# Konfiguracja API OpenAI
openai.api_key = "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"
messages = [{"role": "system", "content": "You are a kind helpful assistant."}]

# Inicjalizacja Pygame
pygame.init()
pygame.display.set_caption('ChatGPT')

# Konfiguracja ekranu
screen = pygame.display.set_mode((800, 600))
background_color = pygame.Color('#FFFFFF')
screen.fill(background_color)

# Konfiguracja menedżera UI
ui_manager = pygame_gui.UIManager((800, 600))

# Tworzenie pola tekstowego dla wpisywania wiadomości
user_text_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((50, 50), (700, 50)),
    manager=ui_manager
)

# Tworzenie pola tekstowego dla wyświetlania odpowiedzi
chat_output = pygame_gui.elements.UITextBox(
    html_text='',
    relative_rect=pygame.Rect((50, 150), (700, 350)),
    manager=ui_manager
)

# Tworzenie przycisku "Send"
send_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((650, 500), (100, 50)),
    text='Send',
    manager=ui_manager
)

# Pętla główna
clock = pygame.time.Clock()
is_running = True
while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == send_button:
                    message = user_text_input.text
                    if message:
                        messages.append({"role": "user", "content": message})
                        chat = openai.ChatCompletion.create(model="text-davinci-002", messages=messages)
                        reply = chat.choices[0].text
                        chat_output.html_text += f"<b>User:</b> {message}<br>"
                        chat_output.html_text += f"<b>ChatGPT:</b> {reply}<br>"
                        messages.append({"role": "assistant", "content": reply})
                        user_text_input.set_text('')
                        
        ui_manager.process_events(event)

    ui_manager.update(time_delta)
    screen.fill(background_color)
    ui_manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()