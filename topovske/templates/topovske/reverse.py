def reverse(x):
    """
    
    :type x: int
    :rtype: int
    """
    c = []
    for i in range(len(str(x)) - 1, -1, 1):
        c.append(x[i])
    d = ''.join(c)
    return d

reverse(321)
        