# simple_snake_ladder.py
# A tiny 2-player Snake & Ladder console game for beginners

import random

# Define snakes and ladders as start: end
SNAKES = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDERS = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98}

def roll_die():
    """Return a random number between 1 and 6."""
    return random.randint(1, 6)

def move(player_pos, roll):
    """
    Move player by roll.
    If landing on a ladder or snake, move to its destination.
    If move would go past 100, do not move (simple exact-roll rule).
    """
    new_pos = player_pos + roll
    if new_pos > 100:
        return player_pos, "Too far to move (need exact roll)"
    if new_pos in LADDERS:
        return LADDERS[new_pos], f"Climbed ladder to {LADDERS[new_pos]}"
    if new_pos in SNAKES:
        return SNAKES[new_pos], f"Bitten by snake to {SNAKES[new_pos]}"
    return new_pos, f"Moved to {new_pos}"

def print_positions(p1_name, p1_pos, p2_name, p2_pos):
    print(f"{p1_name}: {p1_pos}    {p2_name}: {p2_pos}")

def main():
    print("Simple Snake and Ladder - 2 players")
    p1 = input("Name of Player 1 (press Enter for 'Player1'): ").strip() or "Player1"
    p2 = input("Name of Player 2 (press Enter for 'Player2'): ").strip() or "Player2"

    pos1, pos2 = 1, 1   # starting positions
    turn = 0            # 0 => player1, 1 => player2

    while True:
        print("\n" + "-"*40)
        print_positions(p1, pos1, p2, pos2)

        if turn == 0:
            current_name, current_pos = p1, pos1
        else:
            current_name, current_pos = p2, pos2

        cmd = input(f"{current_name}, press Enter to roll the die (or 'q' to quit): ").strip().lower()
        if cmd == 'q':
            print("Goodbye!")
            break

        die = roll_die()
        print(f"{current_name} rolled: {die}")
        new_pos, msg = move(current_pos, die)
        print(msg)

        if turn == 0:
            pos1 = new_pos
        else:
            pos2 = new_pos

        # Check winner
        if pos1 == 100:
            print(f"\nCongratulations {p1}! You reached 100 and won!")
            break
        if pos2 == 100:
            print(f"\nCongratulations {p2}! You reached 100 and won!")
            break

        # switch turn
        turn = 1 - turn

if __name__ == "__main__":
    main()
