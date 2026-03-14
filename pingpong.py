from pygame import *


back = (200, 255, 255) 
main_win = display.set_mode((700, 500)) 



finish = False
game_over = False


clock = time.Clock()



class GameSprite(sprite.Sprite):
    def __init__(self, picture, speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (80, 80))
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

    

ball = GameSprite('мяч-no-bg-preview (carve.photos).png', 5, 300, 220)
rocket1 = Player('ракетка-no-bg-preview (carve.photos).png', 3, 0, 220)
rocket2 = Player('ракетка-no-bg-preview (carve.photos).png', 3, 620, 220)

while not game_over:
    for e in event.get():
        if e.type == QUIT:
           game_over = True
    main_win.fill(back)
    rocket1.go(K_w, K_s)
    rocket2.go(K_UP, K_DOWN)
    ball.reset()
    rocket1.reset()
    rocket2.reset()
    display.update()
    clock.tick(60)
    
    