def same(string: str):
    if len(string) == 2:
        return string[0] == string[1]
    
    seq = list(string)
    buffer = []
    for i in range(len(seq)-1):
        a, b = int(seq[i]), int(seq[i + 1])
        buffer.append((a + b) % 10)
    return same("".join(str(x) for x in buffer))


if __name__ == "__main__":
    s = input("String: ")
    print(same(s))
