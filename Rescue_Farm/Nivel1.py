import pygame, sys, menu

def run_game():
    # Inicializar Pygame
    pygame.init()

    # Configurar la pantalla
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Colisión de Imágenes Aleatorias")

    # Cargar imágenes
    Mapa_Nivel1 = pygame.image.load("Mapatest.jpg")
    player_image = pygame.image.load("personajes/Boy.2.png")
    Oveja_image = pygame.image.load("imagenes/animales/Oveja.png")

    Letra_A = pygame.image.load("Letras/A.png")      
    Letra_B = pygame.image.load("Letras/B.png")
    Letra_C = pygame.image.load("Letras/C.png")
    Letra_D = pygame.image.load("Letras/D.png")
    Letra_E = pygame.image.load("Letras/E.png")
    Letra_G = pygame.image.load("Letras/G.png")
    Letra_H = pygame.image.load("Letras/H.png")
    Letra_I = pygame.image.load("Letras/I.png")
    Letra_J = pygame.image.load("Letras/J.png")
    Letra_K = pygame.image.load("Letras/K.png")
    Letra_L = pygame.image.load("Letras/L.png")
    Letra_M = pygame.image.load("Letras/M.png")
    Letra_N = pygame.image.load("Letras/N.png")
    Letra_O = pygame.image.load("Letras/O.png")
    Letra_P = pygame.image.load("Letras/P.png")


    farmer_image = pygame.image.load("imagenes/Granjero (2).png")
    game_over_image = pygame.image.load("imagenes/gameOver.png")
    win_image = pygame.image.load("imagenes/win.png")  # Cargar la imagen de ganar
    Heart_Image = pygame.image.load("imagenes/CorazonDeVida.png")

    # Posición inicial del jugador
    player_pos = [400, 535]

    # Lista para almacenar las ovejas
    targets = []

    # Función para comprobar colisión
    def check_collision(pos1, size1, pos2, size2):
        return (pos1[0] < pos2[0] + size2[0] and
                pos1[0] + size1[0] > pos2[0] and
                pos1[1] < pos2[1] + size2[1] and
                pos1[1] + size1[1] > pos2[1])

    # Crea una fuente
    font = pygame.font.Font('fuentes/PressStart2P-Regular.ttf', 15)

    # Bucle principal
    score = 0
    Timecounter = 40  # Tiempo inicial
    running = True
    farmer_pos = [280, 80] # Posición inicial del granjero
    farmer_direction = 1  # 1 para mover a la derecha, -1 para mover a la izquierda
    farmer_speed = 2  # Velocidad de movimiento del granjero

    # Límites de movimiento del granjero
    farmer_left_limit = 280  # Límite izquierdo
    farmer_right_limit = 790  # Límite derecho

    # Vida
    Life = 3

    # Tiempo de la última caída
    last_sheep_time = pygame.time.get_ticks()

    # Guardar el tiempo inicial
    start_ticks = pygame.time.get_ticks()  # Captura el tiempo de inicio

    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        # Mover el jugador con las teclas de flecha
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 280:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT] and player_pos[0] < 805:
            player_pos[0] += 5
        if keys[pygame.K_UP]:
            player_pos[1] = 535  # Resetear la posición vertical del jugador

        # Movimiento del granjero
        farmer_pos[0] += farmer_direction * farmer_speed



        # Cambiar dirección al llegar a los límites
        if farmer_pos[0] >= farmer_right_limit or farmer_pos[0] <= farmer_left_limit:
            farmer_direction *= -1  # Cambiar dirección

        # Comprobar colisiones
        player_size = player_image.get_size()
        Oveja_size = Oveja_image.get_size()

        # Verificar colisión entre jugador y ovejas
        for target in targets[:]:  # [:] para hacer una copia de la lista mientras iteramos
            if check_collision(player_pos, player_size, target[:2], Oveja_size):
                score += 1
                targets.remove(target)  # Eliminar oveja después de la colisión

        # Mover las ovejas hacia abajo
        for target in targets:
            target[1] += 5 # Caída de las ovejas (puedes ajustar la velocidad aquí)
            if target[1] == 590:
                Life -= 1



        # Caída de ovejas (generación de nuevas ovejas cada 2 segundos)
        current_time = pygame.time.get_ticks()
        if current_time - last_sheep_time > 2000:  # Cada 2 segundos
            x = farmer_pos[0] + farmer_image.get_width() // 2  # Posición del granjero
            targets.append([x, farmer_pos[1], True])  # Crear nueva oveja en la posición del granjero
            last_sheep_time = current_time  # Reiniciar el temporizador

        
        print(pygame.mouse.get_pos())

        # Actualizar el tiempo
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Tiempo en segundos
        Timecounter = 30 - seconds  # Calcular el tiempo restante

        # Comprobar condiciones de finalización
        if score < 10 and Timecounter <= 0 or Life == 0:
            screen.blit(game_over_image, (0, 0))  # Muestra la imagen de Game Over
            pygame.display.flip()
            pygame.time.wait(3000)  # Esperar 3 segundos antes de salir
            menu.Menu_Run()
        elif score >= 10:
            screen.blit(win_image, (0, 0))  # Muestra la imagen de Game Over
            pygame.display.flip()
            pygame.time.wait(3000)  # Esperar 3 segundos antes de salir
            menu.Menu_Run()
        
        

        # Dibujar todo
        screen.fill((0, 0, 0))  # Limpiar la pantalla
        screen.blit(Mapa_Nivel1, [0, 0])
        screen.blit(player_image, player_pos)
        screen.blit(farmer_image, farmer_pos)  # Dibujar el granjero

        
        if Life >= 3:
            screen.blit(pygame.image.load("imagenes/CorazonDeVida.png"), (62, 50))
        if Life >= 2:
            screen.blit(pygame.image.load("imagenes/CorazonDeVida.png"), (176, 50))
        if Life >= 1:
            screen.blit(pygame.image.load("imagenes/CorazonDeVida.png"), (290, 50))



        # Dibujar ovejas
        for target in targets:
            screen.blit(Oveja_image, target[:2])  # Dibuja la oveja en su posición actual

        # Mostrar puntaje y tiempo
        score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
        time_surface = font.render(f'Time: {int(Timecounter)}', True, (255, 255, 255))
        life_surface = font.render(f'Lifes: {int(Life)}', True, (255, 255, 255))
        screen.blit(score_surface, (100, 50))  # Ajustar posición de puntaje
        screen.blit(time_surface, (870, 20))   # Ajustar posición de tiempo
        screen.blit(life_surface, (100, 80))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # Mostrar imagen de resultado

    

    if score >= 10:
        screen.blit(win_image, (0, 0))  # Muestra la imagen de ganar
        menu.Menu_Run
    else: 
        screen.blit(game_over_image, (0, 0))  # Muestra la imagen de Game Over
    
        pygame.display.flip()
        pygame.time.wait(3000)  # Esperar 3 segundos antes de salir

        menu.Menu_Run()
