# From https://leetcode.com/problems/decode-ways/

def numDecodings( s ):
    # Number of possible string decodings, as described in lecture.
    # Doesn't handle silly corner cases for clarity (e.g., will break
    # on invalid input / 0 length strings)
    array = [ 1 ]
    for i in range( 1, len( s ) ):

        # Pull off previous 2 characters to check for 1 and 2 number encodings
        char = s[ i ]
        prev_char = s[ i - 1 ]

        # Either our new number could be used to form a 1-letter encoding,
        # or a 2-letter encoding
        case1 = array[ i - 1 ] if char != "0" else 0
        case2 = array[ i - 2 ] if int( prev_char + char ) in range( 10, 27 ) else 0

        # Combine by summing
        array.append( case1 + case2 )

    return array[ -1 ]
