import pygame, sys, Nivel1  
# Inicializar Pygame

# Tamaño de pantalla
def Menu_Run():
    
    pygame.init()
    screen_width, screen_height = 1000, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("RESCUE FARM")

    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    CAFE = (139, 69, 19)
    HIGHLIGHT_VERDE = (0, 255, 0)#Color para resaltar en verde
    HIGHLIGHT_AMARILLO =(255, 255,  0)#Color para resaltar en  amarillo


    # Fuente estilo 8 bits (debes descargar la fuente y colocarla en la misma carpeta)
    font_8bit = pygame.font.Font("fuentes/PressStart2P-Regular.ttf", 30)

    #icono
    icono = pygame.image.load("imagenes/icono.jpeg")    
    pygame.display.set_icon(icono)

    # Cargar la imagen del fondo
    background_image = pygame.image.load("imagenes/fondmenu.png")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Movimiento del fondo
    bg_x1 = 0  # posición inicial del primer fondo
    bg_x2 = screen_width  # posición inicial del segundo fondo

    # Velocidad del fondo
    bg_speed = 2

    # Cargar la imagen del botón "Regresar."
    back_button_image = pygame.image.load("imagenes/atras+.png")
    back_button_image = pygame.transform.scale(back_button_image, (100, 100))  # Ajustar según necesites

    # SONIDO DEL MENU
    pygame.mixer.music.load("MUSICA/musicmenu.ogg")
    pygame.mixer.music.play(-1)
    button_click_sound = pygame.mixer.Sound("MUSICA/botonPress.mp3")


    # Estados del juego
    MENU = "menu"
    DIFFICULTY = "difficulty"
    LEVEL = "level"
    state = MENU

    # Botones
    button_width, button_height = 300, 50


    # Función para dibujar texto centrado
    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

    # Bucle principal del juego
    running = True
    difficulty = None


    while running:
        # Dibujar el fondo en movimiento
        screen.blit(background_image, (bg_x1, 0))
        screen.blit(background_image, (bg_x2, 0))

    # Actualizar la posición del fondo
        bg_x1 -= bg_speed
        bg_x2 -= bg_speed

        # Reiniciar la posición del fondo cuando salga de la pantalla
        if bg_x1 <= -screen_width:
            bg_x1 = screen_width
        if bg_x2 <= -screen_width:
            bg_x2 = screen_width

        mouse_pos = pygame.mouse.get_pos()

        if state == MENU:
            # Dibujar el título del menú
            draw_text('RESCUE FARM', font_8bit, BLACK, screen, screen_width // 2, 100)
            
            # Dibujar el botón "Jugar"
            play_button = pygame.Rect(screen_width // 2 - button_width // 2, 250, button_width, button_height)
            pygame.draw.rect(screen, CAFE, play_button, border_radius=15)
            
            #iluminacion de boton jugar    
            if play_button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, HIGHLIGHT_VERDE, play_button, border_radius=15)  # Borde iluminado
            else:
                pygame.draw.rect(screen, CAFE, play_button, border_radius=15)
                
            draw_text('JUGAR', font_8bit, WHITE, screen, screen_width // 2, 275)

            # Detección de clic en el botón
        
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        button_click_sound.play() #reproduce el sonido de click del boton jugar
                        state = DIFFICULTY

        elif state == DIFFICULTY:
            # Mostrar selección de dificultad
            draw_text('SELECCIONA DIFICULTAD', font_8bit, BLACK, screen, screen_width // 2, 100)

            easy_button = pygame.Rect(screen_width // 2 - button_width // 2, 250, button_width, button_height)
            hard_button = pygame.Rect(screen_width // 2 - button_width // 2, 350, button_width, button_height)
            back_button = pygame.Rect(25, 500, 100, 100)  # Posición y tamaño del botón "Regresar"
        
        # Iluminar el  botón "Fácil"
            if easy_button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, HIGHLIGHT_AMARILLO, easy_button, border_radius=15)
            else:
                pygame.draw.rect(screen, CAFE, easy_button, border_radius=15)
            
            # Iluminar el botón "Avanzado"
            if hard_button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, HIGHLIGHT_AMARILLO, hard_button, border_radius=15)
            else:
                pygame.draw.rect(screen, CAFE, hard_button, border_radius=15)
            draw_text('FACIL', font_8bit, WHITE, screen, screen_width // 2, 275)
            draw_text('AVANZADO', font_8bit, WHITE, screen, screen_width // 2, 375)

            # Dibujar la imagen del botón "Regresar"
            screen.blit(back_button_image, (25, 500))

            # Detectar clic de dificultad
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.collidepoint(event.pos):
                        button_click_sound.play()
                        difficulty = "facil"
                        state = LEVEL
                    elif hard_button.collidepoint(event.pos):
                        button_click_sound.play()
                        difficulty = "avanzado"
                        state = LEVEL
                    elif back_button.collidepoint(event.pos):
                        button_click_sound.play()
                        state = MENU  # Regresar al menú principal

        elif state == LEVEL:
            # Mostrar selección de niveles
            draw_text('SELECCIONA UN NIVEL', font_8bit, BLACK, screen, screen_width // 2, 100)

            level1_button = pygame.Rect(screen_width // 2 - button_width // 2, 200, button_width, button_height)
            level2_button = pygame.Rect(screen_width // 2 - button_width // 2, 300, button_width, button_height)
            level3_button = pygame.Rect(screen_width // 2 - button_width // 2, 400, button_width, button_height)
            back_button = pygame.Rect(25, 500, button_width, button_height)

            if level1_button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, HIGHLIGHT_AMARILLO, level1_button, border_radius=15)
            else:
                pygame.draw.rect(screen, CAFE, level1_button, border_radius=15)

            if level2_button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, HIGHLIGHT_AMARILLO, level2_button, border_radius=15)
            else:
                pygame.draw.rect(screen, CAFE, level2_button, border_radius=15)

            if level3_button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, HIGHLIGHT_AMARILLO, level3_button, border_radius=15)
            else:
                pygame.draw.rect(screen, CAFE, level3_button, border_radius=15)
        
            
            
            # Dibujar la imagen del botón "Regresar"
            screen.blit(back_button_image, (50, 500))
            draw_text('NIVEL 1', font_8bit, WHITE, screen, screen_width // 2, 225)
            draw_text('NIVEL 2', font_8bit, WHITE, screen, screen_width // 2, 325)
            draw_text('NIVEL 3', font_8bit, WHITE, screen, screen_width // 2, 425)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if level1_button.collidepoint(event.pos):
                        button_click_sound.play()
                        print(f"Nivel 1 seleccionado en dificultad {difficulty}")
                        Nivel1.run_game()  # Ejecuta el juego principal al seleccionar el nivel 1
                        pygame.quit()    # Cierra el menú después de iniciar el juego
                        sys.exit()
                    elif level2_button.collidepoint(event.pos):
                        button_click_sound.play()
                        Nivel1.run_game()
                        print(f"Nivel 2 seleccionado en dificultad {difficulty}")
                    elif level3_button.collidepoint(event.pos):
                        button_click_sound.play()
                        Nivel1.run_game()
                        print(f"Nivel 3 seleccionado en dificultad {difficulty}")
                    elif back_button.collidepoint(event.pos):
                        button_click_sound.play()
                    if state == LEVEL:
                        state = DIFFICULTY  # Regresar a la selección de dificultad
                
        pygame.display.flip()
        pygame.time.Clock().tick(60)

Menu_Run()