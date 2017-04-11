from crypto import *

class MonomeDinome:
    def __init__(self, letterkw, numberkw):
        self.letterkey = self.lettersScramble(letterkw)
        self.numberkey = self.digitsScramble(numberkw)

    def encrypt(self, pt):
        rlist = []
        for c in pt.get():
            if c == 'J':
                c = 'I'
            if c == 'W':
                c = 'V'
            pos = self.letterkey.find(c)

            if pos == -1:
                continue
            elif pos < 8:
                rlist.append(self.numberkey[pos+2])
            elif pos < 16:
                rlist.append(self.numberkey[0])
                rlist.append(self.numberkey[pos-8+2])
            elif pos < 24:
                rlist.append(self.numberkey[1])
                rlist.append(self.numberkey[pos-16+2])
            else:
                continue
        
        ct = Text()
        ct.set(rlist)
        return ct

    def decrypt(self, ct):
        rlist = []
        saved = -1
        for c in ct.get():
            pos = self.letterskey.find(c)
                if pos == 0 or pos == 1:
                    saved = pos
                elif saved == -1:
                    pos = pos - 2
                    rlist.append(self.letterskey[pos])
                else:
                    pos = pos - 2 + 8 + saved * 8
                    rlist.append(self.letterskey[pos])
                    saved = -1
        pt = Text()
        pt.set(rlist)
        return pt



    def digitsScramble(self, numberkw):
        digitbuf = list((numberkw.upper() + "ZZZZZZZZZZ")[0:10])
        numbers = "0123456789"        
        for n in numbers:
            pos = self.findLowestLetter(digitbuf)
            if pos != -1:
                digitbuf[pos] = n
        return "".join(digitbuf)

    def findLowestLetter(self, larray):
        pos = -1
        lowest = ""

        for i in range(len(larray)):
            if larray[i].isalpha():
                if (lowest == '') or (larray[i] < lowest):
                    lowest = larray[i]
                    pos = i
        return pos

    def lettersScramble(self, letterkw):
        rlist = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVXYZ"
        for c in letterkw.upper():
            if c == 'J':
                c = 'I'
            if c == 'W':
                c = 'V'
            if not c in rlist:
                rlist.append(c)

        for c in alphabet:
            if not c in rlist:
                rlist.append(c)

        return "".join(rlist)

    def __str__(self):
        return "letter keyword: " + self.letterkey + "\n" + \
        "number keyword: " + self.numberkey
