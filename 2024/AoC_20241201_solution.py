def measure_distance(l1, l2):
    distance = 0
    for i in range(len(l1)):
        distance += abs(l1[i] - l2[i])
    return distance

def find_occurrence(number, list):
    count = 0
    for n in list:
        if n == number:
            count += 1
    return count

def measure_similarity(l1, l2):
    sim = 0
    for n in l1:
        sim += n * find_occurrence(n, l2)
    return sim

if __name__ == "__main__":
    file = open("C:\\Work\\Repository\\advent-of-code\\2024\\AoC_20241201_input.txt", "r") 
    data = file.read() 
    file.close()

    file.close()

    l1 = []
    l2 = []

    # Create two lists
    for line in data.split("\n"):
        pair = line.split("   ")
        l1.append(int(pair[0]))
        l2.append(int(pair[1]))

    l1.sort()
    l2.sort()

    # Part 1
    print(measure_distance(l1, l2))
    # Part 2
    print(measure_similarity(l1, l2))
