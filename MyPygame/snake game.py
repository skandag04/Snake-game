import pygame
import time
import random
from pygame.locals import *

SIZE = 25
BACKGROUND_COLOR=(11,110,5)
#pygame.display.flip()
class Apple:
        def __init__(self, parent_screen):
                self.image = pygame.Surface((25,25))
                self.image.fill((255,0,0))
                self.parent_screen = parent_screen
                self.x = SIZE*3
                self.y = SIZE*3
                
        def draw(self):
                #self.parent_screen.fill((110, 110, 5))
                self.parent_screen.blit(self.image, (self.x, self.y))
                pygame.display.flip()  
        
        def move(self):
             self.x = random.randint(1,19)*SIZE
             self.y = random.randint(1,15)*SIZE    
                
class Snake:
        def __init__(self, parent_screen,length):
                self.length = length
                self.parent_screen = parent_screen
                #self.block = pygame.image.load("MyPygame/block.jpeg").convert()
                #self.block = pygame.transform.scale(block, (50, 50))
                self.block = pygame.Surface((25,25))
                self.block.fill((0,0,0))
                self.x = [SIZE]*length
                self.y = [SIZE]*length
                #self.x=100
                #self.y=100
                self.direction='down'
                
        def increase_length(self):
                self.length+=1
                self.x.append(-1)
                self.y.append(-1)
                
                
        
        def move_left(self):
                self.direction = 'left'
                
        def move_right(self):
                self.direction = 'right'
                
        def move_up(self):
                self.direction = 'up'
        
        def move_down(self):
                self.direction = 'down'
        
        def draw(self):
                #self.surface = pygame.display.set_mode((1000, 800))
                #self.background = pygame.image.load("MyPygame/grass.jpg")
                self.parent_screen.fill((BACKGROUND_COLOR))
                #pygame.display.flip()
                for i in range(self.length):
                        self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
                pygame.display.flip()        
        
        
        def walk(self):
                
                for i in range(self.length-1,0,-1):
                        self.x[i] = self.x[i - 1]
                        self.y[i] = self.y[i - 1]
                if self.direction == 'left':
                        self.x[0] -= SIZE
                if self.direction == 'right':
                        self.x[0] += SIZE
                if self.direction == 'up':
                        self.y[0] -= SIZE
                if self.direction == 'down':
                        self.y[0] += SIZE
                        
                self.draw()
                        
                        
        
class Game:
        def __init__(self):
                pygame.init()
                self.surface = pygame.display.set_mode((1000, 800))  # This sets the screen mode
                #self.background = pygame.image.load("MyPygame/grass.jpg").convert()
                #self.surface.blit(self.background, (0,0))
                #self.surface = pygame.display.set_mode((1000, 800))
                #self.background = pygame.image.load("MyPygame/grass.jpg")  # Load the background image
        
                # Resize the image if necessary to fit the screen size (1000x800 in this case)
                #self.background = pygame.transform.scale(self.background, (1000, 800))
                self.surface = pygame.display.set_mode((1000, 800))
                self.surface.fill((11, 110, 5))
                self.snake = Snake(self.surface,1)
                self.snake.draw()
                self.apple = Apple(self.surface)
                self.apple.draw()
                
                #self.clock = pygame.time.Clock()
        
        def is_collision(self,x1,y1,x2,y2):
                if x1 >= x2 and x1 < x2 + SIZE:
                        if y1 >= y2 and y1 < y2 + SIZE:
                                  return True
                return False
        
        def display_score(self):
                font = pygame.font.SysFont('arial',30)
                score = font.render(f"Score : {self.snake.length}", True, (255,255,255))
                self.surface.blit(score, (800,10))
        
        def play(self):
                self.snake.walk()
                self.apple.draw()
                self.display_score()
                pygame.display.flip()
                #snake colliding with apple
                if self.is_collision(self.snake.x[0],self.snake.y[0], self.apple.x, self.apple.y):
                        self.snake.increase_length()
                        self.apple.move()
                        
                #snake collision with itself
                for i in range(3,self.snake.length):
                        if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                              raise "Game over"   
                #snake collision with wall
                if self.snake.x[0] < 0 or self.snake.x[0] >= 1000 or self.snake.y[0] < 0 or self.snake.y[0] >= 800:
                        raise "Game over" 
                
        def show_game_over(self):
                self.surface.fill(BACKGROUND_COLOR)
                font = pygame.font.SysFont('arial',30)
                line1 = font.render(f"Game is over ! Your score is {self.snake.length}", True,(255,255,255))
                self.surface.blit(line1, (280,300))
                line2 = font.render("To play again hit enter, TO exit press escape", True,(255,255,255))
                self.surface.blit(line2, (200,400))
                pygame.display.flip() 
                
        def reset(self):
                self.snake  = Snake(self.surface,1)
                self.apple = Apple(self.surface)  
                
        def run(self):
                running = True
                while running:
                        for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                        if event.key == K_ESCAPE:
                                                running = False
                                        if event.key == K_RETURN:
                                                pause = False
                                        if not pause:
                                                
                                
                                                if event.key == K_UP:
                                                        self.snake.move_up()
                                                if event.key == K_DOWN:
                                                        self.snake.move_down()
                                                if event.key == K_LEFT:
                                                        self.snake.move_left()
                                                if event.key == K_RIGHT:
                                                        self.snake.move_right()
                                                
                                
                                
                                elif event.type == QUIT:
                                        running = False
                                        
                        try:
                                if not pause:
                                        self.play()
                        
                        except Exception as e:
                                self.show_game_over()
                                pause = True
                                self.reset()
                        
                        time.sleep(0.2)
                        #self.clock = pygame.time.Clock()
                        #self.clock.tick(10)  # Controls the speed, lower = slower, higher = faster

  

if __name__ == '__main__':
        game = Game()
        game.run()
    
    
        


        