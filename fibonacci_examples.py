import time
import matplotlib.pyplot as plt

def recursive_fibonacci( n ):
    # Calculates the nth Fibonacci number
    if   n == 0: return 0
    elif n == 1: return 1
    else:
        return recursive_fibonacci( n - 1 ) + \
               recursive_fibonacci( n - 2 )

def dynamic_fibonacci( n ):
    # Calculates the nth Fibonacci number iteratively
    # (all vals stored in a list for clarity)
    if   n == 0: return 0
    elif n == 1: return 1
    else:
        vals = [ 0, 1 ]
        for i in range( 2, n + 1 ):
            vals.append( vals[ i - 1 ] + vals[ i - 2 ] )
        return vals[ -1 ]

memoizer = {}
def memoizing_fibonacci( n ):
    # Calculates the nth Fibonacci number recursively
    # with memoization (top-down)
    global memoizer
    try: return memoizer[ n ]
    except KeyError:
        if   n == 0: fib = 0
        elif n == 1: fib = 1
        else: fib =  memoizing_fibonacci( n - 1 ) + \
                     memoizing_fibonacci( n - 2 )
        memoizer[ n ] = fib
        return fib

def test():
    # Quick and dirty test for accuracy
    fib_nums = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ]
    for index, num in enumerate( fib_nums ):
        assert recursive_fibonacci( index ) == num
        assert dynamic_fibonacci( index ) == num

def time_fib():
    # Timing routine. Will take 2+ minutes to run for max n = 40
    print "Beginning timing"
    for i in range(0, 40, 5):
        t0 = time.time()
        _ = recursive_fibonacci( i )
        t_recursive = time.time() - t0

        t0 = time.time()
        _ = memoizing_fibonacci( i )
        t_dynamic = time.time() - t0
        print "N = %02d, t_recursive = %04f, t_dynamic = %04f" % ( i, t_recursive, t_dynamic )

def plot_fib():
    # Plot routine
    times_recursive = []
    times_dynamic = []

    for i in range( 35 ):
        t0 = time.time()
        _ = recursive_fibonacci( i )
        times_recursive.append( time.time() - t0 )

        t0 = time.time()
        _ = dynamic_fibonacci( i )
        times_dynamic.append( time.time() - t0 )

    plt.subplot(211)
    plt.plot( range( 35 ), times_dynamic, "r--", range( 35 ), times_recursive, "b--" )
    plt.title("Linear Scale")
    plt.ylabel("Execution time (seconds)")

    plt.subplot(212)
    plt.plot( range( 35 ), times_dynamic, "r--", range( 35 ), times_recursive, "b--" )
    plt.title("Logarithmic Scale")
    plt.xlabel("N")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    time_fib()
