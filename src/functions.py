def create_block(left = 0, top = 0, width = 50, height = 50, colour = (255, 255, 255),
                direction = 3, edge = 0, radius = -1, speed_x = 5, speed_y = 5, img = None):
    import pygame
    if img:
        img = pygame.transform.scale(img, (width, height))
    rect = pygame.Rect(left, top, width, height)
    return {"rect": rect, "color": colour, "dir": direction, "edge": edge, "radius": radius, "speed_x": speed_x, "speed_y": speed_y, "img": img}

# def handler_new_coin():
#     coins.append((create_block(randint(0, WIDTH - size_coin), randint(0, HEIGHT - 
#             size_coin), size_coin, size_coin, BLUE, radius = size_coin // 2)))

def show_text(superficie, text, font, coordenadas, colour_font, color_fondo = None):
    sup_text = font.render(text, True, colour_font, color_fondo)
    rect_text = sup_text.get_rect()
    rect_text.center = coordenadas
    superficie.blit(sup_text, rect_text)

def finish():
    import pygame, sys
    pygame.quit()
    sys.exit()

def wait_user():
    import pygame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    finish()
                return


def show_text_button(surface, text, x, y, font_size = 36, colour = (0, 0, 0)):
    import pygame
    font = pygame.font.SysFont("comicsans", font_size)
    render = font.render(text, True, colour)
    rect_text = render.get_rect(center = (x, y))
    surface.blit(render, rect_text)

def create_button(screen, rect, text: str, colour_button: tuple, colour_hover: tuple):
    import pygame
    mouse_position = pygame.mouse.get_pos()
    if rect.collidepoint(mouse_position):
        pygame.draw.rect(screen, colour_hover, rect, border_radius=10)
    else:
        pygame.draw.rect(screen, colour_button, rect, border_radius=10)
    show_text_button(screen, text, rect.centerx, rect.centery)

def initial_menu(rect_1, screen, colour, colour_hover, text, rect_2, text2, colour2, colour_hover2):
    import pygame
    while True:
        create_button(screen, rect_1, text, colour, colour_hover)
        create_button(screen, rect_2, text2, colour2, colour_hover2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_1.collidepoint(event.pos):
                        return None
                    elif rect_2.collidepoint(event.pos):
                        finish()

def handler_new_coin(list, width_screen, height_screen, size_coin, colour, img):
    from random import randint
    list.append((create_block(randint(0, width_screen - size_coin), randint(0, height_screen - 
            size_coin), size_coin, size_coin, colour, radius = size_coin // 2, img= img)))

