#! /usr/bin/python

from sys import argv
script, word = argv

class Twister(object):

    FILENAME = 'words.txt'

    def __init__(self, solve):
        self.solve = solve

    def twist(self):
        with open(self.FILENAME) as f:
            for line in f:
                word = line.strip()
                if len(str(self.solve)) == len(word):
                    if sorted(word) == sorted(str(self.solve)):
                        print word

            print 'done...'


if __name__ == '__main__':
    twist_me = Twister(word)
    twist_me.twist()
