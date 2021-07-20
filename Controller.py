import pygame
import Logic
import UI

dir1 = dir2 = ''
running = run = True

def game():
    Logic.reset()
    
    global running
    run = False

    while running:
        UI.set_screen()
        UI.start_game()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

        if run: 
            run = False
            break

    while running:
        UI.set_screen()
        UI.show_rules()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

        if run: 
            run = False
            break

    while running:
        UI.set_screen()
        UI.choose_speed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    run = True
                    Logic.set_speed(1)
                if event.key == pygame.K_2:
                    run = True
                    Logic.set_speed(1.5)
                if event.key == pygame.K_3:
                    run = True
                    Logic.set_speed(2)
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

        if run: 
            break
    
    while running:
        UI.set_screen()
        UI.background()
        
        global dir1, dir2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Player 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    dir1 = 'up'
                if event.key == pygame.K_s:
                    dir1 = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    dir1 = 'stop'
            
            #Player 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dir2 = 'up'
                if event.key == pygame.K_DOWN:
                    dir2 = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dir2 = 'stop' 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Logic.ready = True

        #Players
        Logic.p1.move(dir1)
        Logic.p2.move(dir2)
        UI.player1.show_player()
        UI.player2.show_player()

        #Ball
        if Logic.ready:
            Logic.moveBall()
        else:
            UI.start_play()
        UI.ball(Logic.ballX, Logic.ballY)
        
        #Screen
        Logic.score_pt()
        UI.show_score(Logic.score1, 205, 70)
        UI.show_score(Logic.score2, 605, 70)

        pygame.display.update()

        if Logic.checkEnd():
            break
    
    while running:
        UI.set_screen()
        UI.end_game()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

game()