def alternate(A):
    for v in A:
        v_is_the_largest = True
        for x in A:
            if v < x:
                v_is_the_largest = False
                break
        if v_is_the_largest:
            return v
    return None
