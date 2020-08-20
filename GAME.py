import pygame

pygame.init()

win = pygame.display.set_mode((1200, 600))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkUp = [pygame.image.load('U1.png'), pygame.image.load('U2.png'), pygame.image.load('U3.png'),
            pygame.image.load('U4.png'), pygame.image.load('U5.png'), pygame.image.load('U6.png'),
            pygame.image.load('U7.png'), pygame.image.load('U8.png'), pygame.image.load('U9.png')]
walkDown = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png'),
            pygame.image.load('D4.png'), pygame.image.load('D5.png'), pygame.image.load('D6.png'),
            pygame.image.load('D7.png'), pygame.image.load('D8.png'), pygame.image.load('D9.png')]
bg = pygame.image.load('bg.png')


clock = pygame.time.Clock()


class player(object):
    def __init__(self,x ,y ,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.up:
                win.blit(walkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(walkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            elif self.up:
                win.blit(walkUp[0], (self.x, self.y))
            else:
                win.blit(walkDown[0], (self.x, self.y))

class projectile(object):
    def __init__(self ,x ,y ,radius ,color ,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# mainloop
man = player(200, 450, 100, 150)
bullets = [] # This goes right above the while loop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 1200 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))  # This will remove the bullet if it is off the screen

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -3
        else:
            facing = 3

        if len(bullets) < 10:
            if man.right:
                bullets.append(projectile(round(man.x + man.width + 10), round(man.y + man.height-55), 6, (0, 0, 0), facing))
            else:
                bullets.append(projectile(round(man.x + man.width - 110), round(man.y + man.height - 55), 6, (0, 0, 0), facing))


    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False
        man.standing = False  # NEW
    elif keys[pygame.K_RIGHT] and man.x < 1100:
        man.x += man.vel
        man.right = True
        man.left = False
        man.up = False
        man.down = False
        man.standing = False  # NEW
    elif keys[pygame.K_UP] and man.y > 0:
        man.y -= man.vel
        man.right = False
        man.left = False
        man.up = True
        man.down = False
        man.standing = False  # NEW
    elif keys[pygame.K_DOWN] and man.y < 445:
        man.y += man.vel
        man.right = False
        man.left = False
        man.up = False
        man.down = True
        man.standing = False  # NEW
    else:
        man.standing = True  # NEW (r# emoved two lines)
        man.walkCount = 0




    redrawGameWindow()
