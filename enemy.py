import pygame


# ==================================================
# BULLET CLASS
# ==================================================

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):

        super().__init__()


        # ==========================================
        # BULLET
        # ==========================================

        self.image = pygame.Surface(
            (12, 6)
        )

        self.image.fill(
            (255, 0, 0)
        )


        self.rect = self.image.get_rect()

        self.rect.center = (
            x,
            y
        )


        # ==========================================
        # BULLET SPEED
        # ==========================================

        self.speed = 7

        self.direction = direction


    # ==========================================
    # UPDATE BULLET
    # ==========================================

    def update(self):

        self.rect.x += (
            self.speed *
            self.direction
        )


        # ==========================================
        # REMOVE BULLET
        # ==========================================

        if self.rect.right < 0:

            self.kill()


        if self.rect.left > 800:

            self.kill()


# ==================================================
# ENEMY CLASS - CAT
# ==================================================

class Enemy(pygame.sprite.Sprite):

    def __init__(
        self,
        x,
        y,
        left_limit,
        right_limit
    ):

        super().__init__()


        # ==========================================
        # ENEMY SIZE
        # ==========================================

        self.width = 70
        self.height = 70


        # ==========================================
        # CAT IMAGE
        # ==========================================

        self.original_image = pygame.image.load(
            "enemy.png"
        ).convert_alpha()


        self.original_image = pygame.transform.scale(
            self.original_image,
            (
                self.width,
                self.height
            )
        )


        self.image = self.original_image


        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


        # ==========================================
        # MOVEMENT
        # ==========================================

        self.speed = 2

        self.direction = 1


        # ==========================================
        # PATROL LIMITS
        # ==========================================

        self.left_limit = left_limit

        self.right_limit = right_limit


        # ==========================================
        # JUMP
        # ==========================================

        self.jump_speed = -12

        self.gravity = 0.5

        self.velocity_y = 0


        # Enemy ground position
        self.ground_y = y


        # ==========================================
        # JUMP TIMER
        # ==========================================

        self.jump_timer = 0

        self.jump_delay = 150


        # ==========================================
        # SHOOT TIMER
        # ==========================================

        self.shoot_timer = 0

        self.shoot_delay = 90


    # ==========================================
    # UPDATE ENEMY
    # ==========================================

    def update(self):


        # ======================================
        # MOVE CAT
        # ======================================

        self.rect.x += (
            self.speed *
            self.direction
        )


        # ======================================
        # RIGHT LIMIT
        # ======================================

        if self.rect.right >= self.right_limit:

            self.rect.right = self.right_limit

            self.direction = -1


        # ======================================
        # LEFT LIMIT
        # ======================================

        if self.rect.left <= self.left_limit:

            self.rect.left = self.left_limit

            self.direction = 1


        # ======================================
        # FLIP CAT
        # ======================================

        if self.direction == -1:

            self.image = pygame.transform.flip(
                self.original_image,
                True,
                False
            )

        else:

            self.image = self.original_image


        # ======================================
        # JUMP TIMER
        # ======================================

        self.jump_timer += 1


        if self.jump_timer >= self.jump_delay:

            if self.rect.y >= self.ground_y:

                self.velocity_y = self.jump_speed

                self.jump_timer = 0


        # ======================================
        # GRAVITY
        # ======================================

        self.velocity_y += self.gravity

        self.rect.y += self.velocity_y


        # ======================================
        # GROUND
        # ==========================================

        if self.rect.y >= self.ground_y:

            self.rect.y = self.ground_y

            self.velocity_y = 0


        # ==========================================
        # SHOOT TIMER
        # ==========================================

        self.shoot_timer += 1


    # ==========================================
    # SHOOT BULLET
    # ==========================================

    def shoot(self, player):


        # ======================================
        # CHECK PLAYER POSITION
        # ======================================

        if player.rect.centerx < self.rect.centerx:

            direction = -1

            gun_x = self.rect.left

        else:

            direction = 1

            gun_x = self.rect.right


        gun_y = self.rect.centery


        return Bullet(
            gun_x,
            gun_y,
            direction
        )


    # ==========================================
    # READY TO SHOOT
    # ==========================================

    def ready_to_shoot(self):

        if self.shoot_timer >= self.shoot_delay:

            self.shoot_timer = 0

            return True

        return False


    # ==========================================
    # PLAYER COLLISION
    # ==========================================

    def check_collision(self, player_rect):

        return self.rect.colliderect(
            player_rect
        )