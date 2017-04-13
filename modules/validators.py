def represents_int(s):
    try:
        for x in list(s):
            int(x)
        return True
    except ValueError:
        return False
