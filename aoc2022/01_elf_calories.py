with open('elf_calories.txt') as f:
    max = 0
    running = 0
    for line in f.readlines():
        if line == '\n':
            print(running)
            if running >= max:
                max = running
                # print('max: %s' % max)
            running = 0
        else:
            running += int(line)

    # account for last line
    # print('running: %s' % running)
    if running >= max:
        max = running
        # print('max: %s' % max)
