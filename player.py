import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        # ==========================================
        # PLAYER IMAGE - WHITE MOUSE
        # ==========================================

        self.width = 70
        self.height = 70

        self.original_image = pygame.image.load(
            "player.png"
        ).convert_alpha()

        self.original_image = pygame.transform.scale(
            self.original_image,
            (self.width, self.height)
        )

        self.image = self.original_image

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


        # ==========================================
        # MOVEMENT
        # ==========================================

        self.speed = 5


        # ==========================================
        # JUMP
        # ==========================================

        self.jump_speed = -12
        self.gravity = 0.5

        self.velocity_y = 0

        self.on_ground = True


        # ==========================================
        # GROUND
        # ==========================================

        self.ground_y = 500


        # ==========================================
        # DIRECTION
        # 1 = RIGHT
        # -1 = LEFT
        # ==========================================

        self.direction = 1


    # ==========================================
    # UPDATE PLAYER
    # ==========================================

    def update(self):

        keys = pygame.key.get_pressed()


        # ======================================
        # MOVE LEFT
        # ======================================

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:

            self.rect.x -= self.speed

            self.direction = -1


        # ======================================
        # MOVE RIGHT
        # ======================================

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:

            self.rect.x += self.speed

            self.direction = 1


        # ======================================
        # FLIP IMAGE
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
        # JUMP
        # ======================================

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:

            if self.on_ground:

                self.velocity_y = self.jump_speed

                self.on_ground = False


        # ======================================
        # GRAVITY
        # ======================================

        self.velocity_y += self.gravity

        self.rect.y += self.velocity_y


        # ======================================
        # GROUND COLLISION
        # ==========================================

        if self.rect.bottom >= self.ground_y:

            self.rect.bottom = self.ground_y

            self.velocity_y = 0

            self.on_ground = True


        # ======================================
        # SCREEN LEFT LIMIT
        # ======================================

        if self.rect.left < 0:

            self.rect.left = 0


        # ======================================
        # SCREEN RIGHT LIMIT
        # ======================================

        if self.rect.right > 800:

            self.rect.right = 800