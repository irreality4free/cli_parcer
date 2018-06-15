from struct import *

s = open("s_11zzz1_ex.cli", "r").read()
s = s.split("$$HEADEREND")[1]
# s = s.split(chr(0x1)+chr(0x0)+chr(0x1))
j = 0
global count
count = 0

def get_command(s):
    global count
    c = unpack("H", s[:2])[0]

    s = s[2:]
    print c
    if c == 128:  # layer
        z = unpack("H", s[:2])
        s = s[2:]
        print "Start layer (128) %s" % z
        count+=1
        print( "layer num - "+str(count))

    elif c == 129:
        id_ = unpack("H", s[:2])
        s = s[2:]
        dir_ = unpack("H", s[:2])
        s = s[2:]
        n = unpack("H", s[:2])[0]
        s = s[2:]
        print "Start polyline (129) id: %s; dir: %s; n: %s;" % (id_, dir_, n)
        for i in range(n):
            x, y = unpack("HH", s[:4])
            s = s[4:]
            # print "%0.2f, %0.2f    " % (float(x) / 65536 * 100 - 50, float(y) / 65536 * 100 - 50),
            print(x)
            print(y)
        print
    else:
        print('Error')
        print(c)
        return
    return s


while len(s) > 0:
    s = get_command(s)
