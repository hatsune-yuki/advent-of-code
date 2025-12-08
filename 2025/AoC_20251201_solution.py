def rotate(start, text):
    rotations = int(text[1:])
    if text[0] == "L":
        return 100 - (start - rotations) % 100 if start - rotations % 100 < 0 else start - rotations % 100
    else: 
        return (start + rotations) % 100

if __name__ == "__main__":
    file = open("/Users/sarahyang/Documents/Github/advent-of-code/2025/AoC_20251201_input.txt", "r") 
    data = file.read()
    file.close()

    position = 50
    psw = 0
    count = 0
    
    for line in data.split("\n"):
        position = rotate(position, line)
        psw += (1 if position == 0 else 0)
        count += 1
        print("Rotate " + line + ": Position " + str(position))
    print(psw)
    