import pygame
import os

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Lecteur Audio")

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.Font(None, 25)

audio_files = ['audio1.mp3', 'audio2.mp3', 'audio3.mp3']

selected_track = 0

pygame.mixer.music.load(audio_files[selected_track])

play_button = pygame.Rect(50, 100, 50, 50)
pause_button = pygame.Rect(150, 100, 50, 50)
stop_button = pygame.Rect(250, 100, 50, 50)
previous_button = pygame.Rect(50, 200, 50, 50)
next_button = pygame.Rect(150, 200, 50, 50)
loop_button = pygame.Rect(250, 200, 50, 50)
volume_up_button = pygame.Rect(50, 300, 50, 50)
volume_down_button = pygame.Rect(150, 300, 50, 50)
add_button = pygame.Rect(250, 300, 50, 50)
remove_button = pygame.Rect(350, 300, 50, 50)

volume = 0.5
pygame.mixer.music.set_volume(volume)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                pygame.mixer.music.play()
            elif pause_button.collidepoint(mouse_pos):
                pygame.mixer.music.pause()
            elif stop_button.collidepoint(mouse_pos):
                pygame.mixer.music.stop()
            elif previous_button.collidepoint(mouse_pos):
                selected_track = (selected_track - 1) % len(audio_files)
                pygame.mixer.music.load(audio_files[selected_track])
                pygame.mixer.music.play()
            elif next_button.collidepoint(mouse_pos):
                selected_track = (selected_track + 1) % len(audio_files)
                pygame.mixer.music.load(audio_files[selected_track])
                pygame.mixer.music.play()
            elif loop_button.collidepoint(mouse_pos):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()
            elif volume_up_button.collidepoint(mouse_pos):
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)
            elif volume_down_button.collidepoint(mouse_pos):
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)
            elif add_button.collidepoint(mouse_pos):
                file_path = pygame.filedialog.askopenfilename()
                if file_path != '':
                    audio_files.append(file_path)
            elif remove_button.collidepoint(mouse_pos):
                os.remove(audio_files[selected_track])
                audio_files.pop(selected_track)
                if len(audio_files) == 0:
                    pygame.mixer.music.stop()
                else:
                    selected_track = selected_track % len(audio_files)
                    pygame.mixer.music.load(audio_files[selected_track])
                    pygame.mixer.music.play()

            window.fill(white)
            pygame.draw.rect(window, black, play_button)
            pygame.draw.rect(window, black, pause_button)
            pygame.draw.rect(window, black, stop_button)
            pygame.draw.rect(window, black, previous_button)
            pygame.draw.rect(window, black, next_button)
            pygame.draw.rect(window, black, loop_button)
            pygame.draw.rect(window, black, volume_up_button)
            pygame.draw.rect(window, black, volume_down_button)
            pygame.draw.rect(window, black, add_button)
            pygame.draw.rect(window, black, remove_button)
            window.blit(font.render("Play", True, white), (60, 110))
            window.blit(font.render("Pause", True, white), (160, 110))
            window.blit(font.render("Stop", True, white), (260, 110))
            window.blit(font.render("Previous", True, white), (60, 210))
            window.blit(font.render("Next", True, white), (160, 210))
            window.blit(font.render("Loop", True, white), (260, 210))
            window.blit(font.render("Volume Up", True, white), (60, 310))
            window.blit(font.render("Volume Down", True, white), (160, 310))
            window.blit(font.render("Add", True, white), (260, 310))
            window.blit(font.render("Remove", True, white), (360, 310))
            if len(audio_files) > 0:
                window.blit(font.render(os.path.basename(audio_files[selected_track]), True, black), (50, 50))
            else:
                window.blit(font.render("No tracks", True, black), (50, 50))
            pygame.display.update()

        pygame.quit()
