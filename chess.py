#-------------------------------------------------------------------------------
# Name:        Chess
#
# Purpose:     Chess in python.
#
# Author:      Daniel Di Giovanni
#
# Created:     02/05/2019
#-------------------------------------------------------------------------------

import pygame
import copy


def chessboard_init():
    """
    Initial chessboard position.
    This function will only be used once per game at the beinning
    """

    # How list works: [permanent colour of square, [piece type, piece colour]]
    first_chessboard = [
                        [[0, [2, 1]], [1, [3, 1]], [0, [4, 1]], [1, [5, 1]],
                        [0, [6, 1]], [1, [4, 1]], [0, [3, 1]], [1, [2, 1]]],

                        [[1, [1, 1]], [0, [1, 1]], [1, [1, 1]], [0, [1, 1]],
                        [1, [1, 1]], [0, [1, 1]], [1, [1, 1]], [0, [1, 1]]],

                        [[0, [0, 0]], [1, [0, 0]], [0, [0, 0]], [1, [0, 0]],
                        [0, [0, 0]], [1, [0, 0]], [0, [0, 0]], [1, [0, 0]]],

                        [[1, [0, 0]], [0, [0, 0]], [1, [0, 0]], [0, [0, 0]],
                        [1, [0, 0]], [0, [0, 0]], [1, [0, 0]], [0, [0, 0]]],

                        [[0, [0, 0]], [1, [0, 0]], [0, [0, 0]], [1, [0, 0]],
                        [0, [0, 0]], [1, [0, 0]], [0, [0, 0]], [1, [0, 0]]],

                        [[1, [0, 0]], [0, [0, 0]], [1, [0, 0]], [0, [0, 0]],
                        [1, [0, 0]], [0, [0, 0]], [1, [0, 0]], [0, [0, 0]]],

                        [[0, [1, 2]], [1, [1, 2]], [0, [1, 2]], [1, [1, 2]],
                        [0, [1, 2]], [1, [1, 2]], [0, [1, 2]], [1, [1, 2]]],

                        [[1, [2, 2]], [0, [3, 2]], [1, [4, 2]], [0, [5, 2]],
                        [1, [6, 2]], [0, [4, 2]], [1, [3, 2]], [0, [2, 2]]],
                        ]

    return first_chessboard


def draw_chessboard(
    current_board, screen_size, surface, w, b, w_p, w_r, w_kn, w_b, w_q, w_ki,
    b_p, b_r, b_kn, b_b, b_q, b_ki):
    """Draws the chessboard"""

    font = pygame.font.SysFont("Calibri", 10, True, False)

    # Starting X and Y coordinates for squares
    x = 0
    y = 0

    # Spacers to make images in the centre
    x_spacer = screen_size[0] // 16 - 25
    y_spacer = screen_size[1] // 16 - 25

    # Get dimension of each square by dividing size by 8
    dimension = screen_size[0] / 8.0

    # Loop for iterating through rows
    for row in range(len(current_board)):

        # Loop for iterating through columns (basically each square)
        for square in range(len(current_board[row])):

            # -- Drawing squares --

            # Check permanent colour of square (0 is white, 1 is black)
            if current_board[row][square][0] == 0:
                # Draw white square
                pygame.draw.rect(surface, w, [x, y, dimension, dimension])

            elif current_board[row][square][0] == 1:
                # Draw black square
                pygame.draw.rect(surface, b, [x, y, dimension, dimension])

            # -- Drawing pieces --

            # Check colour of piece (0 is empty, 1 is white, 2 is black)
            if current_board[row][square][1][1] == 1:

                # Check type of piece (0 is empty, 1 is pawn, 2 is rook,
                # 3 is knight, 4 is bishop, 5 is queen, 6 is king)
                if current_board[row][square][1][0] == 1:
                    # text = font.render("white pawn", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(w_p, [x + x_spacer, y + y_spacer])

                elif current_board[row][square][1][0] == 2:
                    # text = font.render("white rook", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(w_r, [x + x_spacer, y + y_spacer])

                elif current_board[row][square][1][0] == 3:
                    # text = font.render("white knight", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(w_kn, [x + x_spacer, y + y_spacer])

                elif current_board[row][square][1][0] == 4:
                    # text = font.render("white  bishop", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(w_b, [x + x_spacer, y + y_spacer])

                elif current_board[row][square][1][0] == 5:
                    # text = font.render("white queen", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(w_q, [x + x_spacer, y + y_spacer])

                elif current_board[row][square][1][0] == 6:
                    # text = font.render("white king", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(w_ki, [x + x_spacer, y + y_spacer])

            if current_board[row][square][1][1] == 2:

                if current_board[row][square][1][0] == 1:
                    # text = font.render("black pawn", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(b_p, [x + x_spacer, y + y_spacer])

                if current_board[row][square][1][0] == 2:
                    # text = font.render("black rook", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(b_r, [x + x_spacer, y + y_spacer])

                if current_board[row][square][1][0] == 3:
                    # text = font.render("black knight", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(b_kn, [x + x_spacer, y + y_spacer])

                if current_board[row][square][1][0] == 4:
                    # text = font.render("black bishop", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(b_b, [x + x_spacer, y + y_spacer])

                if current_board[row][square][1][0] == 5:
                    # text = font.render("black queen", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(b_q, [x + x_spacer, y + y_spacer])

                if current_board[row][square][1][0] == 6:
                    # text = font.render("black king", True, (218, 150, 10))
                    # surface.blit(text, [x, y])
                    surface.blit(b_ki, [x + x_spacer, y + y_spacer])

            # Increment X coordinate
            x += dimension

        # Set X coordinate back to start (so squares do not continue off-screen)
        x = 0

        # Increment Y coordinate
        y += dimension


def draw_empty_chessboard(screen_size, surface, w, b):
    """Draws the chessboard"""

    font = pygame.font.SysFont("Calibri", 10, True, False)

    # Starting X and Y coordinates for squares
    x = 0
    y = 0

    # Spacers to make images in the centre
    x_spacer = screen_size[0] // 16 - 25
    y_spacer = screen_size[1] // 16 - 25

    # Get dimension of each square by dividing size by 8
    dimension = screen_size[0] / 8.0

    # Loop for iterating through rows
    for i in range(8):

        # Loop for iterating through columns (basically each square)
        for j in range(8):

            # -- Drawing squares --

            if i % 2 == 0:
                # Check permanent colour of square (0 is white, 1 is black)
                if j % 2 == 0:
                    # Draw white square
                    pygame.draw.rect(surface, w, [x, y, dimension, dimension])

                else:
                    # Draw black square
                    pygame.draw.rect(surface, b, [x, y, dimension, dimension])

            else:
                # Check permanent colour of square (0 is white, 1 is black)
                if j % 2 == 0:
                    # Draw white square
                    pygame.draw.rect(surface, b, [x, y, dimension, dimension])

                else:
                    # Draw black square
                    pygame.draw.rect(surface, w, [x, y, dimension, dimension])

            # Increment X coordinate
            x += dimension

        # Set X coordinate back to start (so squares do not continue off-screen)
        x = 0

        # Increment Y coordinate
        y += dimension


def click_position_on_board(click_pos, board_size):
    """Finds the square that was clicked"""

    margin_size = 0  # Just for now margin size will be 0

    # Get board position by floor-dividing coordinates by square size
    board_click_x = click_pos[0] // (board_size[0] // 8) + margin_size
    board_click_y = click_pos[1] // (board_size[1] // 8) + margin_size

    # Store position in a tuple
    board_click_pos = (board_click_x, board_click_y)

    # REMEMBER that the index starts at 0, so top-left square is (0, 0) and
    # bottom-right square is (7, 7)

    return board_click_pos


def square_information(board_click_pos, current_board):
    """
    Returns the information of the square that was clicked.
    Piece, piece colour, etc.
    """

    # Get the piece type and colour from converting the square that was clicked
    # into an index of the chessboard list
    piece_type = current_board[board_click_pos[1]][board_click_pos[0]][1][0]
    piece_colour = current_board[board_click_pos[1]][board_click_pos[0]][1][1]

    return (piece_type, piece_colour)


def piece_selected(click_info, player_turn):
    """Finds if piece is slected with the current click"""

    # Check if player clicked on their own piece, return True or False
    # accordingly
    if player_turn == click_info[1]:
        piece_is_selected = True

    else:
        piece_is_selected = False

    return piece_is_selected


def piece_possibly_moving(click_info, player_turn):
    """
    Finds if user clicked on a square that does not have their piece on it.
    If so, then return True so that it can be checked if the square clicked is
    valid.
    """

    # Check is player did not click on their own piece, return True or False
    # accordingly
    if player_turn != click_info[1]:
        piece_is_possibly_moving = True

    else:
        piece_is_possibly_moving = False

    return piece_is_possibly_moving


def movement_possibilties(
    click_info, board_click_pos, current_board, player_turn):
    """Finds all possible squares that a slected piece can move to"""

    possible_moves = []

    x_square = board_click_pos[0]
    y_square = board_click_pos[1]

    # - Check what piece identity is -

    # Piece is a pawn
    if click_info[0] == 1:

        # White's turn
        if player_turn == 1:

            try:
                # 1 square ahead
                if current_board[y_square + 1][x_square][1][1] == 0:

                    # Board position of selected piece
                    starting_pos = [x_square, y_square]
                    # Board position of piece's destination
                    ending_pos = [x_square, y_square + 1]
                    # Information of the selected square
                    starting_pos_info = current_board[y_square][x_square][1]

                    # Make a copy of the chessboard to use in checking for
                    # valid moves
                    use_board = copy.deepcopy(current_board)

                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does not
                    # get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Append to possible moves if king is not in check
                    if king_pos not in all_enemy_moves:
                        # - Add to list -
                        # Prevents negative numbers
                        if x_square >= 0 and y_square + 1 >= 0:
                            possible_moves.append([x_square, y_square + 1])

            # Pawn has reached the other side
            except IndexError:
                pass

            # 2 squares ahead; can only happen if pawn is in starting position
            if y_square == 1 and \
                    current_board[y_square + 2][x_square][1][1] == 0 and \
                    current_board[y_square + 1][x_square][1][1] == 0:

                    # Board position of selected piece
                    starting_pos = [x_square, y_square]
                    # Board position of piece's destination
                    ending_pos = [x_square, y_square + 2]
                    # Information of the selected square
                    starting_pos_info = current_board[y_square][x_square][1]

                    # Make a copy of the chessboard to use in checking for
                    # valid moves
                    use_board = copy.deepcopy(current_board)

                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does not
                    # get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Append to possible moves if king is not in check
                    if king_pos not in all_enemy_moves:
                        # Prevents negative numbers
                        if x_square >= 0 and y_square + 2 >= 0:
                            possible_moves.append([x_square, y_square + 2])

            try:
                # 1 square up, 1 square to the right, enemy piece is there
                if current_board[y_square + 1][x_square + 1][1][1] == 2:

                    # Board position of selected piece
                    starting_pos = [x_square, y_square]
                    # Board position of piece's destination
                    ending_pos = [x_square + 1, y_square + 1]
                    # Information of the selected square
                    starting_pos_info = current_board[y_square][x_square][1]

                    # Make a copy of the chessboard to use in checking for
                    # valid moves
                    use_board = copy.deepcopy(current_board)

                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does
                    # not get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Append to possible moves if king is not in check
                    if king_pos not in all_enemy_moves:
                        # Prevents negative numbers
                        if x_square + 1 >= 0 and y_square + 1 >= 0:
                            possible_moves.append([x_square + 1, y_square + 1])

            except IndexError:
                pass

            try:
                # 1 square up, 1 square to the left, enemy piece is there
                if current_board[y_square + 1][x_square - 1][1][1] == 2:

                    # Board position of selected piece
                    starting_pos = [x_square, y_square]
                    # Board position of piece's destination
                    ending_pos = [x_square - 1, y_square + 1]
                    # Information of the selected square
                    starting_pos_info = current_board[y_square][x_square][1]

                    # Make a copy of the chessboard to use in checking for
                    # valid moves
                    use_board = copy.deepcopy(current_board)

                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does
                    # not get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Append to possible moves if king is not in check
                    if king_pos not in all_enemy_moves:
                        # Prevents negative numbers
                        if x_square - 1 >= 0 and y_square + 1 >= 0:
                            possible_moves.append([x_square - 1, y_square + 1])

            except IndexError:
                pass

        # Black's turn
        else:

            try:
                # 1 square ahead
                if current_board[y_square - 1][x_square][1][1] == 0:

                    # Board position of selected piece
                    starting_pos = [x_square, y_square]
                    # Board position of piece's destination
                    ending_pos = [x_square , y_square - 1]
                    # Information of the selected square
                    starting_pos_info = current_board[y_square][x_square][1]

                    # Make a copy of the chessboard to use in checking for
                    # valid moves
                    use_board = copy.deepcopy(current_board)

                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does
                    # not get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Append to possible moves if king is not in check
                    if king_pos not in all_enemy_moves:
                        # Prevents negative numbers
                        if x_square >= 0 and y_square - 1 >= 0:
                            # - Add to list -
                            possible_moves.append([x_square, y_square - 1])

            # Pawn has reached the other side
            except IndexError:
                pass

            # 2 squares ahead; can only happen if pawn is in starting position
            if y_square == 6 and \
                    current_board[y_square - 2][x_square][1][1] == 0 and \
                    current_board[y_square - 1][x_square][1][1] == 0:

                    # Board position of selected piece
                    starting_pos = [x_square, y_square]
                    # Board position of piece's destination
                    ending_pos = [x_square, y_square - 2]
                    # Information of the selected square
                    starting_pos_info = current_board[y_square][x_square][1]

                    # Make a copy of the chessboard to use in checking for
                    # valid moves
                    use_board = copy.deepcopy(current_board)

                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does
                    # not get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Append to possible moves if king is not in check
                    if king_pos not in all_enemy_moves:
                        # Prevents negative numbers
                        if x_square >= 0 and y_square - 2 >= 0:
                            possible_moves.append([x_square, y_square - 2])

            try:
                # 1 square up, 1 square to the right, enemy piece is there
                if current_board[y_square - 1][x_square + 1][1][1] == 1:

                    # Board position of selected piece
                    starting_pos = [x_square, y_square]
                    # Board position of piece's destination
                    ending_pos = [x_square + 1, y_square - 1]
                    # Information of the selected square
                    starting_pos_info = current_board[y_square][x_square][1]

                    # Make a copy of the chessboard to use in checking for
                    # valid moves
                    use_board = copy.deepcopy(current_board)

                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does
                    # not get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Append to possible moves if king is not in check
                    if king_pos not in all_enemy_moves:
                        # Prevents negative numbers
                        if x_square + 1 >= 0 and y_square - 1 >= 0:
                            possible_moves.append([x_square + 1, y_square - 1])

            except IndexError:
                pass

            try:
                # 1 square up, 1 square to the left, enemy piece is there
                if current_board[y_square - 1][x_square - 1][1][1] == 1:

                    # Board position of selected piece
                    starting_pos = [x_square, y_square]
                    # Board position of piece's destination
                    ending_pos = [x_square - 1, y_square - 1]
                    # Information of the selected square
                    starting_pos_info = current_board[y_square][x_square][1]

                    # Make a copy of the chessboard to use in checking for
                    # valid moves
                    use_board = copy.deepcopy(current_board)

                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does
                    # not get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Append to possible moves if king is not in check
                    if king_pos not in all_enemy_moves:
                        # Prevents negative numbers
                        if x_square - 1 >= 0 and y_square - 1 >= 0:
                            possible_moves.append([x_square - 1, y_square - 1])

            except IndexError:
                pass

    # Piece is rook
    elif click_info[0] == 2:

        # Loop for iterating through directions
        for direction in range(4):
            # First iteration is right
            if direction == 0:
                next_x = 1
                next_y = 0
            # Second iteration is left
            elif direction == 1:
                next_x = -1
                next_y = 0
            # Third iteration is up
            elif direction == 2:
                next_x = 0
                next_y = -1
            # Fourth iteration is down
            else:
                next_x = 0
                next_y = 1

            # Next loop will run
            done_finding = False

            square_counter = 1

            # Loop for iterating through squares
            while not done_finding:

                # Board position of selected piece
                starting_pos = [x_square, y_square]
                # Board position of piece's destination
                ending_pos = [
                    x_square + square_counter * next_x,
                    y_square + square_counter * next_y
                    ]

                # Information of the selected square
                starting_pos_info = current_board[y_square][x_square][1]

                # Make a copy of the chessboard to use in checking for
                # valid moves
                use_board = copy.deepcopy(current_board)

                # Index error used to detect border
                try:
                    # Current square has friendly piece
                    if current_board[y_square + square_counter * next_y] \
                            [x_square + square_counter * next_x][1][1] \
                            == player_turn:

                        done_finding = True

                    # Current square is not friendly piece
                    else:
                        # Copy of the chessboard with the after this
                        # possible move
                        # Deep copy of board used so that actual chessboard does
                        # not get changed
                        copy_b = change_board(
                            use_board, starting_pos, ending_pos,
                            starting_pos_info
                            )

                        # Get all possibilities of enemy on the new,
                        # theoretical board
                        all_enemy_moves = enemy_possibilities(
                            copy_b, player_turn)

                        # Get the player's own king position on the new,
                        # thoretical board
                        king_pos = king_position(copy_b, player_turn)

                        # Prevent negative numbers
                        if y_square + square_counter * next_y >= 0 and \
                                x_square + square_counter * next_x >= 0:

                            # Append to possible moves if king is not in check
                            if king_pos not in all_enemy_moves:
                                # Next square is empty
                                if current_board[
                                        y_square + square_counter * next_y] \
                                        [x_square + square_counter * next_x] \
                                        [1][1] == 0:

                                    possible_moves.append(
                                        [
                                        x_square + square_counter * next_x,
                                        y_square + square_counter * next_y
                                        ])

                                # Current square has enemy piece
                                else:
                                    possible_moves.append(
                                        [
                                        x_square + square_counter * next_x,
                                        y_square + square_counter * next_y
                                        ])

                                    done_finding = True

                # Board limit reached
                except IndexError:
                    done_finding = True

                square_counter += 1

    # Piece is knight
    elif click_info[0] == 3:

        # Loop for iterating through movements (knight has 8 movements)
        for movement in range(8):
            # For the first half of the movements, Y will be 2 and X will be 1
            if movement < 4:
                y_move = 2
                x_move = 1
            # X and Y switch for the second half of the movements
            else:
                y_move = 1
                x_move = 2
            # Y is negative at movements 2, 3, and 6, 7
            if movement > 1 and movement < 4 or movement > 5:
                y_move *= -1
            # Every other X movement is negative
            if movement % 2 == 0:
                x_move *= -1

            # Board position of selected piece
            starting_pos = [x_square, y_square]
            # Board position of piece's destination
            ending_pos = [x_square + x_move, y_square + y_move]
            # Information of the selected square
            starting_pos_info = current_board[y_square][x_square][1]

            # Make a copy of the chessboard to use in checking for valid moves
            use_board = copy.deepcopy(current_board)

            # Index error used to detect border
            try:
                # Append to possible movements list if target square is empty
                # or has enemy piece on it
                if current_board[y_square + y_move][x_square + x_move][1][1] \
                        != player_turn:

                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does
                    # not get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Prevent negative numbers
                    if x_square + x_move >= 0 and y_square + y_move >= 0:

                        # Append to possible moves if king is not in check
                        if king_pos not in all_enemy_moves:
                            possible_moves.append(
                                [x_square + x_move, y_square + y_move])

            except IndexError:
                pass

    # Piece is bishop
    elif click_info[0] == 4:

        # Loop for iterating through directions
        for direction in range(4):
            # First direction is right, up
            if direction == 0:
                next_x = 1
                next_y = -1
            # Second direction is right, down
            elif direction == 1:
                next_x = 1
                next_y = 1
            # Third direction is left, up
            elif direction == 2:
                next_x = -1
                next_y = 1
            # Fourth direction is left, down
            else:
                next_x = -1
                next_y = -1

            # Next loop will run
            done_finding = False

            square_counter = 1

            # Loop for iterating through each square
            while not done_finding:

                # Board position of selected piece
                starting_pos = [x_square, y_square]
                # Board position of piece's destination
                ending_pos = [
                    x_square + square_counter * next_x,
                    y_square + square_counter * next_y
                    ]

                # Information of the selected square
                starting_pos_info = current_board[y_square][x_square][1]

                # Make a copy of the chessboard to use in checking for
                # valid moves
                use_board = copy.deepcopy(current_board)

                # Index error used to detect border
                try:
                    # Current square has friendly piece
                    if current_board[y_square + square_counter * next_y] \
                            [x_square + square_counter * next_x][1][1] \
                            == player_turn:
                        done_finding = True

                    # Current square does not have friendly piece
                    else:
                        # Copy of the chessboard with the after this
                        # possible move
                        # Deep copy of board used so that actual chessboard does
                        # not get changed
                        copy_b = change_board(
                            use_board, starting_pos, ending_pos,
                            starting_pos_info)

                        # Get all possibilities of enemy on the new,
                        # theoretical board
                        all_enemy_moves = enemy_possibilities(
                            copy_b, player_turn)

                        # Get the player's own king position on the new,
                        # thoretical board
                        king_pos = king_position(copy_b, player_turn)

                        # Prevent negative numbers
                        if y_square + square_counter * next_y >= 0 and \
                                x_square + square_counter * next_x >= 0:

                            # Append to possible moves if king is not in check
                            if king_pos not in all_enemy_moves:

                                # Current square empty
                                if current_board \
                                        [y_square + square_counter * next_y] \
                                        [x_square + square_counter * next_x] \
                                        [1][1] == 0:
                                    possible_moves.append(
                                        [
                                        x_square + square_counter * next_x,
                                        y_square + square_counter * next_y
                                        ])

                                # Current square has enemy piece
                                else:
                                    possible_moves.append(
                                        [
                                        x_square + square_counter * next_x,
                                        y_square + square_counter * next_y
                                        ])
                                    done_finding = True

                    square_counter += 1

                except IndexError:
                    done_finding = True

    # Piece is queen
    elif click_info[0] == 5:

        # Loop for iterating through directions
        for direction in range(8):
            # First iteration is right
            if direction == 0:
                next_x = 1
                next_y = 0
            # Second iteration is right, up
            if direction == 1:
                next_x = 1
                next_y = -1
            # Third iteration is up
            if direction == 2:
                next_x = 0
                next_y = -1
            # Fourth iteration is left, up
            if direction == 3:
                next_x = -1
                next_y = -1
            # Fifth iteration left
            if direction == 4:
                next_x = -1
                next_y = 0
            # Sixth iteration is left, down
            if direction == 5:
                next_x = -1
                next_y = 1
            # Seventh iteration is down
            if direction == 6:
                next_x = 0
                next_y = 1
            # Eighth iteration is right, down
            if direction == 7:
                next_x = 1
                next_y = 1

            # Next loop will run
            done_finding = False

            square_counter = 1

            # Loop for iterating through squares
            while not done_finding:

                # Board position of selected piece
                starting_pos = [x_square, y_square]
                # Board position of piece's destination
                ending_pos = [
                    x_square + square_counter * next_x,
                    y_square + square_counter * next_y
                    ]

                # Information of the selected square
                starting_pos_info = current_board[y_square][x_square][1]

                # Make a copy of the chessboard to use in checking for
                # valid moves
                use_board = copy.deepcopy(current_board)

                # Index error used to detect border
                try:
                    # Current square has friendly piece on it
                    if current_board[y_square + square_counter * next_y] \
                            [x_square + square_counter * next_x][1][1] \
                            == player_turn:
                        done_finding = True

                    # Current square does not have friendly piece
                    else:
                        # Copy of the chessboard with the after this
                        # possible move
                        # Deep copy of board used so that actual chessboard does
                        # not get changed
                        copy_b = change_board(
                            use_board, starting_pos, ending_pos,
                            starting_pos_info)

                        # Get all possibilities of enemy on the new,
                        # theoretical board
                        all_enemy_moves = enemy_possibilities(
                            copy_b, player_turn)

                        # Get the player's own king position on the new,
                        # thoretical board
                        king_pos = king_position(copy_b, player_turn)

                        # Prevent negative numbers
                        if y_square + square_counter * next_y >= 0 and \
                                x_square + square_counter * next_x >= 0:

                            # Append to possible moves if king is not in check
                            if king_pos not in all_enemy_moves:
                                # Curent square is empty
                                if current_board \
                                        [y_square + square_counter * next_y] \
                                        [x_square + square_counter * next_x] \
                                        [1][1] == 0:

                                    possible_moves.append(
                                        [
                                        x_square + square_counter * next_x,
                                        y_square + square_counter * next_y
                                        ])

                                # Current square has enemy piece
                                else:
                                    possible_moves.append(
                                        [
                                        x_square + square_counter * next_x,
                                        y_square + square_counter * next_y
                                        ])
                                    done_finding = True

                except IndexError:
                    done_finding = True

                square_counter += 1

    # Piece is king
    elif click_info[0] == 6:
        # Loop for iterating through directions
        for direction in range(8):
            # First iteration is right
            if direction == 0:
                next_x = 1
                next_y = 0
            # Second iteration is right, up
            if direction == 1:
                next_x = 1
                next_y = -1
            # Third iteration is up
            if direction == 2:
                next_x = 0
                next_y = -1
            # Fourth iteration is left, up
            if direction == 3:
                next_x = -1
                next_y = -1
            # Fifth iteration left
            if direction == 4:
                next_x = -1
                next_y = 0
            # Sixth iteration is left, down
            if direction == 5:
                next_x = -1
                next_y = 1
            # Seventh iteration is down
            if direction == 6:
                next_x = 0
                next_y = 1
            # Eighth iteration is right, down
            if direction == 7:
                next_x = 1
                next_y = 1

            # Board position of selected piece
            starting_pos = [x_square, y_square]
            # Board position of piece's destination
            ending_pos = [x_square + 1 * next_x, y_square + 1 * next_y]
            # Information of the selected square
            starting_pos_info = current_board[y_square][x_square][1]

            # Make a copy of the chessboard to use in checking for valid moves
            use_board = copy.deepcopy(current_board)

            # Index error used to detect border
            try:
                # Current square has friendly piece on it
                if current_board[y_square + 1 * next_y][x_square + 1 * next_x] \
                        [1][1] == player_turn:
                    pass

                # Current square does not have friendly piece
                else:
                    # Copy of the chessboard with the after this possible move
                    # Deep copy of board used so that actual chessboard does
                    # not get changed
                    copy_b = change_board(
                        use_board, starting_pos, ending_pos, starting_pos_info)

                    # Get all possibilities of enemy on the new,
                    # theoretical board
                    all_enemy_moves = enemy_possibilities(copy_b, player_turn)

                    # Get the player's own king position on the new,
                    # thoretical board
                    king_pos = king_position(copy_b, player_turn)

                    # Prevent negative numbers
                    if y_square + 1 * next_y >= 0 and \
                            x_square + 1 * next_x >= 0:
                        # Append to possible moves if king is not in check
                        if king_pos not in all_enemy_moves:
                            # Curent square is empty
                            if current_board[y_square + 1 * next_y] \
                                    [x_square + 1 * next_x][1][1] == 0:

                                possible_moves.append(
                                    [
                                    x_square + 1 * next_x,
                                    y_square + 1 * next_y
                                    ])

                            # Current square has enemy piece
                            else:
                                possible_moves.append(
                                [
                                x_square + 1 * next_x,
                                y_square + 1 * next_y
                                ])

            except IndexError:
                pass

    return possible_moves


def king_position(current_chessboard, player_turn):
    """Finds the position of the player's king on the chessboard"""

    # Loop for iterating through rows
    for row in range(len(current_chessboard)):
        # Loop for iterating thruogh each square
        for square in range(len(current_chessboard[row])):
            # Check if that square has king
            if current_chessboard[row][square][1][0] == 6 and \
                    current_chessboard[row][square][1][1] == player_turn:
                position_of_king = [square, row]

    return position_of_king


def enemy_possibilities(current_board, player_turn):
    """Returns every movement possibility of the enemy"""

    possible_moves = []

    if player_turn == 1:
        player_turn = 2
    elif player_turn == 2:
        player_turn = 1

    for row in range(len(current_board)):
        for square in range(len(current_board[row])):

            x_square = square
            y_square = row

            if current_board[row][square][1][1] == player_turn:

                if current_board[row][square][1][0] == 0:
                    pass
                # - Check what piece identity is -

                # Piece is a pawn
                elif current_board[y_square][x_square][1][0] == 1:

                    # White's turn
                    if player_turn == 1:

                        try:
                            # 1 square ahead
                            if current_board[y_square + 1][x_square][1][1] == 0:
                                # - Add to list -
                                possible_moves.append([x_square, y_square + 1])

                        # Pawn has reached the other side
                        except IndexError:
                            pass

                        # 2 squares ahead; can only happen if pawn is in
                        # starting position
                        if y_square == 1 and current_board \
                                [y_square + 2][x_square][1][1] == 0 and \
                                current_board[y_square + 1][x_square][1][1] \
                                == 0:
                            possible_moves.append([x_square, y_square + 2])

                        try:
                            # 1 square up, 1 square to the right, enemy piece
                            # is there
                            if current_board[y_square + 1][x_square + 1][1][1] \
                                    == 2:
                                possible_moves.append(
                                    [x_square + 1, y_square + 1])

                        except IndexError:
                            pass

                        try:
                            # 1 square up, 1 square to the left, enemy piece
                            # is there
                            if current_board[y_square + 1][x_square - 1][1][1] \
                                    == 2:
                                possible_moves.append(
                                    [x_square - 1, y_square + 1])

                        except IndexError:
                            pass

                    # Black's turn
                    else:

                        try:
                            # 1 square ahead
                            if current_board[y_square - 1][x_square][1][1] == 0:
                                # - Add to list -
                                possible_moves.append([x_square, y_square - 1])

                        # Pawn has reached the other side
                        except IndexError:
                            pass

                        # 2 squares ahead; can only happen if pawn is in
                        # starting position
                        if y_square == 6 and current_board \
                                [y_square - 2][x_square][1][1] == 0 and \
                                current_board[y_square - 1][x_square][1][1] \
                                == 0:
                            possible_moves.append([x_square, y_square - 2])

                        try:
                            # 1 square up, 1 square to the right, enemy piece
                            # is there
                            if current_board[y_square - 1][x_square + 1][1][1] \
                                    == 1:
                                possible_moves.append(
                                    [x_square + 1, y_square - 1])

                        except IndexError:
                            pass

                        try:
                            # 1 square up, 1 square to the left, enemy piece
                            # is there
                            if current_board[y_square - 1][x_square - 1][1][1] \
                                    == 1:
                                possible_moves.append(
                                    [x_square - 1, y_square - 1])

                        except IndexError:
                            pass

                # Piece is rook
                elif current_board[y_square][x_square][1][0] == 2:

                    # Loop for iterating through directions
                    for direction in range(4):
                        # First iteration is right
                        if direction == 0:
                            next_x = 1
                            next_y = 0
                        # Second iteration is left
                        elif direction == 1:
                            next_x = -1
                            next_y = 0
                        # Third iteration is up
                        elif direction == 2:
                            next_x = 0
                            next_y = -1
                        # Fourth iteration is down
                        else:
                            next_x = 0
                            next_y = 1

                        # Next loop will run
                        done_finding = False

                        square_counter = 1

                        # Loop for iterating through squares
                        while not done_finding:

                            # Index error used to detect border
                            try:
                                # Current square has friendly piece
                                if current_board \
                                        [y_square + square_counter * next_y] \
                                        [x_square + square_counter * next_x] \
                                        [1][1] == player_turn:

                                    done_finding = True

                                # Current square is not friendly piece
                                else:
                                    # Next square is empty
                                    if current_board \
                                        [y_square + square_counter * next_y] \
                                        [x_square + square_counter * next_x] \
                                        [1][1] == 0:

                                        # Append to list
                                        possible_moves.append(
                                            [x_square + square_counter * next_x,
                                            y_square + square_counter * next_y])

                                    # Current square has enemy piece
                                    else:
                                        possible_moves.append(
                                            [x_square + square_counter * next_x,
                                            y_square + square_counter * next_y])

                                        done_finding = True

                            # Board limit reached
                            except IndexError:
                                done_finding = True

                            square_counter += 1

                # Piece is knight
                elif current_board[y_square][x_square][1][0] == 3:

                    # Loop for iterating through movements
                    # (knight has 8 movements)
                    for movement in range(8):
                        # For the first half of the movements, Y will be 2
                        # and X will be 1
                        if movement < 4:
                            y_move = 2
                            x_move = 1
                        # X and Y switch for the second half of the movements
                        else:
                            y_move = 1
                            x_move = 2
                        # Y is negative at movements 2, 3, and 6, 7
                        if movement > 1 and movement < 4 or movement > 5:
                            y_move *= -1
                        # Every other X movement is negative
                        if movement % 2 == 0:
                            x_move *= -1

                        # Index error used to detect border
                        try:
                            # Append to possible movements list if target square
                            # is empty or has enemy piece on it
                            if current_board[y_square + y_move] \
                                    [x_square + x_move] \
                                    [1][1] != player_turn:

                                possible_moves.append(
                                    [x_square + x_move, y_square + y_move])

                        except IndexError:
                            pass

                # Piece is bishop
                elif current_board[y_square][x_square][1][0] == 4:

                    # Loop for iterating through directions
                    for direction in range(4):
                        # First direction is right, up
                        if direction == 0:
                            next_x = 1
                            next_y = -1
                        # Second direction is right, down
                        elif direction == 1:
                            next_x = 1
                            next_y = 1
                        # Third direction is left, up
                        elif direction == 2:
                            next_x = -1
                            next_y = 1
                        # Fourth direction is left, down
                        else:
                            next_x = -1
                            next_y = -1

                        # Next loop will run
                        done_finding = False

                        square_counter = 1

                        # Loop for iterating through each square
                        while not done_finding:

                            # Index error used to detect border
                            try:
                                # Current square has friendly piece
                                if current_board \
                                        [y_square + square_counter * next_y] \
                                        [x_square + square_counter * next_x] \
                                        [1][1] == player_turn:
                                    done_finding = True

                                # Current square does not have friendly piece
                                else:
                                    # Current square empty
                                    if current_board \
                                        [y_square + square_counter * next_y] \
                                        [x_square + square_counter * next_x] \
                                        [1][1] == 0:

                                        # Append to list
                                        possible_moves.append(
                                            [x_square + square_counter * next_x,
                                            y_square + square_counter * next_y])

                                    # Current square has enemy piece
                                    else:
                                        possible_moves.append(
                                            [x_square + square_counter * next_x,
                                            y_square + square_counter * next_y])
                                        done_finding = True

                                square_counter += 1

                            except IndexError:
                                done_finding = True

                # Piece is queen
                elif current_board[y_square][x_square][1][0] == 5:

                    # Loop for iterating through directions
                    for direction in range(8):
                        # First iteration is right
                        if direction == 0:
                            next_x = 1
                            next_y = 0
                        # Second iteration is right, up
                        if direction == 1:
                            next_x = 1
                            next_y = -1
                        # Third iteration is up
                        if direction == 2:
                            next_x = 0
                            next_y = -1
                        # Fourth iteration is left, up
                        if direction == 3:
                            next_x = -1
                            next_y = -1
                        # Fifth iteration left
                        if direction == 4:
                            next_x = -1
                            next_y = 0
                        # Sixth iteration is left, down
                        if direction == 5:
                            next_x = -1
                            next_y = 1
                        # Seventh iteration is down
                        if direction == 6:
                            next_x = 0
                            next_y = 1
                        # Eighth iteration is right, down
                        if direction == 7:
                            next_x = 1
                            next_y = 1

                        # Next loop will run
                        done_finding = False

                        square_counter = 1

                        # Loop for iterating through squares
                        while not done_finding:

                            # Index error used to detect border
                            try:
                                # Current square has friendly piece on it
                                if current_board \
                                        [y_square + square_counter * next_y] \
                                        [x_square + square_counter * next_x] \
                                        [1][1] == player_turn:
                                    done_finding = True

                                # Current square does not have friendly piece
                                else:
                                    # Curent square is empty
                                    if current_board \
                                        [y_square + square_counter * next_y] \
                                        [x_square + square_counter * next_x] \
                                        [1][1] == 0:

                                        # Append to list
                                        possible_moves.append(
                                            [x_square + square_counter * next_x,
                                            y_square + square_counter * next_y])

                                    # Current square has enemy piece
                                    else:
                                        possible_moves.append(
                                            [x_square + square_counter * next_x,
                                            y_square + square_counter * next_y])
                                        done_finding = True

                            except IndexError:
                                done_finding = True

                            square_counter += 1

                # Piece is king
                elif current_board[y_square][x_square][1][0] == 6:
                    # Loop for iterating through directions
                    for direction in range(8):
                        # First iteration is right
                        if direction == 0:
                            next_x = 1
                            next_y = 0
                        # Second iteration is right, up
                        if direction == 1:
                            next_x = 1
                            next_y = -1
                        # Third iteration is up
                        if direction == 2:
                            next_x = 0
                            next_y = -1
                        # Fourth iteration is left, up
                        if direction == 3:
                            next_x = -1
                            next_y = -1
                        # Fifth iteration left
                        if direction == 4:
                            next_x = -1
                            next_y = 0
                        # Sixth iteration is left, down
                        if direction == 5:
                            next_x = -1
                            next_y = 1
                        # Seventh iteration is down
                        if direction == 6:
                            next_x = 0
                            next_y = 1
                        # Eighth iteration is right, down
                        if direction == 7:
                            next_x = 1
                            next_y = 1

                        # Index error used to detect border
                        try:
                            # Current square has friendly piece on it
                            if current_board[y_square + 1 * next_y] \
                                    [x_square + 1 * next_x][1][1] \
                                    == player_turn:
                                pass

                            # Current square does not have friendly piece
                            else:

                                # Curent square is empty
                                if current_board[y_square + 1 * next_y] \
                                        [x_square + 1 * next_x][1][1] == 0:

                                    possible_moves.append(
                                        [x_square + 1 * next_x,
                                        y_square + 1 * next_y])

                                # Current square has enemy piece
                                else:
                                    possible_moves.append(
                                        [x_square + 1 * next_x,
                                        y_square + 1 * next_y])

                        except IndexError:
                            pass

    return possible_moves


def friendly_movement_possibilities(board, player_turn):
    """Returns list of friendly moves"""

    friendly_moves = []

    # Loop for iterating through rows
    for row in range(len(board)):
        # Loop for iterating through squares
        for square in range(len(board[row])):
            # Get the square to check and the information of the square
            checking_pos = [square, row]
            checking_pos_info = board[row][square][1]

            # Check if piece on the square is friendly
            if checking_pos_info[1] == player_turn:
                # Get the movement possibilities of the piece
                partial_friendly_moves = movement_possibilties(
                    checking_pos_info, checking_pos, board, player_turn)

                # Only append to list of friendly movement possibilities if the
                # piece has movement possibilities
                if len(partial_friendly_moves) != 0:
                    friendly_moves.append(partial_friendly_moves)

    return friendly_moves


def highlight_movement_options(
    board_click_pos, current_board, possible_moves, surface, b, board_size,
    squares_to_highlight):
    """Highlights square clicked and possible movement possibilities"""

    # Spacers to centre dots
    x_spacer = board_size[0] // 16 - 5
    y_spacer = board_size[1] // 16 - 5

    # Highlight the square being clicked
    square_highlight_pos_x = (board_click_pos[0] * (board_size[0] // 8)) + \
        x_spacer
    square_highlight_pos_y = (board_click_pos[1] * (board_size[1] // 8)) + \
        y_spacer
    pygame.draw.ellipse(
        surface, b, [square_highlight_pos_x, square_highlight_pos_y, 10, 10])

    # Get coordinates to highlight
    # MAY NEED TO ADD MARGINS LATER

    # Loop for iterating through possible movements
    for square in squares_to_highlight:

        # Get X and Y coordinates of and highlight square using the coordinates
        square_highlight_pos_x = (square[0] * (board_size[0] // 8)) + x_spacer
        square_highlight_pos_y = (square[1] * (board_size[1] // 8)) + y_spacer

        pygame.draw.ellipse(
            surface, b, [square_highlight_pos_x, square_highlight_pos_y,
            10, 10])


def highlight_check(current_board, king_pos, board_size, surface, r):
    """Highlights king in check"""
    # Get X and Y coordinates of and highlight square using the coordinates
    square_highlight_pos_x = (king_pos[0] * (board_size[0] // 8)) + 30
    square_highlight_pos_y = (king_pos[1] * (board_size[1] // 8)) + 30

    pygame.draw.ellipse(
        surface, r, [square_highlight_pos_x, square_highlight_pos_y, 20, 20])


def piece_can_move(possible_moves, board_click_pos):
    """Determines if selected square can be moved to, returns True or False"""

    # Check if the square that was ckicked is in the list of possible moves,
    # return True or False accordingly
    if [board_click_pos[0], board_click_pos[1]] in possible_moves:
        can_move = True

    else:
        can_move = False

    return can_move


def change_board(
    current_chessboard, start_square, end_square, starting_click_info):
    """
    Once a piece is moved, this function changes the list to represent the new
    chessboard after the movement
    """

    # Set starting square to empty, set ending square to the moved piece
    current_chessboard[start_square[1]][start_square[0]][1] = [0, 0]
    current_chessboard[end_square[1]][end_square[0]][1] = \
        [starting_click_info[0], starting_click_info[1]]

    return current_chessboard


def load_text_files():
    """Loads text files for instructions"""

    pawn_file = open("texts/pawn.txt", "r")
    pawn_lines = pawn_file.readlines()
    pawn_file.close()

    pawn_promotion_file = open("texts/pawn_promotion.txt", "r")
    pawn_promotion_lines = pawn_promotion_file.readlines()
    pawn_promotion_file.close()

    rook_file = open("texts/rook.txt", "r")
    rook_lines = rook_file.readlines()
    rook_file.close()

    knight_file = open("texts/knight.txt", "r")
    knight_lines = knight_file.readlines()
    knight_file.close()

    bishop_file = open("texts/bishop.txt", "r")
    bishop_lines = bishop_file.readlines()
    bishop_file.close()

    queen_file = open("texts/queen.txt", "r")
    queen_lines = queen_file.readlines()
    queen_file.close()

    king_file = open("texts/king.txt", "r")
    king_lines = king_file.readlines()
    king_file.close()

    check_file = open("texts/check.txt", "r")
    check_lines = check_file.readlines()
    check_file.close()

    stalemate_file = open("texts/stalemate.txt", "r")
    stalemate_lines = stalemate_file.readlines()
    stalemate_file.close()

    pause_file = open("texts/pause.txt", "r")
    pause_lines = pause_file.readlines()
    pause_file.close()

    full_lines = [
        pawn_lines, pawn_promotion_lines, rook_lines, knight_lines,
        bishop_lines, queen_lines, king_lines, check_lines, stalemate_lines,
        pause_lines
        ]

    return full_lines


def draw_button(surface,  colour, x_pos, y_pos, length, width):
    """Draws buttons"""

    pygame.draw.rect(surface, colour, [x_pos, y_pos, length, width])


def draw_small_button(surface, colour, x_pos, y_pos, length, width):
    """Draws small buttons"""

    pygame.draw.rect(surface, colour, [x_pos, y_pos, length, width])


def menu_logic(pos, x_b, b_1_y, b_l, b_w):
    """Finds the button that the mouse is on in the main menu"""

    # Mouse is within button x-coordinates
    if pos[0] > x_b and pos[0] < x_b + b_l:
        # Mouse is on play button
        if pos[1] > b_1_y and pos[1] < b_1_y + b_w:
            button = 1
        # Mouse is on instructions button
        elif pos[1] > b_1_y + 100 and pos[1] < b_1_y + 100 + b_w:
            button = 2
        # Mouse is on quit button
        elif pos[1] > b_1_y + 200 and pos[1] < b_1_y + 200 + b_w:
            button = 3
        # Mouse not on any button
        else:
            button = 0
    # Mouse not on any button
    else:
        button = 0

    return button


def draw_menu_buttons(
    surface, x_b, b_1_y, b_l, b_w, b_1_c, b_2_c, b_3_c, p_text, i_text, q_text,
    o_t_1, o_t_2):
    """Draws the buttons in the main menu"""

    # Play button
    draw_button(surface, b_1_c, x_b, b_1_y, b_l, b_w)
    surface.blit(p_text, [x_b + 140, b_1_y + 25])

    # Instructions button
    draw_button(surface, b_2_c, x_b, b_1_y + 100, b_l, b_w)
    surface.blit(i_text, [x_b + 100, b_1_y + 125])

    # Quit button
    draw_button(surface, b_3_c, x_b, b_1_y + 200, b_l, b_w)
    surface.blit(q_text, [x_b + 140, b_1_y + 225])

    # My name
    surface.blit(o_t_1, [290, 570])
    surface.blit(o_t_2, [290, 595])


def instructions_logic(pos):
    """Finds the button that the mouse is on in the instructions page"""

    # Mouse is within the x-coordinates of the first four buttons
    if pos[0] >= 500 and pos[0] <= 600:
        # Mouse within y-coordinates of first two buttons
        if pos[1] > 500 and pos[1] < 550:
            # Mouse is on back button
            if pos[0] >= 500 and pos[0] <= 550:
                button = 1
            # Mouse is on forward button
            elif pos[0] >= 550 and pos[0] <= 600:
                button = 2
        # Mouse is on main menu button
        elif pos[1] >= 560 and pos[1] <= 610:
            button = 3
        # Mouse is on quit button
        elif pos[1] >= 620 and pos[1] <= 670:
            button = 4
        # Mouse is on no button
        else:
            button = 0
    # Mouse is on play button
    elif pos[0] >= 195 and pos[0] <= 490 and pos[1] >= 570 and pos[1] <= 640:
        button = 5
    # Mouse is on no button
    else:
        button = 0

    return button


def draw_instruction_buttons(
    surface, p, b_4_c, b_5_c, b_6_c, b_7_c, b_8_c, b_text, f_text, m_text, q_text, p_text):
    """
    Draws the buttons in the instructions pages
    Also draws the background for the instructions text
    """

    # Draw background for instructions text
    pygame.draw.rect(surface, p, [85, 85, 510, 510])

    # Back button
    draw_small_button(surface, b_4_c, 500, 500, 50, 50)
    surface.blit(b_text, [515, 515])
    # Forward button
    draw_small_button(surface, b_5_c, 550, 500, 50, 50)
    surface.blit(f_text, [565, 515])

    # Menu button
    draw_small_button(surface, b_6_c, 500, 560, 100, 50)
    surface.blit(m_text, [520, 575])

    # Quit button
    draw_small_button(surface, b_7_c, 500, 620, 100, 50)
    surface.blit(q_text, [525, 635])

    # Play button
    draw_button(surface, b_8_c, 195, 560, 295, 70)
    surface.blit(p_text, [320, 585])


def current_instructions(current_instructions_lines, page, font, b):
    """Returns list of instructions and coordinates for the current page"""

    text_x = 85
    text_y = 85
    instruction_display_list = []

    # Loop for iterating through instruction lines within a page
    for instruction_line in current_instructions_lines[page]:
        # Add instruction lines and their coordinates to blit list
        current_line = font.render(instruction_line[:-1], True, b)
        instruction_display_list.append([current_line, [text_x, text_y]])
        text_y += 30

    return instruction_display_list


def blit_instructions(
    surface, screen_size, instructions_display_list, page, p_pic, r_pic, kn_pic,
    b_pic, q_pic, ki_pic, p_p_pic, c_pic, p_text):
    """Displays the instructions"""

    # Display the current instructions
    for instruction_blit in instructions_display_list:
        surface.blit(
            instruction_blit[0], [instruction_blit[1][0],
            instruction_blit[1][1]
            ])

    # Display the current page's picture
    if page == 0:
        surface.blit(p_pic, [screen_size[0] // 2 - 150 // 2, 120])
    elif page == 1:
        surface.blit(p_p_pic, [screen_size[0] // 2 - 235 // 2, 110])
    elif page == 2:
        surface.blit(r_pic, [screen_size[0] // 2 - 150 // 2, 120])
    elif page == 3:
        surface.blit(kn_pic, [screen_size[0] // 2 - 150 // 2, 120])
    elif page == 4:
        surface.blit(b_pic, [screen_size[0] // 2 - 150 // 2, 120])
    elif page == 5:
        surface.blit(q_pic, [screen_size[0] // 2 - 150 // 2, 120])
    elif page == 6:
        surface.blit(ki_pic, [screen_size[0] // 2 - 150 // 2, 120])
    elif page == 7:
        surface.blit(c_pic, [screen_size[0] // 2 - 150 // 2, 120])
    elif page == 8:
        surface.blit(ki_pic, [screen_size[0] // 2 - 150 // 2, 120])
    elif page == 9:
        surface.blit(p_text, [screen_size[0] // 2 - 150 // 2, 170])


def pause_menu_logic(pos, x_b, b_l, b_w):
    """Finds the button that the mouse is on in the pause menu"""

    # Mouse in within x-coordinates of button
    if pos[0] >= x_b and pos[0] <= x_b + b_l:
        # Mouse is on resume button
        if pos[1] >= 200 and pos[1] <= 200 + b_w:
            button = 1
        # Mouse is on main menu button
        elif pos[1] >= 300 and pos[1] <= 300 + b_w:
            button = 2
        # Mouse is on restart button
        elif pos[1] >= 400 and pos[1] <= 400 + b_w:
            button = 3
        # Mouse is on quit button
        elif pos[1] >= 500 and pos[1] <= 500 + b_w:
            button = 4
        # Mouse is on no button
        else:
            button = 0
    # Mouse is on no button
    else:
        button = 0

    return button


def draw_pause_buttons(
    surface, b_9_c, b_10_c, b_11_c, b_12_c, x_b, b_l, b_w, pse_pic, rsme_text,
    m_text, rstrt_text, q_text):
    """
    Draws the buttons in the pause menu
    Also draws puase image
    """

    # Resume button
    draw_button(surface, b_9_c, x_b, 200, b_l, b_w)
    surface.blit(rsme_text, [x_b + 125, 225])

    # Main menu button
    draw_button(surface, b_10_c, x_b, 300, b_l, b_w)
    surface.blit(m_text, [x_b + 135, 325])

    # Restart button
    draw_button(surface, b_11_c, x_b, 400, b_l, b_w)
    surface.blit(rstrt_text, [x_b  + 125, 425])

    # Quit button
    draw_button(surface, b_12_c, x_b, 500, b_l, b_w)
    surface.blit(q_text, [x_b + 140, 525])

    # Display pause image
    surface.blit(pse_pic, [100, 100])


def endgame_logic(pos, x_b, b_l, b_w):
    """Finds the button that the mouse is on in engame menu"""

    # Mouse in within x-coordinates of button
    if pos[0] >= x_b and pos[0] <= x_b + b_l:
        # Mouse is on play again button
        if pos[1] >= 300 and pos[1] <= 300 + b_w:
            button = 1
        # Mouse is on main menu button
        elif pos[1] >= 400 and pos[1] <= 400 + b_w:
            button = 2
        # Mouse is on quit button
        elif pos[1] >= 500 and pos[1] <= 500 + b_w:
            button = 3
        # Mouse is on no button
        else:
            button = 0
    # Mouse is on no button
    else:
        button = 0

    return button


def draw_endgame_buttons(
    surface, checkmate, stalemate, b_13_c, b_14_c, b_15_c, x_b, b_l, b_w, c_pic,
    s_pic, p_a_text, m_text, q_text):
    """Draws the buttons in the endgame"""

    # Display checkamte or stalemate pic
    if checkmate:
        surface.blit(c_pic, [100, 100])
    elif stalemate:
        surface.blit(s_pic, [100, 100])

    # Play again button
    draw_button(surface, b_13_c, x_b, 300, b_l, b_w)
    surface.blit(p_a_text, [x_b + 114, 325])

    # Main menu button
    draw_button(surface, b_14_c, x_b, 400, b_l, b_w)
    surface.blit(m_text, [x_b + 135, 425])

    # Quit button
    draw_button(surface, b_15_c, x_b, 500, b_l, b_w)
    surface.blit(q_text, [x_b + 140, 525])


def pawn_promotion_logic(pos, screen_size):
    """Finds which button the mouse in on in pawn promotion"""

    # Starting coordinates
    x_start = screen_size[0] // 2 - 120
    y_start = screen_size[1] // 2 - 45

    # Mouse is within y-coordinates of buttons
    if pos[1] >= y_start + 20 and pos[1] <= y_start + 70:
        # Mouse is on rook button
        if pos[0] >= x_start + 20 and pos[0] <= x_start + 70:
            button = 1
            coords = [x_start + 40, y_start + 40]
        # Mouse is on knight button
        elif pos[0] >= x_start + 70 and pos[0] <= x_start + 120:
            button = 2
            coords = [x_start + 90, y_start + 40]
        # Mouse is on bishop button
        elif pos[0] >= x_start + 120 and pos[0] <= x_start + 170:
            button = 3
            coords = [x_start + 140, y_start + 40]
        # Mouse is on queen button
        elif pos[0] >= x_start + 170 and pos[0] <= x_start + 220:
            button = 4
            coords = [x_start + 190, y_start + 40]
        # Mouse is on no button
        else:
            button = 0
            coords = [0, 0]
    # Mouse is on no button
    else:
        button = [0, 0]
        coords = [0, 0]

    return [button, coords]


def draw_pawn_promtion_buttons(
    surface, p, screen_size, choose_text, r_pic, kn_pic, b_pic, q_pic):
    """
    Draws the buttons in pawn promotion
    Also draws the background for the buttons
    """

    # Starting coordinates
    x_start = screen_size[0] // 2 - 120
    y_start = screen_size[1] // 2 - 45

    pygame.draw.rect(surface, p, [x_start , y_start - 70, 240, 70])
    surface.blit(choose_text, [x_start + 50, y_start - 45])

    # Draw background for options
    pygame.draw.rect(surface, p, [x_start, y_start, 240, 70])

    # Draw options as pictures of the pieces
    surface.blit(r_pic, [x_start + 20, y_start + 15])
    surface.blit(kn_pic, [x_start + 70, y_start + 15])
    surface.blit(b_pic, [x_start + 120, y_start + 15])
    surface.blit(q_pic, [x_start + 170, y_start + 15])


def highlight_p_p_selection(surface, b, p_p_x, p_p_y):
    """Highlights the selection of the user in pawn promotion"""

    # Draw selection
    pygame.draw.ellipse(surface, b, [p_p_x, p_p_y, 10, 10])


def main():
    """Main game, main loop, and event handling"""

    # Define colours
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    HIGHLIGHT_BLUE = (53, 248, 255)
    HIGHLIGHT_RED = (255, 70, 10)
    GREEN = (0, 255, 0)
    BLUE = (20, 40, 255)
    RED = (255, 40, 40)
    PINK = (255, 40, 255)
    ORANGE = (245, 140, 40)

    # Program mode
    # 1 is menu, 2 is instructions, 3 is game, 4 is pause menu, 5 is endgame,
    # 6 is pawn promotion
    mode = 1

    # - Colours for each button -
    # Main Menu buttons
    button_1_colour = BLUE
    button_2_colour = BLUE
    button_3_colour = BLUE
    # Instructions buttons
    button_4_colour = BLUE
    button_5_colour = BLUE
    button_6_colour = BLUE
    button_7_colour = BLUE
    button_8_colour = BLUE
    # Pause menu buttons
    button_9_colour = BLUE
    button_10_colour = BLUE
    button_11_colour = BLUE
    button_12_colour = BLUE
    # Checkmate or stalemate buttons
    button_13_colour = BLUE
    button_14_colour = BLUE
    button_15_colour = BLUE

    # Button clicks initialized to False, button numbers initialized to zero
    main_menu_click = False
    menu_button = 0
    instruction_click = False
    instructions_button = 0
    pause_menu_click = False
    pause_menu_button = 0
    end_menu_click = False
    end_menu_button = 0
    pawn_promotion_click = False
    pawn_promotion_button = 0

    # Initialize instructions page to 0 (first page)
    instructions_page_counter = 0

    # Text files have not been loaded, so initialize to False
    # Text files are loaded if the user clicks on instructions
    text_files_loaded = False
    # Text files have not yet been loaded, so do not display them
    draw_text_files = False

    # No sounds being played yet, so initialize to False
    play_move_sound = False
    play_win_sound = False

    # Mouse is not on pawn promotion screen, so initialize to False
    highlight_pawn_promotion = False

    # Get chessboard list from calling chessboard function
    chessboard = chessboard_init()

    # Controls which player's turn it is
    # White's turn = 1, Black's turn = 2
    turn = 1

    # If 50 moves have been made without any pieces taken, stalemate is reached
    stalemate_counter = 0

    # No one has made any moves, so initialized check to False
    check = False
    checkmate = False
    stalemate = False

    # User has not clicked on a piece yet, so initialize to False
    selecting = False
    draw_selecting = False

    # User is not choosing possible moves yet, so initialize to False
    moving = False

    # No pieces are moving yet, so initialize to False
    move_piece = False

    friendly_possibilities = []

    pygame.init()

    # Initialize fonts
    font = pygame.font.SysFont("Calibri", 25, True, False)
    font_big = pygame.font.SysFont("Calibri", 50, True, False)

    # Text for buttons
    play_text = font.render("Play", True, BLACK)
    instructions_text = font.render("Instructions", True, BLACK)
    quit_text = font.render("Quit", True, BLACK)
    back_text = font.render("<", True, BLACK)
    forward_text = font.render(">", True, BLACK)
    menu_text = font.render("Menu", True, BLACK)
    resume_text = font.render("Resume", True, BLACK)
    restart_text = font.render("Restart", True, BLACK)
    play_again_text = font.render("Play Again", True, BLACK)
    choose_piece_text = font.render("Choose Piece", True, BLACK)
    pause_text = font_big.render("PAUSE", True, WHITE)
    owner_text_1 = font.render("Daniel", True, ORANGE)
    owner_text_2 = font.render("Di Giovanni", True, ORANGE)

    # Set screen size
    size = (680, 680)
    screen = pygame.display.set_mode(size)

    # Default button size (used for most buttons)
    button_width = 70
    button_length = 340

    # The x-coordinate for default buttons
    x_button = size[0] // 2 - button_length // 2

    # The y-coordinate of the first button
    button_1_y = 290

    # - Load image -
    title_pic = pygame.image.load("pictures/title.png").convert()
    # - Set colorkey of image -
    title_pic.set_colorkey(GREEN)
    instructions_title = pygame.image.load(
        "pictures/instructions_title.png").convert()
    instructions_title.set_colorkey(GREEN)
    pause_pic = pygame.image.load("pictures/pause.png").convert()
    pause_pic.set_colorkey(GREEN)
    check_pic = pygame.image.load("pictures/check.png").convert()
    check_pic.set_colorkey(GREEN)
    checkmate_pic = pygame.image.load("pictures/checkmate.png").convert()
    checkmate_pic.set_colorkey(GREEN)
    stalemate_pic = pygame.image.load("pictures/stalemate.png").convert()
    stalemate_pic.set_colorkey(GREEN)
    pawn_pic = pygame.image.load("pictures/big_pawn.png").convert()
    pawn_pic.set_colorkey(GREEN)
    rook_pic = pygame.image.load("pictures/big_rook.png").convert()
    rook_pic.set_colorkey(GREEN)
    knight_pic = pygame.image.load("pictures/big_knight.png").convert()
    knight_pic.set_colorkey(GREEN)
    bishop_pic = pygame.image.load("pictures/big_bishop.png").convert()
    bishop_pic.set_colorkey(GREEN)
    queen_pic = pygame.image.load("pictures/big_queen.png").convert()
    queen_pic.set_colorkey(GREEN)
    king_pic = pygame.image.load("pictures/big_king.png").convert()
    king_pic.set_colorkey(GREEN)
    white_pawn_pic = pygame.image.load("pictures/white_pawn.png").convert()
    white_pawn_pic.set_colorkey(GREEN)
    white_rook_pic = pygame.image.load("pictures/white_rook.png").convert()
    white_rook_pic.set_colorkey(GREEN)
    white_knight_pic = pygame.image.load("pictures/white_knight.png").convert()
    white_knight_pic.set_colorkey(GREEN)
    white_bishop_pic = pygame.image.load("pictures/white_bishop.png").convert()
    white_bishop_pic.set_colorkey(GREEN)
    white_queen_pic = pygame.image.load("pictures/white_queen.png").convert()
    white_queen_pic.set_colorkey(GREEN)
    white_king_pic = pygame.image.load("pictures/white_king.png").convert()
    white_king_pic.set_colorkey(GREEN)
    black_pawn_pic = pygame.image.load("pictures/black_pawn.png").convert()
    black_pawn_pic.set_colorkey(GREEN)
    black_rook_pic = pygame.image.load("pictures/black_rook.png").convert()
    black_rook_pic.set_colorkey(GREEN)
    black_knight_pic = pygame.image.load("pictures/black_knight.png").convert()
    black_knight_pic.set_colorkey(GREEN)
    black_bishop_pic = pygame.image.load("pictures/black_bishop.png").convert()
    black_bishop_pic.set_colorkey(GREEN)
    black_queen_pic = pygame.image.load("pictures/black_queen.png").convert()
    black_queen_pic.set_colorkey(GREEN)
    black_king_pic = pygame.image.load("pictures/black_king.png").convert()
    black_king_pic.set_colorkey(GREEN)
    pawn_promotion_pic = pygame.image.load(
        "pictures/pawn_promotion.png").convert()

    move_sound = pygame.mixer.Sound("sounds/move.ogg")
    win_sound = pygame.mixer.Sound("sounds/win.ogg")

    pygame.display.set_caption("Chess")

    # Loop will run
    done = False

    # Set clock
    clock = pygame.time.Clock()

    # ----- Main loop -----
    while not done:
        # --- Event loop ---
        for event in pygame.event.get():

            # User clicks quit
            if event.type == pygame.QUIT:
                # Stop loop
                done = True

            # User clicks and it is a left click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # Main menu
                if mode == 1:
                    main_menu_click = True
                # Instructions
                elif mode == 2:
                    instruction_click = True
                # Game
                elif mode == 3:
                    # Get coordinates of click
                    click_coordinates = pygame.mouse.get_pos()

                    # Get coordinates on board by calling function that converts
                    # click position to board position
                    board_position = click_position_on_board(
                        click_coordinates, size)

                    # Get information of the square that was clicked
                    click_information = square_information(
                        board_position, chessboard)

                    # If the user selected a piece, check if next click was not
                    # on their piece
                    if selecting:
                        moving = piece_possibly_moving(click_information, turn)

                    # Find if user has clicked on their own piece
                    selecting = piece_selected(click_information, turn)

                # Pause menu
                elif mode == 4:
                    pause_menu_click = True
                # Checkmate or stalemate
                elif mode == 5:
                    end_menu_click = True
                # Pawn promotion
                elif mode == 6:
                    pawn_promotion_click = True

            # User lets go of click and it is left click
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                # Main menu
                if mode == 1:
                    main_menu_click = False
                # Instructions
                elif mode == 2:
                    instruction_click = False
                # Pause menu
                elif mode == 4:
                    pause_menu_click = False
                # Checkmate or stalemate
                elif mode == 5:
                    end_menu_click = False
                # Pawn promotion
                elif mode == 6:
                    pawn_promotion_click = False

            # User lets go of escape ket or p key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:

                    # Go to game or pause menu, depending on the current mode
                    if mode == 3:
                        mode = 4
                    elif mode == 4:
                        mode = 3

        # --- Game logic ---

        # -- Main Menu --
        if mode == 1:

            # Get position of mouse
            menu_pos = pygame.mouse.get_pos()

            # Get the button that the mouse is on
            menu_button = menu_logic(
                menu_pos, x_button, button_1_y, button_length, button_width)

            # Mouse not on any button
            if menu_button == 0:
                button_1_colour = BLUE
                button_2_colour = BLUE
                button_3_colour = BLUE
            # Mouse on play button
            elif menu_button == 1:
                button_1_colour = RED
                button_2_colour = BLUE
                button_3_colour = BLUE
                if main_menu_click:
                    # If user clicks on play button, start game
                    mode = 3
                    main_menu_click = False
            # Mouse on instructions button
            elif menu_button == 2:
                button_1_colour = BLUE
                button_2_colour = RED
                button_3_colour = BLUE
                if main_menu_click:
                    # If user clicks on instructions button, start instructions
                    mode = 2
                    main_menu_click = False
            # Mouse on quit button
            elif menu_button == 3:
                button_1_colour = BLUE
                button_2_colour = BLUE
                button_3_colour = RED
                if main_menu_click:
                    # If user clicks on quit, stop program
                    done = True

        # -- Instructions --
        elif mode == 2:

            # Get position of mouse
            instructions_pos = pygame.mouse.get_pos()

            # Get the button that the mouse is on
            instructions_button = instructions_logic(instructions_pos)

            # Mouse is not on button
            if instructions_button == 0:
                button_4_colour = BLUE
                button_5_colour = BLUE
                button_6_colour = BLUE
                button_7_colour = BLUE
                button_8_colour = BLUE
            # Mouse is on back button
            elif instructions_button == 1:
                button_4_colour = RED
                button_5_colour = BLUE
                button_6_colour = BLUE
                button_7_colour = BLUE
                button_8_colour = BLUE
                if instruction_click:
                    # Go back a page in instructions
                    # If min page is reached, go to last page
                    if instructions_page_counter <= 0:
                        instructions_page_counter = len(instructions) - 1
                        instruction_click = False
                    else:
                        instructions_page_counter -= 1
                        instruction_click = False
            # Mouse is on forward button
            elif instructions_button == 2:
                button_4_colour = BLUE
                button_5_colour = RED
                button_6_colour = BLUE
                button_7_colour = BLUE
                button_8_colour = BLUE
                if instruction_click:
                    # Go to next instructions page
                    # If max page is reached, go to first page
                    if instructions_page_counter >= len(instructions) - 1:
                        instructions_page_counter = 0
                        instruction_click = False
                    else:
                        instructions_page_counter += 1
                        instruction_click = False
            # Mouse is on main menu button
            elif instructions_button == 3:
                button_4_colour = BLUE
                button_5_colour = BLUE
                button_6_colour = RED
                button_7_colour = BLUE
                button_8_colour = BLUE
                if instruction_click:
                    mode = 1
                    instruction_click = False
                    instructions_page_counter = 0
            # Mouse is on quit button
            elif instructions_button == 4:
                button_4_colour = BLUE
                button_5_colour = BLUE
                button_6_colour = BLUE
                button_7_colour = RED
                button_8_colour = BLUE
                if instruction_click:
                    done = True
            # Mouse is on play button
            elif instructions_button == 5:
                button_4_colour = BLUE
                button_5_colour = BLUE
                button_6_colour = BLUE
                button_7_colour = BLUE
                button_8_colour = RED
                if instruction_click:
                    mode = 3
                    instruction_click = False
                    instructions_page_counter = 0

            # Load text files if they have not already been loaded
            if not text_files_loaded:
                instructions = load_text_files()
                text_files_loaded = True

            else:
                # Only draw text files if they have been loaded
                draw_text_files = True
                instruction_blit_list = current_instructions(
                    instructions, instructions_page_counter, font, BLACK)

        # -- Game --
        elif mode == 3:

            # Set pause click to False so that next time user pauses,
            # it will not automatically click
            pause_menu_click = False

            # Get the position of the player's king
            king_square = king_position(chessboard, turn)

            # Get the movement posibilities of every enemy piece
            possibilities_of_enemy = enemy_possibilities(chessboard, turn)

            # King in check
            if king_square in possibilities_of_enemy:
                check = True

            # Get friendly movement possibilities
            friendly_possibilities = friendly_movement_possibilities(
                chessboard, turn)

            # If player can not make any moves, it is checkmate or stalemate
            if len(friendly_possibilities) == 0:
                # If the king is in check, it is checkmate
                if check:
                    checkmate = True
                # If the king is not in check, it is stalemate
                else:
                    stalemate = True

            if checkmate or stalemate:
                mode = 5

            # If the user selected their piece, get a list of possible moves
            if selecting:
                possible_movements = movement_possibilties(
                    click_information, board_position, chessboard, turn)

                # Save this square in variables because it is the starting point
                starting_square = board_position
                starting_square_info = click_information

            # After a piece was selected, then a square without the user's piece
            # was selected,
            # check if that square is in the list of movement possibilities
            if moving:
                move_piece = piece_can_move(possible_movements, board_position)

            # If piece can move, save the ending square in a variable and update
            # the chessboard list
            if move_piece:
                ending_square = board_position

                # If no piece was taken, increment stlaemate counter
                if chessboard[ending_square[1]][ending_square[0]][1][1] == 0:
                    stalemate_counter += 1
                else:
                    # A piece was taken, so set stalemate counter to zero
                    stalemate_counter = 0

                # If 50 moves have been reached, stalemate is reached
                if stalemate_counter > 49:
                    stalemate = True

                if turn == 1:

                    if (ending_square[1] == 7 and
                            chessboard[starting_square[1]][starting_square[0]]
                            [1][0] == 1 and
                            chessboard[starting_square[1]][starting_square[0]]
                            [1][1] == 1):
                        # White's pawn reached other side
                        mode = 6
                        pawn_promotion_square = ending_square
                elif turn == 2:

                    if (ending_square[1] == 0 and
                            chessboard[starting_square[1]][starting_square[0]]
                            [1][0] == 1 and
                            chessboard[starting_square[1]][starting_square[0]]
                            [1][1] == 2):
                        # Black's pawn reached other side
                        mode = 6
                        pawn_promotion_square = ending_square

                # Change the board
                chessboard = change_board(
                    chessboard, starting_square, ending_square,
                    starting_square_info)


                # Piece has been moved, so user is not moving, not selecting,
                # and does not need the possible movements list
                move_piece = False
                moving = False
                selecting = False
                possible_movements = []
                check = False

                # Move sound will be played
                play_move_sound = True

                # Change turn
                if turn == 1:
                    turn = 2
                else:
                    turn = 1

        # -- Pause menu --
        elif mode == 4:

            # Get position of mouse
            pause_menu_pos = pygame.mouse.get_pos()

            # Get the button that the mouse is on
            pause_menu_button = pause_menu_logic(
                pause_menu_pos, x_button, button_length, button_width)

            # Mouse is on no button
            if pause_menu_button == 0:
                button_9_colour = BLUE
                button_10_colour = BLUE
                button_11_colour = BLUE
                button_12_colour = BLUE
            # Mouse is on resume button
            elif pause_menu_button == 1:
                button_9_colour = RED
                button_10_colour = BLUE
                button_11_colour = BLUE
                button_12_colour = BLUE
                if pause_menu_click:
                    # Go to game
                    mode = 3
                    pause_menu_click = False
            # Mouse is on main menu button
            elif pause_menu_button == 2:
                button_9_colour = BLUE
                button_10_colour = RED
                button_11_colour = BLUE
                button_12_colour = BLUE
                if pause_menu_click:
                    # Go to main menu, reset variables
                    mode = 1
                    chessboard = chessboard_init()
                    selecting = False
                    moving = False
                    move_piece = False
                    check = False
                    checkmate = False
                    stalemate = False
                    turn = 1
                    pause_menu_click = False
            # Mouse is on restart button
            elif pause_menu_button == 3:
                button_9_colour = BLUE
                button_10_colour = BLUE
                button_11_colour = RED
                button_12_colour = BLUE
                if pause_menu_click:
                    # Go to game, reset variables
                    mode = 3
                    chessboard = chessboard_init()
                    selecting = False
                    moving = False
                    move_piece = False
                    check = False
                    checkmate = False
                    stalemate = False
                    turn = 1
                    pause_menu_click = False
            # Mouse is on quit button
            elif pause_menu_button == 4:
                button_9_colour = BLUE
                button_10_colour = BLUE
                button_11_colour = BLUE
                button_12_colour = RED
                if pause_menu_click:
                    # Quit program
                    done = True

            # Set button to 0 so that next time user pauses,
            # a button will not automatically be clicked
            button = 0

        # -- Checkmate or stalemate --
        elif mode == 5:

            # Get position of mouse
            end_menu_pos = pygame.mouse.get_pos()

            # Get the button that the mouse is on
            end_menu_button = endgame_logic(
                end_menu_pos, x_button, button_length, button_width)

            # Mouse is on no button
            if end_menu_button == 0:
                button_13_colour = BLUE
                button_14_colour = BLUE
                button_15_colour = BLUE
            # Mouse is on play again button
            elif end_menu_button == 1:
                button_13_colour = RED
                button_14_colour = BLUE
                button_15_colour = BLUE
                if end_menu_click:
                    # Go to game, reset variables
                    mode = 3
                    chessboard = chessboard_init()
                    selecting = False
                    moving = False
                    move_piece = False
                    check = False
                    checkmate = False
                    stalemate = False
                    turn = 1
                    end_menu_click = False
            # Mouse is on main menu button
            elif end_menu_button == 2:
                button_13_colour = BLUE
                button_14_colour = RED
                button_15_colour = BLUE
                if end_menu_click:
                    # Go to main menu, reset variables
                    mode = 1
                    chessboard = chessboard_init()
                    selecting = False
                    moving = False
                    move_piece = False
                    check = False
                    checkmate = False
                    stalemate = False
                    turn = 1
                    end_menu_click = False
            # Mouse is on quit button
            elif end_menu_button == 3:
                button_13_colour = BLUE
                button_14_colour = BLUE
                button_15_colour = RED
                if end_menu_click:
                    # Quit program
                    done = True

            # Win sound will be played
            play_win_sound = True


        # -- Pawn promotion --
        elif mode == 6:

            # Get position of mouse
            pawn_promotion_pos = pygame.mouse.get_pos()

            # Get button that the mouse is on
            pawn_promotion_button = pawn_promotion_logic(
                pawn_promotion_pos, size)[0]

            # Coordinates to highlight
            pawn_promotion_coords = pawn_promotion_logic(
                pawn_promotion_pos, size)[1]

            # Mouse is on no button
            if pawn_promotion_button == 0:
                # Do not highlight
                highlight_pawn_promotion = False
            # Mouse is on a button
            else:
                # Do highlight
                highlight_pawn_promotion = True

                if pawn_promotion_click:
                    # Mouse is on rook button
                    if pawn_promotion_button == 1:
                        chessboard[pawn_promotion_square[1]] \
                        [pawn_promotion_square[0]][1][0] = 2
                        # - Go back to game  and reset click variable -
                        mode = 3
                        pawn_promotion_click = False
                    # Mouse is on knight button
                    elif pawn_promotion_button == 2:
                        chessboard[pawn_promotion_square[1]] \
                        [pawn_promotion_square[0]][1][0] = 3
                        mode = 3
                        pawn_promotion_click = False
                    # Mouse is on bishop button
                    elif pawn_promotion_button == 3:
                        chessboard[pawn_promotion_square[1]] \
                        [pawn_promotion_square[0]][1][0] = 4
                        mode = 3
                        pawn_promotion_click = False
                    # Mouse is on queen button
                    elif pawn_promotion_button == 4:
                        chessboard[pawn_promotion_square[1]] \
                        [pawn_promotion_square[0]][1][0] = 5
                        mode = 3
                        pawn_promotion_click = False

        # --- Drawing logic ---

        # -- Clear screen --
        screen.fill(WHITE)

        # -- Drawing --

        # - Main menu -
        if mode == 1:

            draw_empty_chessboard(size, screen, WHITE, BLACK)
            screen.blit(title_pic, [14, 62])
            draw_menu_buttons(
                screen, x_button, button_1_y, button_length, button_width,
                button_1_colour, button_2_colour, button_3_colour, play_text,
                instructions_text, quit_text, owner_text_1, owner_text_2)

        # - Instructions -
        elif mode == 2:

            draw_empty_chessboard(size, screen, WHITE, BLACK)
            screen.blit(instructions_title, [95, 15])
            draw_instruction_buttons(
                screen, PINK, button_4_colour, button_5_colour, button_6_colour,
                button_7_colour, button_8_colour, back_text, forward_text,
                menu_text, quit_text, play_text)

            if draw_text_files:
                blit_instructions(
                    screen, size, instruction_blit_list,
                    instructions_page_counter, pawn_pic, rook_pic, knight_pic,
                    bishop_pic, queen_pic, king_pic, pawn_promotion_pic,
                    check_pic, pause_text)

        # - Game -
        elif mode == 3 or mode == 4 or mode == 5 or mode == 6:

            draw_chessboard(
                chessboard, size, screen, WHITE, BLACK, white_pawn_pic,
                white_rook_pic, white_knight_pic, white_bishop_pic,
                white_queen_pic, white_king_pic, black_pawn_pic, black_rook_pic,
                black_knight_pic, black_bishop_pic, black_queen_pic,
                black_king_pic)

            if selecting:
                highlight_movement_options(
                    board_position, chessboard, possible_movements, screen,
                    HIGHLIGHT_BLUE, size, possible_movements)

            if check:
                highlight_check(
                    chessboard, king_square, size, screen, HIGHLIGHT_RED)

            if play_move_sound:
                # Play move sound
                move_sound.play()
                # Do not repeat sound
                play_move_sound = False

            # - Pause menu -
            if mode == 4:
                draw_pause_buttons(
                    screen, button_9_colour, button_10_colour, button_11_colour,
                    button_12_colour, x_button, button_length, button_width,
                    pause_pic, resume_text, menu_text, restart_text, quit_text)

            # - Checkmate or stalemate -
            elif mode == 5:
                draw_endgame_buttons(
                    screen, checkmate, stalemate, button_13_colour,
                    button_14_colour, button_15_colour, x_button, button_length,
                    button_width, checkmate_pic, stalemate_pic, play_again_text,
                    menu_text, quit_text)

                if play_win_sound:
                    # Play win sound
                    win_sound.play()
                    # Do not repeat sound
                    play_win_sound = False

            # - Pawn promotion -
            elif mode == 6:
                draw_pawn_promtion_buttons(
                    screen, PINK, size, choose_piece_text, white_rook_pic,
                    black_knight_pic, white_bishop_pic, black_queen_pic)

                # Highlight pawn promtion selection if mouse is on an option
                if highlight_pawn_promotion:
                    highlight_p_p_selection(
                    screen, HIGHLIGHT_BLUE, pawn_promotion_coords[0],
                    pawn_promotion_coords[1])

        # Update screen
        pygame.display.flip()

        # Limits loop to 60 frames per second
        clock.tick(30)

    # Once loop is over, quit game
    pygame.quit()

main()