import pygame, os
from random import randint
from config import *
from colisiones import *
from functions import *


# inicializar los modulos de pygame
pygame.init()

#configuracion pantalla principal
screen = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Froggy")

#creo un reloj
clock = pygame.time.Clock()

# cargo imagenes

# backgrounds
background = pygame.transform.scale(pygame.image.load("./src/assets/street.jpg"), SIZE_SCREEN)
background_menu = pygame.transform.scale(pygame.image.load("./src/assets/background_menu.jpg"), SIZE_SCREEN)
background_game_over = pygame.transform.scale(pygame.image.load("./src/assets/dead.png"), SIZE_SCREEN)
icon = pygame.transform.scale(pygame.image.load("./src/assets/icon.png"), SIZE_SCREEN)

pygame.display.set_icon(icon)

# car
enemy_car = pygame.transform.scale(pygame.image.load("./src/assets/car.png"), CAR_SIZE)
rect_enemy_car = enemy_car.get_rect()
mask_enemy_car = pygame.mask.from_surface(enemy_car)

# coin
image_coin = pygame.transform.scale(pygame.image.load("./src/assets/coin.png"), (COIN_SIZE, COIN_SIZE))
rect_image_coin = image_coin.get_rect()
mask_image_coin = pygame.mask.from_surface(image_coin)

# slow_coin
image_slow_coin = pygame.transform.scale(pygame.image.load("./src/assets/slow_coin.png"), (COIN_SIZE, COIN_SIZE))
rect_image_slow_coin = image_slow_coin.get_rect()
mask_image_slow_coin = pygame.mask.from_surface(image_slow_coin)

# truck
enemy_truck = pygame.transform.scale(pygame.image.load("./src/assets/truck.png"), TRUCK_SIZE)
rect_enemy_truck = enemy_truck.get_rect()
mask_enemy_truck = pygame.mask.from_surface(enemy_truck)

# motorcycle
enemy_motorcycle = pygame.transform.scale(pygame.image.load("./src/assets/motorcycle.png"), MOTORCYCLE_SIZE)
rect_enemy_motorcycle = enemy_motorcycle.get_rect()
mask_enemy_motorcycle = pygame.mask.from_surface(enemy_motorcycle)

# player
image_player = pygame.transform.scale(pygame.image.load("./src/assets/frog.png"), (BLOCK_WIDTH , BLOCK_HEIGHT))
rect_image_player = image_player.get_rect()
mask_player = pygame.mask.from_surface(image_player)

# cargo audio
coin_sound = pygame.mixer.Sound("./src/assets/mario-coin.mp3")
coin_sound.set_volume(0.3)
pum_sound = pygame.mixer.Sound("./src/assets/PUM.mp3")
pum_sound.set_volume(0.3)
dead_sound = pygame.mixer.Sound("./src/assets/sad.mp3")
dead_sound.set_volume(0.3)
background_sound = pygame.mixer.Sound("./src/assets/background_sound.mp3")
background_sound.set_volume(0.3)


# seteo fuente
font = pygame.font.SysFont(None, 48)

# texto vida
text_life = font.render(f"hearts: {hearts}", True, BLACK)
rect_text_life = text_life.get_rect()
rect_text_life.midleft = (0, 30)

# texto monedas

text_score = font.render(f"Score: {score}", True, BLACK)
rect_text_score = text_score.get_rect()
rect_text_score.midright = (WIDTH, (0 + rect_text_score.height))


# frog
block = create_block(BLOCK_LEFT, BLOCK_TOP, width=BLOCK_WIDTH, height=BLOCK_HEIGHT,colour=GREEN, img= image_player)

# autos
cars = []
for car in range(number_of_cars):
    car = create_block(randint(0, WIDTH), randint(0, (HEIGHT - BLOCK_HEIGHT)),
                        width = CAR_SIZE[0], height = CAR_SIZE[1], colour = RED, img= enemy_car)
    cars.append(car)

# motos
motorcycles = []
for motorcycle in range(number_of_motorcylces):
    motorcycle = create_block(randint(0, WIDTH), randint(0, (HEIGHT - BLOCK_HEIGHT)),width = MOTORCYCLE_SIZE[0],
                                height = MOTORCYCLE_SIZE[1], colour = MAGENTA, img= enemy_motorcycle)
    motorcycles.append(motorcycle)

# camiones
trucks = []
for truck in range(number_of_trucks):
    truck = create_block(randint(0, WIDTH), randint(0, (HEIGHT - BLOCK_HEIGHT)),width = TRUCK_SIZE[0],
                            height = TRUCK_SIZE[1], colour = LIGHT_BLUE, img= enemy_truck)
    trucks.append(truck)

# monedas
coins = []

# monedas especiales
slow_coins = []

# evento personalizado
EVENT_NEW_COIN = pygame.USEREVENT + 1

pygame.time.set_timer(EVENT_NEW_COIN, 3000)


# bottones
start_button = pygame.Rect(CENTER_SCREEN[0] - BUTTON_WIDTH // 2, 350, BUTTON_WIDTH, BUTTON_HEIGHT)
quit_button = pygame.Rect(CENTER_SCREEN[0] - BUTTON_WIDTH // 2, 450, BUTTON_WIDTH, BUTTON_HEIGHT)

# dict
directory = os.getcwd()
completely_path = os.path.join(directory, "max_score.txt")



while True:
    screen.blit(background_menu, background_menu.get_rect())
    background_sound.play(-1)
    show_text(screen, "FROGGY", font, (WIDTH//2, 220), GREEN)
    initial_menu(start_button, screen, GREEN, GREEN_PERSONALIZED, "New game", quit_button, "Quit", GREEN, GREEN_PERSONALIZED)
    score = 0
    hearts = 5
    pygame.display.flip()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            if event.type == EVENT_NEW_COIN:
                handler_new_coin(coins, WIDTH, (HEIGHT - BLOCK_HEIGHT), COIN_SIZE, YELLOW, image_coin)
                print("nueva moneda")
            if event.type == EVENT_NEW_COIN:
                handler_new_coin(slow_coins, WIDTH, (HEIGHT - BLOCK_HEIGHT), COIN_SIZE, BLUE, image_slow_coin)
                print("MONEDA ESPECIAL")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    move_right = True
                elif event.key == pygame.K_a:
                    move_left = True
                elif event.key == pygame.K_w:
                    move_up = True
                elif event.key == pygame.K_s:
                    move_down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    move_right = False
                elif event.key == pygame.K_a:
                    move_left = False
                elif event.key == pygame.K_w:
                    move_up = False
                elif event.key == pygame.K_s:
                    move_down = False


        if move_right and block["rect"].right <= (WIDTH - SPEED):
            # derecha
            block["rect"].left += SPEED

        elif move_left and block["rect"].left >= SPEED:
            # izquierda
            block["rect"].left -= SPEED

        elif move_up and block["rect"].top >= (0 + SPEED):
            # arriba
            block["rect"].top -= SPEED

        elif move_down and block["rect"].bottom <= HEIGHT - SPEED:
            # abajo
            block["rect"].top += SPEED

        # muevo los carros
        if not flag_slow_coin:
            for car in cars:
                car["rect"].move_ip(2.5, 0)
                if car["rect"].right > WIDTH:
                    car["rect"].right = 0
            for motorcycle in motorcycles:
                motorcycle["rect"].move_ip(4, 0)
                if motorcycle["rect"].right > WIDTH:
                    motorcycle["rect"].right = 0
            for truck in trucks:
                truck["rect"].move_ip(-1, 0)
                if truck["rect"].right < 0:
                    truck["rect"].right = WIDTH
        else:
            for car in cars:
                car["rect"].move_ip(1.5, 0)
                if car["rect"].right > WIDTH:
                    car["rect"].right = 0
            for motorcycle in motorcycles:
                motorcycle["rect"].move_ip(2, 0)
                if motorcycle["rect"].right > WIDTH:
                    motorcycle["rect"].right = 0
            for truck in trucks:
                truck["rect"].move_ip(-1, 0)
                if truck["rect"].right < 0:
                    truck["rect"].right = WIDTH
        
        for coin in coins:
                if detect_collisions(coin["rect"], block["rect"]):
                    coins.remove(coin)
                    score+=1
                    text_score = font.render(f"Score: {score}", True, BLACK)
                    rect_text_score = text_score.get_rect()
                    rect_text_score.midright = (WIDTH, (0 + rect_text_score.height))
                    coin_sound.play()

        for coin in slow_coins:
                if detect_collisions(coin["rect"], block["rect"]):
                    slow_coins.remove(coin)
                    flag_slow_coin = True
                    time_slow_coin = 100
                    score+=1
                    text_score = font.render(f"Score: {score}", True, BLACK)
                    rect_text_score = text_score.get_rect()
                    rect_text_score.midright = (WIDTH, (0 + rect_text_score.height))
                    coin_sound.play()
                if flag_slow_coin:
                    if time_slow_coin > 0:
                        time_slow_coin -= 1
                        print(time_slow_coin)
                    elif time_slow_coin == 0:
                        flag_slow_coin = False

        for motorcycle in motorcycles:
            if detect_collisions(motorcycle["rect"], block["rect"]):
                collision = True
                if collision:
                    print("Chocaron")
                    motorcycles.remove(motorcycle)
                    hearts -= 1
                    text_life = font.render(f"hearts: {hearts}", True, BLACK)
                    rect_text_life = text_life.get_rect()
                    rect_text_life.midleft = (0, 30)
                    pum_sound.play()
            else:
                collision = False
    
        for truck in trucks:
            if detect_collisions(truck["rect"], block["rect"]):
                collision = True
                if collision:
                    print("Chocaron")
                    trucks.remove(truck)
                    hearts -= 1
                    text_life = font.render(f"hearts: {hearts}", True, BLACK)
                    rect_text_life = text_life.get_rect()
                    rect_text_life.midleft = (0, 30)
                    pum_sound.play()
            else:
                collision = False

        for car in cars:
            if detect_collisions(car["rect"], block["rect"]):
                collision = True
                if collision:
                    print("Chocaron")
                    cars.remove(car)
                    hearts -= 1
                    text_life = font.render(f"hearts: {hearts}", True, BLACK)
                    rect_text_life = text_life.get_rect()
                    rect_text_life.midleft = (0, 30)
                    pum_sound.play()
            else:
                collision = False
        
        if hearts == 0:
            move_down = False
            move_right = False
            move_left = False
            move_up = False
            background_sound.stop()
            dead_sound.play()
            break
        
        screen.blit(background, background.get_rect())

        screen.blit(block["img"], block["rect"])
        for coin in coins:
            screen.blit(coin["img"], coin["rect"])
        for coin in slow_coins:
            screen.blit(coin["img"], coin["rect"])
        for car in cars:
            screen.blit(car["img"], car["rect"])
        for motorcycle in motorcycles:
            screen.blit(motorcycle["img"], motorcycle["rect"])
        for truck in trucks:  
            screen.blit(truck["img"], truck["rect"])  
        screen.blit(text_life, rect_text_life)
        screen.blit(text_score, rect_text_score)
        pygame.display.flip()
    
    if score > max_score:
            max_score = score
    
    screen.fill(BLACK)
    screen.blit(background_game_over, background_game_over.get_rect())
    show_text(screen, "Game Over", font, (WIDTH//2, 20), BLUE)
    show_text(screen, f"Score: {score}", font, (WIDTH // 2, HEIGHT - 70), YELLOW)
    show_text(screen, f"Max Score: {max_score}", font, (WIDTH // 2, HEIGHT - 30), YELLOW)
    with open(completely_path, "w") as file:
        file.write(f"la maxima puntuacion es {max_score}")
    pygame.display.flip()
    wait_user()




