import pygame

from player import Player
from enemy import Enemy


pygame.init()


# ==================================================
# SCREEN
# ==================================================

WIDTH = 800
HEIGHT = 600


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)


pygame.display.set_caption(
    "Mouse vs Cat"
)


# ==================================================
# COLORS
# ==================================================

WHITE = (255, 255, 255)

GREEN = (0, 180, 0)

DARK_GRAY = (80, 80, 80)


# ==================================================
# CLOCK
# ==================================================

clock = pygame.time.Clock()


# ==================================================
# PLAYER
# ==================================================

player = Player(
    100,
    430
)


# ==================================================
# ENEMY
# ==================================================

enemy = Enemy(
    500,
    430,
    250,
    700
)


# ==================================================
# GROUPS
# ==================================================

enemy_group = pygame.sprite.Group()

bullet_group = pygame.sprite.Group()


enemy_group.add(
    enemy
)


# ==================================================
# PLAYER LIVES
# ==================================================

player_lives = 3


# ==================================================
# GAME LOOP
# ==================================================

running = True


while running:


    # ==========================================
    # EVENTS
    # ==========================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # ==========================================
    # PLAYER UPDATE
    # ==========================================

    player.update()


    # ==========================================
    # ENEMY UPDATE
    # ==========================================

    enemy_group.update()


    # ==========================================
    # ENEMY SHOOTING
    # ==========================================

    if enemy.ready_to_shoot():

        bullet = enemy.shoot(
            player
        )

        bullet_group.add(
            bullet
        )


    # ==========================================
    # BULLET UPDATE
    # ==========================================

    bullet_group.update()


    # ==========================================
    # CAT - MOUSE COLLISION
    # ==========================================

    if enemy.check_collision(
        player.rect
    ):

        print("MOUSE HIT!")

        player_lives -= 1

        player.rect.x = 100


        if player_lives <= 0:

            print("MOUSE DIED!")

            running = False


    # ==========================================
    # BULLET - MOUSE COLLISION
    # ==========================================

    for bullet in bullet_group:


        if bullet.rect.colliderect(
            player.rect
        ):

            print("MOUSE SHOT!")

            player_lives -= 1

            bullet.kill()


            # Move mouse back
            player.rect.x = 100


            if player_lives <= 0:

                print("MOUSE DIED!")

                running = False


    # ==========================================
    # BACKGROUND
    # ==========================================

    screen.fill(
        WHITE
    )


    # ==========================================
    # GROUND
    # ==========================================

    pygame.draw.rect(
        screen,
        GREEN,
        (
            0,
            500,
            WIDTH,
            100
        )
    )


    # ==========================================
    # DRAW PLAYER
    # ==========================================

    screen.blit(
        player.image,
        player.rect
    )


    # ==========================================
    # DRAW ENEMY
    # ==========================================

    enemy_group.draw(
        screen
    )


    # ==========================================
    # CAT GUN
    # ==========================================

    if enemy.direction == 1:

        # Gun pointing RIGHT

        pygame.draw.rect(
            screen,
            DARK_GRAY,
            (
                enemy.rect.right - 5,
                enemy.rect.centery - 4,
                20,
                8
            )
        )

    else:

        # Gun pointing LEFT

        pygame.draw.rect(
            screen,
            DARK_GRAY,
            (
                enemy.rect.left - 15,
                enemy.rect.centery - 4,
                20,
                8
            )
        )


    # ==========================================
    # DRAW BULLETS
    # ==========================================

    bullet_group.draw(
        screen
    )


    # ==========================================
    # DISPLAY
    # ==========================================

    pygame.display.update()


    # ==========================================
    # FPS
    # ==========================================

    clock.tick(60)


# ==================================================
# QUIT
# ==================================================

pygame.quit()