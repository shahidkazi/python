'''
Encode/Decode the string based on the input. The output should be based on the key. 
There are following 3 inputs from the user:
int (operation o-for encode, 1-for decode)
string (input string – word which is to be encoded/decoded)
string (key to encode/decode e.g. 123)e.g.

Input:
0
open
123

Expected output:
oppeeen
'''

def encode(inp, code):
    ''' Function to encode a string using the given code '''
    res = ''
    idx = 0
    for i in code:
        res += inp[idx] * int(i)
        idx += 1
    res += inp[idx:]
    return res


def decode(inp):
    ''' Function to decode a given encoded string '''
    res = ''
    count = 1
    for i in range(len(inp) - 1):
        if inp[i] == inp[i+1]:
            count += 1
        else:
            res += str(count)
            count = 1

    return res


# Driver Code
if __name__ == '__main__':
    op = input()
    inp = input()
    code = input()

    if op == '0':
        print(encode(inp, code))
    else:
        print(decode(inp))
