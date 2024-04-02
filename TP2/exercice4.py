# Fontion fournie ne pas modifier
clearConsole = lambda: print('\n' * 10)

def print_table(table):
    # Dimension 1 = ligne
    # Dimension 2 = colonne
    clearConsole()
    for i, row in enumerate(table):
        row_str = "{:>2}" * len(row)
        row_str = row_str.format(*row)
        print("{:^20}".format(row_str), '\n')

# ________________________________________________________________

# Partie 1
def init_maze(nb_row, nb_col, player_pos, end_pos, walls):
    maze = [] # TODO Générer un labyrinthe vide -> rempli de "_"
    for i in range(0, nb_row):
        maze.append([])
        for j in range(0,nb_col):
            maze[i].append("_")
    # TODO Placer le joueur "O" la sortie "X" les murs "W"
    maze[player_pos[0]][player_pos[1]] = "O" #ligne, col
    maze[end_pos[0]][end_pos[1]] = "X" 
    for w in range(0, len(walls)):        
            maze[walls[w][0]][walls[w][1]] = "W"
    return maze

# Partie 2
def validate_move(maze, new_player_pos):
    result = False
    # TODO Vérifier si la position est valide -> dans le labyrinthe et pas sur un mur    
    if new_player_pos[0] < 0 or new_player_pos[0] >= len(maze):
        return False
    elif new_player_pos[1] < 0 or new_player_pos[1] >= len(maze[0]):
        return False
    elif maze[new_player_pos[0]][new_player_pos[1]] == "_" or maze[new_player_pos[0]][new_player_pos[1]] == "X":
        result = True
    return result

#Partie 3
def move(key_pressed, maze, player_pos):
    move_dic = {"w" : "up", "a" : "left", "s" : "down", "d" : "right"} # TODO Créer le dictionnaire d'équivalence entre la touche appuyée et la direction ("up", "left", "down", "right")

    # TODO Vérifier si la touche appuyée est dans le dictionnaire
    if (key_pressed in move_dic) :
        move = move_dic.get(key_pressed) # TODO Récupérer la direction du mouvement

        # TODO Générer la position potentielle du joueur en fonction de la direction
        new_player_pos = player_pos.copy()

        if move == "up":
            new_player_pos[0] -= 1
        elif move == "left":
            new_player_pos[1] -= 1
        elif move == "down":
            new_player_pos[0] += 1
        elif move == "right":
            new_player_pos[1] += 1
        

        if validate_move(maze, new_player_pos):
            # TODO Changer réellement la position du joueur
            maze[player_pos[0]][player_pos[1]] = "_"
            maze[new_player_pos[0]][new_player_pos[1]] = "O"
            player_pos = new_player_pos
            pass
            

    return maze, player_pos


if __name__ == '__main__':
    nb_row = 4
    nb_col = 7
    player_pos = [0,0]  # TODO Définir la position ligne, colonne sur en haut à gauche
    end_pos = [nb_row-1,nb_col-1]  # TODO Définir la position ligne, colonne sur en bas à droite
    # Coordoné sous la forme (ligne, colone)
    walls = [[0, 1],[1, 1], [1, 2], [1, 3], [1, 5], [2, 1], [2, 5], [3, 3], [3, 5]]
    maze = init_maze(nb_row, nb_col, player_pos, end_pos, walls)

    print_table(maze)

    # TODO Décommenter pour tester votre code en Partie 2
    test_pos = [-1,0] #changez les valeurs pour tester tous les cas possibles
    valid = validate_move(maze, test_pos)
    print(valid)


    # TODO Décommenter pour tester votre code en Partie 3
    while player_pos != end_pos:                  
         key_pressed = input("mouvement : ")
         maze, player_pos = move(key_pressed, maze, player_pos)
         print_table(maze)
    
    print("Vous avez gagnez !")
