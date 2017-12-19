import io
import sys


if __name__ == '__main__':
    path = raw_input('file path, please?')
    f = open(path, 'r')
    
    for line_no, line in enumerate(f):
        # Remember not to count the newline character
        if len(line.strip()) != 32:
            print line_no, line
    
    
    for line in f:
        for i in range(0, 3):
            print line[i]
    f.close()