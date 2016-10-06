# From https://leetcode.com/problems/house-robber/

def house_robber( H ):
    # Takes a list of house values and returns the max
    # money a robber can make robbing houses such that
    # no two adjacent houses are robbed
    R = [ H[ 0 ], max( H[ 0 ], H[ 1 ] )] # base cases
    for i in range( 2, len( H ) ):
        case1 = R[ i - 1 ] # House i isn't robbed
        case2 = H[ i ] + R[ i - 2 ] # House i is robbed
        R.append( max( case1, case2 ) )
    return R[ -1 ] # Return final element of R
