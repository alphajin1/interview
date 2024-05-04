if __name__ == '__main__':
    while True:
        try:
            s = input()
        except EOFError:
            break

        n = int(s)
        result = 1
        temp = 1
        while temp % n != 0:
            temp = temp * 10 + 1
            result += 1

        print(result)
