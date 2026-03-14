from pygame import *
font.init()

back = (200, 255, 255) 
main_win = display.set_mode((700, 500)) 
win1 = font.Font(None, 30)
win2 = font.Font(None, 30)
w1 = win1.render('Игрок 1 проиграл', False, (133, 21, 40))
w2 = win1.render('Игрок 2 проиграл', False, (133, 21, 40))

finish = False
game_over = False


clock = time.Clock()



class GameSprite(sprite.Sprite):
    def __init__(self, picture, speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def go(self, W, S):
        keys = key.get_pressed()
        if keys[W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[S] and self.rect.y < 420:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3    

ball = GameSprite('мяч-no-bg-preview (carve.photos).png', 1, 300, 220)
rocket1 = Player('ракетка-no-bg-preview (carve.photos).png', 5, 0, 220)
rocket2 = Player('ракетка-no-bg-preview (carve.photos).png', 5, 620, 220)

while not game_over:
    for e in event.get():
        if e.type == QUIT:
           game_over = True
    if finish != True:
        main_win.fill(back)
        ball.reset()
        rocket1.reset()
        rocket2.reset()
        rocket1.go(K_w, K_s)
        rocket2.go(K_UP, K_DOWN)
        if ball.rect.x < 650 and ball.rect.x > 50:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        elif ball.rect.x < 0:
            finish = True
            main_win.blit(w1, (300, 200))
        elif ball.rect.x > 600:
            finish = True
            main_win.blit(w2, (300, 300))
        if ball.rect.y > 470 or ball.rect.y < 30:
            speed_y *= -1
        if sprite.collide_rect(ball, rocket1) or sprite.collide_rect(ball, rocket2):
            speed_x*= -1
    
        
    display.update()
    clock.tick(60)
display.update()
    


