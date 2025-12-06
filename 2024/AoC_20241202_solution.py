def is_safe(l):
    n_prev = l[0]
    if l[1] - n_prev > 0:
        trend = 1
    elif l[1] - n_prev < 0:
        trend = -1
    else:
        trend = 0

    for i in range(1, len(l)):
        delta = l[i] - n_prev
        if delta == 0:
            return False
        if trend == 1 and (delta < 0 or delta > 3):
            return False
        elif trend == -1 and (delta < -3 or delta > 0):
            return False
        n_prev = l[i]
    print(f"{l} is safe.")
    return True

if __name__ == "__main__":
    file = open("C:\\Work\\Repository\\advent-of-code\\2024\\AoC_20241202_input.txt", "r") 
    data = file.read() 
    file.close()

    table = []
    for text in data.split("\n"):        
        table.append(list(map(int, text.split(" "))))

    safeCnt = 0

    for l in table:
        print(f"original list: {l}")
        for i in range(len(l)):
            newList = l[:i] + l[(i+1):]
            if is_safe(newList):
                safeCnt += 1
                break
    
    print(safeCnt)

