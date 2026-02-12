def checkmate(board_str):
    validation_error = validate_input(board_str.upper())
    if validation_error:
        print(validation_error)
        return
    board_2d_list = convert_board_to_list(board_str.upper())
    position_dict = get_piece_positions(board_2d_list)
    print(check_chekmate(board_2d_list, position_dict))

def validate_input(board_str):
    stripped_str = board_str.strip()
    rows = stripped_str.split('\n')
    
    # 1. เช็คว่ามีแถวหรือไม่
    if len(rows) == 0:          
        return 'not have row'

    first_row_len = len(rows[0].replace(" ", "").strip())
    
    # 2. เช็ค NxN
    if len(rows) != first_row_len:
         return 'not square board'
    # ทุกแถวต้องมีความยาวเท่ากัน
    for i in range(len(rows)):
        row = rows[i]
        current_len = len(row.replace(" ", "").strip())
        if current_len != first_row_len:
            return f'Row length mismatch'

    # 3. เช็ค King (ต้องมี K ตัวเดียว)
    if board_str.count('K') != 1:
        return 'King is required just one'

    # 4. เช็คตัวอักษร
    valid_pieces = set('KQRBP.')
    for char in board_str:
        if char in ' \n\t\r':
            continue
        if char not in valid_pieces:
            return f'not valid piece: {char}'

    # 5. เช็คตัวหมากฝ่ายตรงข้าม
    if all(board_str.count(piece) == 0 for piece in 'QRBP'):
        return 'not have opponent piece'

    return None


def convert_board_to_list(board_str):
    return board_str.replace(" ", "").strip().split("\n")


def get_piece_positions(board_2d_list):
    position_dict = {}

    for row_idx, row in enumerate(board_2d_list):
        for col_idx, cell in enumerate(row):
            if cell != ".":
                if cell not in position_dict:
                    position_dict[cell] = []
                position_dict[cell].append((row_idx, col_idx))
    return position_dict


def check_chekmate(board_2d_list, position_dict):
    is_success = False

    if "K" not in position_dict:
        return "Failed"

    king_position = position_dict["K"]
    king_position_row, king_position_col = king_position[0]

    pieces = position_dict.keys()

    # Pawns, Bishops, Rooks, Queens... and a King.
    for piece in pieces:
        #Pawn: top left, top right
        if piece == "P":
            checkmate_position = [
                (king_position_row + 1, king_position_col + 1),
                (king_position_row + 1, king_position_col - 1),
            ]
            if any(p in checkmate_position for p in position_dict[piece]):
                is_success = True

        elif piece == "B":
        # Bishop: top left, top right, bottom left, bottom right
            condition = {
                "target_piece": piece,
                "board_2d_list": board_2d_list,
                "stuck_path": [False, False, False, False],
                "add_position": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
                "king_position_row": king_position_row,
                "king_position_col": king_position_col,
            }
            is_success = check_checkmate_with_clear_path(condition)

        elif piece == "R":
        # Rook: up, down, left, right
            condition = {
                "target_piece": piece,
                "board_2d_list": board_2d_list,
                "stuck_path": [False, False, False, False],
                "add_position": [(0, -1), (0, 1), (-1, 0), (1, 0)],
                "king_position_row": king_position_row,
                "king_position_col": king_position_col,
            }
            is_success = check_checkmate_with_clear_path(condition)

        elif piece == "Q":
        # Queen: up down, left, right, top left, top right, bottom left, bottom right
            condition = {
                "target_piece": piece,
                "board_2d_list": board_2d_list,
                "stuck_path": [False, False, False, False, False, False, False, False],
                "add_position": [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)],
                "king_position_row": king_position_row,
                "king_position_col": king_position_col,
            }
            is_success = check_checkmate_with_clear_path(condition)

        if is_success:
            break

    return "Success" if is_success else "Failed"


def check_checkmate_with_clear_path(condition):
    is_success = False

    target_piece = condition["target_piece"]
    board_2d_list = condition["board_2d_list"]
    stuck_path = condition["stuck_path"]
    add_position = condition["add_position"]
    king_position_row = condition["king_position_row"]
    king_position_col = condition["king_position_col"]

    rows = len(board_2d_list)
    cols = len(board_2d_list[0]) if rows > 0 else 0

    for idx, (dr, dc) in enumerate(add_position):
        if is_success:
            break
        if stuck_path[idx]:
            continue
        for n in range(1, max(rows, cols)):
            r = king_position_row + dr * n
            c = king_position_col + dc * n
            if r < 0 or r >= rows or c < 0 or c >= cols:
                break
            cell = board_2d_list[r][c]
            if cell == ".":
                continue
            if cell == target_piece:
                is_success = True
                break
            else:
                stuck_path[idx] = True
                break

    return is_success
