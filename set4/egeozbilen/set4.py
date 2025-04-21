if __name__ == "__main__":
    size = 3
    for n in range(-size-1, size+2, 2):
        a = abs(n) + 1
        print(((size+2) - a//2)*" " + a * "#")
