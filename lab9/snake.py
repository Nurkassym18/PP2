import pygame
import random 
import time 

pygame.init()
cell_size = 10

screen = pygame.display.set_mode((300,200))
pygame.display.set_caption("Snake game")

snake = [(50, 50), (40, 50), (30, 50)]
snake_dir = (cell_size, 0)

def spawn_food():
    food_x = random.randint(0, (300 - cell_size) // cell_size) * cell_size # generate coordinate for (x,y)
    food_y = random.randint(0, (200 - cell_size) // cell_size) * cell_size
    
    food_size = random.randint(10, 20)  #generate random size for apple 
    return (food_x, food_y, food_size)
def draw_snake():
    for segment in snake:  # draw snake
        pygame.draw.rect(screen,(0,255,0), (*segment, cell_size, cell_size))

def draw_food():
    if food is not None : #if food exists , draw the food
        pygame.draw.rect(screen, (255,0,0), (food[0],food[1], food[2], food[2]))
food = spawn_food() 
running = True 
score_apples = 0

last_food = time.time()

food_delay = 5

clock = pygame.time.Clock()

while running :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0,cell_size):
                snake_dir = (0, -cell_size)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -cell_size):
                snake_dir = (0, cell_size)
            elif event.key == pygame.K_LEFT and snake_dir != (cell_size, 0):
                snake_dir = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-cell_size, 0):
                snake_dir = (cell_size, 0)

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)
    
    if food and time.time() - last_food >= food_delay:
        food = None 
    
    if food is None and time.time() - last_food >= 1:
        food = spawn_food()
        last_food = time.time()
    
    if food and (new_head[0] in range(food[0], food[0] + food[2]) and 
            new_head[1] in range(food[1], food[1] + food[2])): #we check the collision between snake and apple 
            score_apples += 1
            food = None  
            last_food = time.time() #update the time 
    else:
        snake.pop() #remove the хвост snake
        
    
    if (new_head[0] < 0 or new_head[0] >= 300 or new_head[1] < 0 or new_head[1] >= 200 or new_head in snake[1:]):
        running = False  #checking collisions by itself 
    
    screen.fill((0, 0, 0))
    draw_snake()
    draw_food()
  
    pygame.display.flip()
    clock.tick(5)
print(score_apples)
pygame.quit()