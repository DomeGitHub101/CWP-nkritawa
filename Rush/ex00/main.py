from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1: King ถูก Rook โจมตี
    print("--- Test Case 1 ---")
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1) # คาดหวัง: Success

    # ตัวอย่างที่ 2: King ไม่ถูกโจมตี (Pawn อยู่ผิดตำแหน่ง)
    print("\n--- Test Case 2 ---")
    board2 = """\
....
.K..
...P
...."""
    checkmate(board2) # คาดหวัง: Fail

    # ตัวอย่างที่ 3: King ถูก Queen โจมตีในแนวทแยง และถูก Rook บล็อก
    print("\n--- Test Case 3 ---")
    board3 = """\
Q...
.R..
..K.
...."""
    checkmate(board3) # คาดหวัง: Success (Queen โจมตีได้)

    # ตัวอย่างที่ 4: King ถูก Bishop โจมตี
    print("\n--- Test Case 4 ---")
    board4 = """\
B.......
........
........
...K....
........
........
........
........"""
    checkmate(board4) # คาดหวัง: Success

    # ตัวอย่างที่ 5: King ถูก Pawn โจมตี
    print("\n--- Test Case 5 ---")
    board5 = """\
....
.K..
P...
...."""
    checkmate(board5) # คาดหวัง: Success
    
    # ตัวอย่างที่ 6: กระดานที่ไม่มี King
    print("\n--- Test Case 6 (Undefined: No King) ---")
    board6 = """\
R...
....
..P.
...."""
    checkmate(board6)

    # ตัวอย่างที่ 7: กระดานที่ไม่ใช่สี่เหลี่ยมจัตุรัส
    print("\n--- Test Case 7 (Undefined: Not Square) ---")
    board7 = """\
R..
.K.
..P.
...."""
    checkmate(board7)


if __name__ == "__main__":
    main()