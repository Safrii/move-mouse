import mouse

infinite = True

print("if you want to quit program press ctrl+C")

try:
    while infinite:
        mouse.move(800, 800, True, 0.5)
        mouse.move(500, 500, True, 0.5)
except KeyboardInterrupt:
    exit()
