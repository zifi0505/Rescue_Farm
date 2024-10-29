import pygame, sys, menu, random

def run_game():
    # Inicializar Pygame
    pygame.init()

    # Configurar la pantalla
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Colisión de Imágenes Aleatorias")

    # Cargar imágenes
    Mapa_Nivel1 = pygame.image.load("Mapa.png")
    Player_male = pygame.transform.scale(pygame.image.load("personajes/Boy.2.png"), (70, 70))
    Player_Female = pygame.transform.scale(pygame.image.load("personajes/1WOMAN.png"), (70, 70))
    Oveja_image = pygame.image.load("imagenes/animales/Oveja.png")

    LetrasEscala_X = 32
    LetrasEscala_Y = 32

    CAFE = (139, 69, 19)

    Letra_A = pygame.transform.scale(pygame.image.load("Letras/A.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_B = pygame.transform.scale(pygame.image.load("Letras/B.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_C = pygame.transform.scale(pygame.image.load("Letras/C.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_D = pygame.transform.scale(pygame.image.load("Letras/D.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_E = pygame.transform.scale(pygame.image.load("Letras/E.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_G = pygame.transform.scale(pygame.image.load("Letras/G.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_H = pygame.transform.scale(pygame.image.load("Letras/H.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_I = pygame.transform.scale(pygame.image.load("Letras/I.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_J = pygame.transform.scale(pygame.image.load("Letras/J.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_K = pygame.transform.scale(pygame.image.load("Letras/K.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_L = pygame.transform.scale(pygame.image.load("Letras/L.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_M = pygame.transform.scale(pygame.image.load("Letras/M.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_N = pygame.transform.scale(pygame.image.load("Letras/N.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_O = pygame.transform.scale(pygame.image.load("Letras/O.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_P = pygame.transform.scale(pygame.image.load("Letras/P.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_V = pygame.transform.scale(pygame.image.load("Letras/V-19-10-2024.png"), (LetrasEscala_X, LetrasEscala_Y))

    AInt = 0
    BInt = 0
    CInt = 0
    DInt = 0
    EInt = 0
    GInt = 0
    HInt = 0
    IInt = 0
    JInt = 0
    KInt = 0
    LInt = 0
    MInt = 0
    NInt = 0
    OInt = 0
    PInt = 0
    SInt = 0
    VInt = 0


    farmer_image = pygame.image.load("imagenes/Granjero (2).png")
    game_over_image = pygame.image.load("imagenes/Perder 8.png")
    win_image = pygame.image.load("imagenes/Ganar 8.png")  # Cargar la imagen de ganar
    Heart_Image = pygame.transform.scale(pygame.image.load("imagenes/CorazonDeVida.png"), (40, 40))


    # Posición inicial del jugador
    player_pos = [400, 520]

    # Lista para almacenar las ovejas
    targets = []
    Etargets = []
    Otargets = []
    Atargets = []
    Jtargets = []
    Vtargets = []

    PauseValue = False

    # Función para comprobar colisión
    def check_collision(pos1, size1, pos2, size2):
        return (pos1[0] < pos2[0] + size2[0] and
                pos1[0] + size1[0] > pos2[0] and
                pos1[1] < pos2[1] + size2[1] and
                pos1[1] + size1[1] > pos2[1])

    # Crea una fuente
    font = pygame.font.Font('fuentes/PressStart2P-Regular.ttf', 15)


    # Bucle principal
    Character = ""
    Status = "Characters"
    score = 0
    Timecounter = 40  # Tiempo inicial
    running = True
    farmer_pos = [280, 80] # Posición inicial del granjero
    farmer_direction = 1  # 1 para mover a la derecha, -1 para mover a la izquierda
    farmer_speed = 2  # Velocidad de movimiento del granjero

    # Límites de movimiento del granjero
    farmer_left_limit = 280  # Límite izquierdo
    farmer_right_limit = 670  # Límite derecho

    # Vida
    Life = 3

    # Velocidad de caida de las letras

    VelocidadDeCaida = 5

    # Tiempo de la última caída
    Last_A_Time = pygame.time.get_ticks()
    Last_V_Time = pygame.time.get_ticks()
    Last_E_Time = pygame.time.get_ticks()
    Last_J_Time = pygame.time.get_ticks()
    Last_O_Time = pygame.time.get_ticks()

    # Guardar el tiempo inicial
    
    start_ticks = pygame.time.get_ticks()  # Captura el tiempo de inicio

    font_8bit = pygame.font.Font("fuentes/PressStart2P-Regular.ttf", 17)

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)


    back_button = pygame.Rect(25, 500, 100, 100)
    back_button_image = pygame.transform.scale(pygame.image.load("imagenes/atras+.png"), (100, 100))

    while running:
    
        if Status == "Characters":
            screen.blit(pygame.transform.scale(pygame.image.load("imagenes/fondmenu.png"), (1000, 600)), (0, 0))
            pygame.draw.rect(screen, CAFE, pygame.Rect(200, 50, 600, 500), border_radius=15)


            FemaleCharacterButton = pygame.Rect(550, 250, 100, 100)
            pygame.draw.rect(screen, (63, 31, 8), FemaleCharacterButton, border_radius=15)

     
            mouse_pos = pygame.mouse.get_pos()

            MaleCharacterButton = pygame.Rect(375, 250, 100, 100)
            pygame.draw.rect(screen, ((63, 31, 8)), MaleCharacterButton, border_radius=15)



            if MaleCharacterButton.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (32, 16, 4), MaleCharacterButton, border_radius=15)  # Borde iluminado
            else:
                pygame.draw.rect(screen, (63, 31, 8), MaleCharacterButton, border_radius=15)
            if FemaleCharacterButton.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (32, 16, 4), FemaleCharacterButton, border_radius=15)  # Borde iluminado
            else:
                pygame.draw.rect(screen, (63, 31, 8), FemaleCharacterButton, border_radius=15)

            screen.blit(pygame.transform.scale(pygame.image.load("personajes/1WOMAN.png"), (100, 100)), (550, 250))

            screen.blit(pygame.transform.scale(pygame.image.load("personajes/Boy.2.png"), (100, 100)), (375, 250))

            screen.blit(back_button_image, (25, 500))

            pygame.draw.rect(screen, (63, 31, 8), pygame.Rect(300, 175, 400, 50), border_radius=15)
            draw_text('SELECT YOUT CHARACTER', font_8bit, (255, 255, 255), screen, 500, 200)

            

            pygame.display.flip()

            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:

                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if FemaleCharacterButton.collidepoint(event.pos):
                        Character = "Female"
                        Status = "Game"
                        print("Character has been choosen", Character)

                    if MaleCharacterButton.collidepoint(event.pos):
                        Character = "Male"
                        Status = "Game"
                        print("Character has been choosen", Character)

                    if back_button.collidepoint(event.pos):
                        menu.Menu_Run()


        
        if Status == "Game":
            # Mover el jugador con las teclas de flecha

            if PauseValue == False:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and player_pos[0] > 280:
                    player_pos[0] -= 5
                if keys[pygame.K_RIGHT] and player_pos[0] < 805:
                    player_pos[0] += 5
                if keys[pygame.K_UP]:
                    player_pos[1] = 535  # Resetear la posición vertical del jugador




            # Movimiento del granjero
            if PauseValue == False:
                farmer_pos[0] += farmer_direction * farmer_speed



            # Cambiar dirección al llegar a los límites
            if farmer_pos[0] >= farmer_right_limit or farmer_pos[0] <= farmer_left_limit:
                farmer_direction *= -1  # Cambiar dirección

            # Comprobar colisiones
            player_size = Player_male.get_size()
            Letra_A_Size = Letra_A.get_size()
            Letra_V_Size = Letra_V.get_size()
            Letra_E_Size = Letra_E.get_size()
            Letra_J_Size = Letra_J.get_size() 
            Letra_O_Size = Letra_O.get_size()

            # Verificar colisión entre jugador y ovejas
            for target in Atargets[:]:  # [:] para hacer una copia de la lista mientras iteramos
                if check_collision(player_pos, player_size, target[:2], Letra_V_Size):
                    score += 1
                    AInt += 1
                    if AInt >= 3:
                        Life -= 1
                    Atargets.remove(target)  # Eliminar oveja después de la colisión
            for target in Vtargets[:]:  # [:] para hacer una copia de la lista mientras iteramos
                if check_collision(player_pos, player_size, target[:2], Letra_V_Size):
                    score += 1
                    VInt += 1
                    if VInt >= 2:
                        Life -= 1
                    Vtargets.remove(target)
            for target in Etargets[:]:  # [:] para hacer una copia de la lista mientras iteramos
                if check_collision(player_pos, player_size, target[:2], Letra_E_Size):
                    score += 1
                    EInt += 1
                    if EInt >= 2:
                        Life -= 1
                    Etargets.remove(target)
            for target in Jtargets[:]:  # [:] para hacer una copia de la lista mientras iteramos
                if check_collision(player_pos, player_size, target[:2], Letra_J_Size):
                    score += 1
                    JInt += 1
                    if JInt >= 2:
                        Life -= 1
                    Jtargets.remove(target)
            for target in Otargets[:]:  # [:] para hacer una copia de la lista mientras iteramos
                if check_collision(player_pos, player_size, target[:2], Letra_O_Size):
                    score += 1
                    OInt += 1
                    if OInt >= 2:
                        Life -= 1
                    Otargets.remove(target)
            
            
            # Movel las letras hacia abajo
            if PauseValue == False:
                for target in Atargets:
                    target[1] += VelocidadDeCaida #Velocidad
                for target in Otargets:
                    target[1] += VelocidadDeCaida #Velocidad

                for target in Jtargets:
                    target[1] += VelocidadDeCaida #Velocidad
                for target in Vtargets:
                    target[1] += VelocidadDeCaida #Velocidad

                for target in Etargets:
                    target[1] += VelocidadDeCaida #Velocidad







            # Caída de ovejas (generación de nuevas ovejas cada 2 segundos)

            if PauseValue == False:
                current_time = pygame.time.get_ticks()
                if current_time - Last_A_Time > 1400:  # Cada 2 segundos
                    x = farmer_pos[0] + farmer_image.get_width() // 2  # Posición del granjero
                    Atargets.append([x, farmer_pos[1], True])  # Crear nueva oveja en la posición del granjero
                    Last_A_Time = current_time  # Reiniciar el temporizado
                if current_time - Last_V_Time > 5350:  # Cada 2 segundos
                    x = farmer_pos[0] + farmer_image.get_width() // 2  # Posición del granjero
                    Vtargets.append([x, farmer_pos[1], True])  # Crear nueva oveja en la posición del granjero
                    Last_V_Time = current_time 
                if current_time - Last_E_Time > 3500:  # Cada 2 segundos
                    x = farmer_pos[0] + farmer_image.get_width() // 2  # Posición del granjero
                    Etargets.append([x, farmer_pos[1], True])  # Crear nueva oveja en la posición del granjero
                    Last_E_Time = current_time 
                if current_time - Last_O_Time > 7700:  # Cada 2 segundos
                    x = farmer_pos[0] + farmer_image.get_width() // 2  # Posición del granjero
                    Otargets.append([x, farmer_pos[1], True])  # Crear nueva oveja en la posición del granjero
                    Last_O_Time = current_time 
                if current_time - Last_J_Time > 6600:  # Cada 2 segundos
                    x = farmer_pos[0] + farmer_image.get_width() // 2  # Posición del granjero
                    Jtargets.append([x, farmer_pos[1], True])  # Crear nueva oveja en la posición del granjero
                    Last_J_Time = current_time 
            



            # Actualizar el tiempo
            if PauseValue == False and Status == "Game":
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Tiempo en segundos
                Timecounter = 30 - seconds  # Calcular el tiempo restante

            # Comprobar condiciones de finalización
            if AInt < 1 and VInt < 1 and JInt < 1 and EInt < 1 and OInt < 1 and Timecounter <= 0 or Life == 0:
                screen.blit(game_over_image, (0, 0))  # Muestra la imagen de Game Over
                pygame.display.flip()
                pygame.time.wait(3000)  # Esperar 3 segundos antes de salir
                menu.Menu_Run()
            elif AInt >= 1 and VInt >= 1 and JInt >= 1 and EInt >= 1 and OInt >= 1:
                screen.blit(win_image, (0, 0))  # Muestra la imagen de Game Over
                screen.blit(Letra_V, (470, 30))
                screen.blit(Letra_O, (440, 30))
                screen.blit(Letra_E, (500, 30))
                screen.blit(Letra_J, (530, 30))
                screen.blit(Letra_A, (560, 30))
                pygame.display.flip()
                pygame.time.wait(3000)  # Esperar 3 segundos antes de salir
                menu.Menu_Run()
            
            

            # Dibujar todo
            screen.fill((0, 0, 0))  # Limpiar la pantalla
            screen.blit(Mapa_Nivel1, [0, 0])
            if Character == "Male":
                screen.blit(Player_male, player_pos)
            if Character == "Female":
                screen.blit(Player_Female, player_pos)
            
            screen.blit(farmer_image, farmer_pos)  # Dibujar el granjero

            
            if Life >= 3:
                screen.blit(Heart_Image, (72, 70))
            if Life >= 2:
                screen.blit(Heart_Image, (134, 70))
            if Life >= 1:
                screen.blit(Heart_Image, (196, 70))



            # Dibujar Letras
            for Letra_O_target in Otargets:
                screen.blit(Letra_O, Letra_O_target[:2])
            for Letra_E_target in Etargets:
                screen.blit(Letra_E, Letra_E_target[:2])     
            for Letra_V_target in Vtargets:
                screen.blit(Letra_V, Letra_V_target[:2])    
            for Letra_J_target in Jtargets:
                screen.blit(Letra_J, Letra_J_target[:2])     
            for Letra_A_target in Atargets:
                screen.blit(Letra_A, Letra_A_target[:2])   

            

            if VInt >= 1:
                screen.blit(Letra_V, (470, 30))
            if OInt >= 1:
                screen.blit(Letra_O, (440, 30))
            if EInt >= 1:
                screen.blit(Letra_E, (500, 30))
            if JInt >= 1:
                screen.blit(Letra_J, (530, 30))
            if AInt >= 1:
                screen.blit(Letra_A, (560, 30))

            # Mostrar puntaje y tiempo
    
            score_surface = font.render(f'A: {AInt:}, V: {VInt}, J: {JInt}, O: {OInt}, E: {EInt}', True, (255, 255, 255))
            time_surface = font.render(f'Time: 0:{int(Timecounter):02d}', True, (255, 255, 255))
            screen.blit(score_surface, (100, 30))  # Ajustar posición de puntaje
            screen.blit(time_surface, (850, 20))   # Ajustar posición de tiempo

            if PauseValue == False:
                Pause_Button = pygame.Rect(30, 30, 70, 70)
                pygame.draw.rect(screen, CAFE, Pause_Button, border_radius=15)
                screen.blit(pygame.transform.scale(pygame.image.load("imagenes/Pause button.png"), (70, 70)), (30, 30))
            else:
                Pause_Button = pygame.Rect(30, 30, 70, 70)
                screen.blit(pygame.transform.scale(pygame.image.load("imagenes/BotonEnPause.png"), (70, 70)), (30, 30))

            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Pause_Button.collidepoint(event.pos):
                        PauseValue = not PauseValue

        # Mostrar imagen de resultado

            
            pygame.display.flip()
            pygame.time.Clock().tick(60)

  