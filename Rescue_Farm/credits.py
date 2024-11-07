import pygame, sys, menu

def creditsWall():
    pygame.init()
    font_8bit = pygame.font.Font("fuentes/PressStart2P-Regular.ttf", 17)

    screen = pygame.display.set_mode((1000, 600))
    Running = True
    AlturaY = [100, 200, 300, 400, 500, 600]

    back_button_image = pygame.transform.scale(pygame.image.load("imagenes/atras+.png"), (100, 100))

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

    Velocidad = 1

    Altura1 = 500
    Altura2 = 600
    Altura3 = 700
    Altura4 = 800
    Altura5 = 900
    Altura6 = 1000
    Altura7 = 1100
    Altura8 = 1200
    Altura9 = 1300
    Altura10 = 1400
    Altura11 = 1500
    Altura12 = 1600

    while Running:

        Altura1 -= Velocidad
        Altura2 -= Velocidad
        Altura3 -= Velocidad
        Altura4 -= Velocidad
        Altura5 -= Velocidad
        Altura6 -= Velocidad
        Altura7 -= Velocidad
        Altura8 -= Velocidad
        Altura9 -= Velocidad
        Altura10 -= Velocidad
        Altura11 -= Velocidad
        Altura12 -= Velocidad

        screen.blit(pygame.image.load("Mapa.png"), (0, 0))

        back_button = pygame.Rect(25, 500, 100, 100)

        screen.blit(back_button_image, (25, 500))

        draw_text('Lider del proyecto', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura1)
        draw_text('Zifei Mei Chen', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura2)

        draw_text('Programador', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura3)
        draw_text('Miguel Arturo Parra Garzón', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura4)

        draw_text('Programacion y Diseño', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura5)
        draw_text('Victor Manuel Carrillo Barajas', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura6)

        draw_text('Diseño', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura7)
        draw_text('Nahomi Jaizibeth Casillas Molina', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura8)

        draw_text('Programacion y Diseño', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura9)
        draw_text('Aram Sebastian Dimas Rolon', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura10)

        draw_text('Compositor de sonidos y Guinista', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura11)
        draw_text('Maximiliano Martinez Gomez', font_8bit, (255, 255, 255), screen, 1000 // 2, Altura12)

        
        

    


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    menu.Menu_Run()


        pygame.display.flip()
        pygame.time.Clock().tick(60)