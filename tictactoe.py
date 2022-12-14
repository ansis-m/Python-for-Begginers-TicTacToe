def win(chars):
    count = ""

    for i in range(3):
        if chars[i * 3] == chars[i * 3 + 1] and chars[i * 3] == chars[i * 3 + 2]:
            count += chars[i * 3]
        if chars[i] == chars[i + 3] and chars[i] == chars[i + 6]:
            count += chars[i]
    if chars[0] == chars[4] and chars[0] == chars[8]:
        count += chars[0]
    if chars[2] == chars[4] and chars[2] == chars[6]:
        count += chars[2]

    return count


def count_chars(chars):
    X = 0
    O = 0

    for ch in chars:
        if ch == 'X':
            X += 1
        elif ch == 'O':
            O += 1

    return X, O


def draw(chars):
    X, O = count_chars(chars)
    return True if X + O == 9 else False

def show_field(chars):
    print("---------")
    print("| {} {} {} |".format(chars[0], chars[1], chars[2]))
    print("| {} {} {} |".format(chars[3], chars[4], chars[5]))
    print("| {} {} {} |".format(chars[6], chars[7], chars[8]))
    print("---------")


def main():

    chars = [' ' for i in range(9)]
    show_field(chars)

    symbol = 'X'

    while True:
        move = input()
        digits = move.split()
        try:
            x = int(digits[0])
            y = int(digits[1])
        except:
            print("You should enter numbers!")
        else:
            if x > 3 or y > 3 or x < 1 or y < 1:
                print("Coordinates should be from 1 to 3!")
                continue
            elif chars[(x - 1) * 3 + y - 1] != ' ':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                chars[(x - 1) * 3 + y - 1] = symbol
                symbol = 'X' if symbol == 'O' else 'O'
        show_field(chars)
        if win(chars) == 'X' or win(chars) == 'O':
            print("{} wins".format(win(chars)))
            break
        elif draw(chars):
            print("Draw")
            break

if __name__ == "__main__":
    main()