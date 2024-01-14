with open('usernames.txt', 'w') as file:
    for i in range(1, 201):
        file.write(f'VVCE23CSE{str(i).zfill(4)}\n')
