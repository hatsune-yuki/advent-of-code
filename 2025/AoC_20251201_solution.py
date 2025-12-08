import math

def rotate(start, text):
    rotations = int(text[1:])
    if text[0] == "L":
        return ((start - rotations) % 100, math.floor(abs((start - rotations) / 100))) #calculate floor
    else: 
        return ((start + rotations) % 100, math.floor(abs((start + rotations) / 100)))

if __name__ == "__main__":
    file = open("/Users/sarahyang/Documents/Github/advent-of-code/2025/AoC_20251201_input.txt", "r") 
    data = file.read()
    file.close()

    position = 50
    psw = 0
    count = 0
    
    for line in data.split("\n"):
        (position, count) = rotate(position, line)
        psw += count
        print("Rotate " + line + ": Position " + str(position) + ", " + str(psw) + " passes")
    print(psw)
    