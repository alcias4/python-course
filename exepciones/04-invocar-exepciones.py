def divsion(n=0):

    if n == 0:
        raise ZeroDivisionError("NO se puede divir por cero")
    return 5/0


try:
    divsion()
except ZeroDivisionError as e:
    print(e)
