

import pygame   # import the module to enable you to make the game


pygame.init()   #initialise the function
width, height = 800, 600
screen=pygame.display.set_mode((width, height))

import pygame
file_name = "NOLK-GAME/data/images.jpg"
player = pygame.image.load(file_name)

while 1:
    screen.fill(0)
    screen.blit(player, playerpos)
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

file_name2 = "NOLK-GAME/data/Battlefield.jpg"
battle_field = pygame.image.load(file_name2)

file_name3 = "NOLK-GAME/data/castle.png"
castle = pygame.image.load(file_name3)

for x in range(width/battle_field.get_width()+1):
    for y in range(height/battle_field.get_height()+1):             \
    screen.blit(battle_field , (x*100, y*100))
    screen.blit(castle , (0 , 30))
    screen.blit(castle , (0 , 135))
    screen.blit(castle , (0 , 240))
    screen.blit(castle , (0 , 345 ))

keys = [False, False, False, False]
playerpos = [100,100]



if event.type == pygame.KEYDOWN:
    if event.key == K_w:
        keys[0] = True
    elif event.key == K_a:
        keys[1] = True
    elif event.key == K_s:
        keys[2] = True
    elif event.key == K_d:
        keys[3] = True


if event.type == pygame.KEYUP:
    if event.key == pygame.K_w:
        keys[0] = False
    elif event.key == pygame.K_a:
        keys[1] = False
    elif event.key == pygame.K_s:
        keys[2] = False
    elif event.key == pygame.K_d:
        keys[3] = False


if keys[0]:   # This is now the player movement.....
    playerpos[1] -= 5
elif keys[2]:
    playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5

import math

position = pygame.mouse.get_pos()      #Setting the player position and rotation
angle = math.atan2(position[1] - (playerpos[1]+32),position[0] - (playerpos[0]+26))
playerrot = pygame.transform.rotate(player, 360-angle*57.29)
playerpos1 = (playerpos[0] - playerrot.get_rect().width/2, playerpos[1] - playerrot.get_rect().height/2)
screen.blit(playerrot, playerpos1)


acc = [0,0]
canon_balls = []

file_name4 = "NOLK-GAME/data/bullet.png"
canon_ball = pygame.image.load(file_name4)

if event.type == pygame.MOUSEBUTTONDOWN:
    position = pygame.mouse.get_pos()
    acc[1] += 1
    canon_balls.append([math.atan2(position[1] - (playerpos1[1]+32),position[0] - (playerpos1[0]+26)), playerpos1[0]+32, player[1]+32])

for bullet in canon_ballss:
    index = 0
    velx = math.cos(bullet[0])*10
    vely = math.sin(bullet[0])*10
    bullet[1] += velx
    bullet[2] += vely
    if bullet[1] <-64 or bullet > 800 or  bullet[2]<-64 or bullet[2] > 600:
        canon_balls.pop(index)
    index += 1
    for projectile in canon_balls:
        canon_ball1 = pygame.transform.rotate(canon_ball, 360-projectile[0]*57.29)
        screen.blit(canon_ball1, (projectile[1], projectile[2]))

# Here we insert the enemy into the game...
enemy_timer = 100
enemy_timer1 = 0
enemyz = [[800,100]]
life_meter = 194

file_name5 = "NOLK-GAME/data/badguy.png"
enemyimage1 = pygame.image.load(file_name5)
enemyimage = enemyimage1

if enemy_timer == 0:
    enemyz.append([800, random.randint(50,550)])
    enemy_timer = 100-(enemy_timer1*2)
    if enemy_timer1 >= 35:
        enemy_timer1 = 35
    else:
        enemy_timer1 += 5
index = 0
for enemy in enemyz:
    if enemy[0]<-64:
        enemyz.pop(index)
    enemy[0] -= 7
    index += 1
for enemy in enemyz:
    screen.blit(enemyimage, enemy)

# enemy attack.
badrect = pygame.Rect(enemyimage.get_rect())
badrect.top = badguy[1]
badrect.left = enemy[0]
if badrect.left < 64:
    life_level -= random.randint(5,20)

#reinenforcements
index1 = 0
for bullet in canon_balls:
    ballrect = pygame.Rect(canon_ball.get_rect())
    bullrect.left = bullet[1]
    bullrect.top = bullet[2]
    if badrect.colliderect(bullrect):
        acc[0] += 1
        enemyz.pop(index)
        canon_balls.pop(index)
    index1 += 1


font = pygame.font.Font(None, 24)
survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+
                           str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
textRect = survivedtext.get_rect()
textRect.topright = [635,5]
screen.blit(survivedtext, textRect)

file_name6 = "C:/Users/Owner/PycharmProjects/untitled/health.png"
life_bar = pygame.image.load(file_name6)

file_name7 = "C:/Users/Owner/Documents/CALVIN/resources/images/healthbar.png"
health = pygame.image.load(file_name7)

screen.blit(life_bar, (5,5))
for health1 in range(healthvalue):
    screen.blit(health, (health1+8,8))


if pygame.time.get_ticks()>=90000:
    running = 0
    exitcode = 1
if healthvalue <= 0:
    running = 0
    exitcode = 0
if acc[1]!= 0:
    accuracy = acc[0]*1.0/acc[1]*100
else:
    accuracy = 0

if exitcode == 0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(GAME_OVER, (0,0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(YOU_WIN, (0,0))
    screen.blit(text, textRect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()

file_name8 = "C:/Users/Owner/Documents/CALVIN/resources/images/gameover.png"
GAME_OVER = pygame.image.load(file_name8)

file_name9 = "C:/Users/Owner/Documents/CALVIN/resources/images/youwin.png"
YOU_WIN = pygame.image.load(file_name9)


while 1:
    enemy_timer -= 1
    running = 1
    exitcode = 0
    while running:
        enemy_timer -= 1
