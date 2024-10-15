def shift_left(L):
    """ (str) -> str
    """

    first_item = L[0]
    for i in range(1, len(L)):
        L[i-1]=L[i]

    L[-1]=first_item

