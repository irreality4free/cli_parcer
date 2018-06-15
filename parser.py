# -*-coding:utf-8 -*-
from struct import *
import codecs


class Parser:
    def __init__(self,name):
        self.name = name
        self.j = 0
        self.element = 0
        self.layer = 0
        self.layers = dict()

    def Open(self):
        with open(self.name, "rb") as  f:
            self.s = f.read()
            self.s = self.s.split(b"$$HEADEREND")[1]

    def get_command(self,s):


        c = unpack("H", s[:2])[0]

        s = s[2:]
        print(c)
        if c == 128:  # layer
            self.layer += 1
            self.layers[str(self.layer)] = list()
            print(str(self.layer) + ' layer num')
            z = unpack("H", s[:2])[0]
            s = s[2:]
            element = 0
            print("Start layer (128) %s" % z)
        elif c == 129:
            id_ = unpack("H", s[:2])
            s = s[2:]
            dir_ = unpack("H", s[:2])
            s = s[2:]
            n = unpack("H", s[:2])[0]
            s = s[2:]
            print("Start polyline (129) id: %s; dir: %s; n: %s;" % (id_, dir_, n))
            coord_list = list()
            for i in range(n):
                x, y = unpack("HH", s[:4])

                s = s[4:]
                x_scaled, y_scaled = int(float(x) / 65536 * 10000 - 1100), int(float(y) / 65536 * 10000 - 1100)

                coord_list.append(x_scaled)
                coord_list.append(y_scaled)

                # print(x_scaled, y_scaled)
                print(x, y)
            print()
            self.layers[str(self.layer)].append(coord_list)
            self.element += 1
        else:
            print ("Bad command found! c = %s"%c)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            i = unpack("H", s[:2])
            s = s[2:]
            print(i) # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)
            # i = unpack("H", s[:2])
            # s = s[2:]
            # print(i)





            return ""
        return s

    def Run(self):
        self.Open()
        while len(self.s) > 0:
            self.s = self.get_command(self.s)

        self.parced_layers = self.layers
        print(self.layers['1'])


if __name__ == '__main__':

    par = Parser("s_11zzz1_ex.cli")
    par.Run()

