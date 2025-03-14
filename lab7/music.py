import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Music player")
icon = pygame.image.load("White.png")
icon = pygame.transform.scale(icon,(600,600))

clock = pygame.time.Clock()

running = True

stop = pygame.image.load("image/stop.png")
stop = pygame.transform.scale(stop,(150,150))

play = pygame.image.load("image/play.png")
play = pygame.transform.scale(play,(150,150))

Stop_Play = [play,stop]
counter=0

left = pygame.image.load("image/left.png")
left = pygame.transform.scale(left,(150,150))

right = pygame.image.load("image/right.png")
right = pygame.transform.scale(right,(150,150))

playlist = ["sounds/1.mp3", "sounds/2.mp3","sounds/3.mp3"]
image1=pygame.image.load("image/1.png")
image1=pygame.transform.scale(image1,(450,300))

image2=pygame.image.load("image/2.png")
image2=pygame.transform.scale(image2,(450,300))

image3=pygame.image.load("image/3.png")
image3=pygame.transform.scale(image3,(450,300))

image = [image1,image2,image3]
current_song=0

pygame.mixer.music.load(playlist[current_song])
pygame.mixer.music.play()

while running:
    pygame.display.update()
    screen.blit(icon,(0,0))
    screen.blit(image[current_song], (75, 50))
    screen.blit(Stop_Play[counter],(225,400))
    screen.blit(right,(425,400))
    screen.blit(left,(25,400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():  
                    pygame.mixer.music.pause()
                    counter = (counter + 1) % len(Stop_Play)
                
                else:
                    pygame.mixer.music.unpause()
                    counter = (counter - 1) % len(Stop_Play)

                    

            
            elif event.key == pygame.K_RIGHT:
                current_song = (current_song + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT: 
                current_song = (current_song - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()

    
    clock.tick(60)  

pygame.quit()
    


