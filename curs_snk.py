import keyboard
import random
import curses

s=curses.initscr()
curses.curs_set(0)
sh, sw = s.getmayxy()
w=curses.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(100)
snk_x=sw/4
snk_y=sh/2
snake = [
    [snk_y, snl_x],
    [snk_y, snl_x-1],
    [snk_y, snl_x-2]
    ]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else nexk_key

    if snake[0][0] in [0, sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN or 'S' or 's':
        new_head[0] += 1
        
    if key == curses.KEY_UP or 'W' or 'w':
        new_head[0] -= 1

    if key == curses.KEY_LEFT or 'A' or 'a':
        new_head[1] -= 1

    if key == curses.KEY_RIGHT or 'D' or 'd':
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1,sh-1),
                random.randint(1,sw-1)
                ]

            food = nf if nf not in snake else None
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    
    



