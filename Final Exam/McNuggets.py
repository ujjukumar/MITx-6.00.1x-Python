def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    a=0
    b=0
    c=0
    while 6*a + 9*b + 20*c < n:
        for a in range((n//6)+1):
            for b in range((n//9)+1):
                for c in range ((n//20)+1):
                    if 6*a + 9*b + 20*c == n:
                        return print(True)
    if 6*a + 9*b + 20*c != n:
        return print(False)