

def combination(a, b):
    # aCb
    b = min(b, a - b)
    result = 1

    da = a
    db = 1

    while da >= 1 and db <= b:
        result *= da
        result /= db
        da -= 1
        db += 1

    return int(result)