import pygame

from enemy import Enemy, Bullet


pygame.init()


# ==========================================
# SCREEN
# ==========================================

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Cat Enemy Game"
)


# ==========================================
# COLORS
# ==========================================

WHITE = (255, 255, 255)

GREEN = (0, 180, 0)

BLUE = (50, 100, 255)

DARK_GRAY = (80, 80, 80)


# ==========================================
# CLOCK
# ==========================================

clock = pygame.time.Clock()


# ==========================================
# ENEMY GROUP
# ==========================================

enemy_group = pygame.sprite.Group()


# ==========================================
# BULLET GROUP
# ==========================================

bullet_group = pygame.sprite.Group()


# ==========================================
# CREATE ENEMY
# ==========================================

enemy = Enemy(
    400,      # X position
    440,      # Y position
    250,      # Left limit
    700       # Right limit
)

enemy_group.add(enemy)


# ==========================================
# TEMPORARY PLAYER
# ==========================================

player = pygame.Rect(
    100,      # X
    460,      # Y
    40,       # Width
    40        # Height
)


player_speed = 5


# ==========================================
# PLAYER LIFE
# ==========================================

player_lives = 1


# ==========================================
# GAME LOOP
# ==========================================

running = True


while running:

    # ======================================
    # EVENTS
    # ======================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # ======================================
    # PLAYER MOVEMENT
    # ======================================

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:

        player.x -= player_speed


    if keys[pygame.K_RIGHT]:

        player.x += player_speed


    # ======================================
    # UPDATE ENEMY
    # ======================================

    enemy_group.update()


    # ======================================
    # ENEMY SHOOTING
    # ======================================

    if enemy.ready_to_shoot():

        bullet = enemy.shoot(player)

        bullet_group.add(bullet)


    # ======================================
    # UPDATE BULLETS
    # ======================================

    bullet_group.update()


    # ======================================
    # ENEMY - PLAYER COLLISION
    # ======================================

    if enemy.check_collision(player):

        print("PLAYER HIT!")

        player_lives -= 1

        if player_lives <= 0:

            print("PLAYER DIED!")

            running = False


    # ======================================
    # BULLET - PLAYER COLLISION
    # ======================================

    for bullet in bullet_group:

        if bullet.rect.colliderect(player):

            print("PLAYER SHOT!")

            player_lives = 0

            bullet.kill()

            print("PLAYER DIED!")

            running = False


    # ======================================
    # BACKGROUND
    # ======================================

    screen.fill(WHITE)


    # ======================================
    # GROUND
    # ======================================

    pygame.draw.rect(
        screen,
        GREEN,
        (0, 500, WIDTH, 100)
    )


    # ======================================
    # PLAYER
    # ======================================

    pygame.draw.rect(
        screen,
        BLUE,
        player
    )


    # ======================================
    # ENEMY
    # ======================================

    enemy_group.draw(screen)


    # ======================================
    # ENEMY GUN
    # ======================================

    if enemy.direction == 1:

        # Gun pointing right

        pygame.draw.rect(
            screen,
            DARK_GRAY,
            (
                enemy.rect.right - 5,
                enemy.rect.centery - 5,
                20,
                8
            )
        )

    else:

        # Gun pointing left

        pygame.draw.rect(
            screen,
            DARK_GRAY,
            (
                enemy.rect.left - 15,
                enemy.rect.centery - 5,
                20,
                8
            )
        )


    # ======================================
    # BULLETS
    # ======================================

    bullet_group.draw(screen)


    # ======================================
    # UPDATE DISPLAY
    # ======================================

    pygame.display.update()


    # ======================================
    # FPS
    # ======================================

    clock.tick(60)


# ==========================================
# QUIT
# ==========================================

pygame.quit()