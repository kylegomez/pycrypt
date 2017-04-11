#!/usr/bin/env python
import sys

class Text:
    def __init__(self, filename = 0):
        if filename:
            self.load(filename)

    def set(self, lst):
        self.text = "".join(lst)

    def get(self):
        return self.text

    def load(self, filename):
        fp = open(filename, "r")
        self.rawtext = fp.read()
        fp.close
        self.text = self.convert(self.rawtext)

    def convert(self, txt):
        rval = ""
        pos = 1
        for c in txt:
            if c.isalpha():
                rval += c.upper()
                pos += 1

            if pos % 60 == 0:
                rval += "\n"
            elif pos % 5 == 0:
                rval += " "
        return rval

    def __str__(self):
        return self.text

if __name__ == "__main__":
    if len(sys.argv) == 2:
        txt = Text(sys.argv[1])
    else:
        print "Error"
        sys.exit(1)

    print txt
