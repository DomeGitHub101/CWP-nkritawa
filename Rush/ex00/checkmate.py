
def is_valid_pos(size, r, c):
    return 0 <= r < size and 0 <= c < size

def checkmate(board_str):
    
    rows = [row for row in board_str.strip().split('\n') if row]
    if not rows:
        return

    board_size = len(rows)
    king_pos = None
    king_count = 0

    for r, row in enumerate(rows):
        if len(row) != board_size:
            return
        for c, piece in enumerate(row):
            if piece == 'K':
                king_pos = (r, c)
                king_count += 1

    if king_count != 1:
        return

    kr, kc = king_pos

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1) 
    ]

    for i, (dr, dc) in enumerate(directions):
        r, c = kr + dr, kc + dc
        while is_valid_pos(board_size, r, c):
            piece = rows[r][c]
            if piece != '.':
                is_diagonal = i >= 4
                if is_diagonal:
                    if piece in 'BQ':
                        print("Success")
                        return
                else:
                    if piece in 'RQ':
                        print("Success")
                        return
                break
            r, c = r + dr, c + dc


    pawn_attack_positions = [
        (kr + 1, kc - 1), 
        (kr + 1, kc + 1)  
    ]

    for r, c in pawn_attack_positions:
        if is_valid_pos(board_size, r, c) and rows[r][c] == 'P':
            print("Success")
            return
    print("Fail")