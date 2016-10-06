def ways_to_eat( n ):
    w0, w1 = 1, 1,
    for i in range( 2, n + 1 ):
        w1, w0 = w1 + w0, w1
    return w1

if __name__ == "__main__":
    assert ways_to_eat( 4 ) == 5
