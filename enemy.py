import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        super().__init__()

        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 7
        self.direction = direction

    def update(self):

        self.rect.x += self.speed * self.direction

        # Remove bullet when it goes outside screen
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, left_limit, right_limit):
        super().__init__()

        # Enemy size
        self.width = 60
        self.height = 60

        # Cat image
        self.image = pygame.image.load(
            "enemy.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (self.width, self.height)
        )

        # Position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Movement
        self.speed = 2
        self.direction = 1

        # Patrol limits
        self.left_limit = left_limit
        self.right_limit = right_limit

        # Jump
        self.jump_speed = -12
        self.gravity = 0.5
        self.velocity_y = 0

        self.ground_y = y

        # Jump timer
        self.jump_timer = 0
        self.jump_delay = 120

        # Shooting
        self.shoot_timer = 0
        self.shoot_delay = 90


    def update(self):

        # =========================
        # LEFT-RIGHT MOVEMENT
        # =========================

        self.rect.x += self.speed * self.direction

        if self.rect.right >= self.right_limit:
            self.rect.right = self.right_limit
            self.direction = -1

        if self.rect.left <= self.left_limit:
            self.rect.left = self.left_limit
            self.direction = 1


        # =========================
        # JUMP
        # =========================

        self.jump_timer += 1

        if self.jump_timer >= self.jump_delay:

            if self.rect.y >= self.ground_y:

                self.velocity_y = self.jump_speed
                self.jump_timer = 0


        # =========================
        # GRAVITY
        # =========================

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y


        # =========================
        # GROUND
        # =========================

        if self.rect.y >= self.ground_y:

            self.rect.y = self.ground_y
            self.velocity_y = 0


        # =========================
        # SHOOT TIMER
        # =========================

        self.shoot_timer += 1


    def shoot(self, player):

        # Decide bullet direction based on player position

        if player.centerx < self.rect.centerx:
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


    def ready_to_shoot(self):

        if self.shoot_timer >= self.shoot_delay:

            self.shoot_timer = 0

            return True

        return False


    def check_collision(self, player):

        return self.rect.colliderect(player)