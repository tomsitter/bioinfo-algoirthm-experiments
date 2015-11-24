'''
    Find most frequent patterns in a randomly generated sequence
    The sequence is generated by random selection from the string choices

    Sample usage:
        >python most_frequent_kmer.py -n 10000 -k 6 --choices='ctga'
    
    Default parameters:
    n = 5000
    k = 5
    choices = 'atgc'
'''


import random
from collections import defaultdict
import sys, getopt

def main(argv, n=5000, k=5, choices='ACTG', filename='', count_compliments=False):

    try:
        opts, args = getopt.getopt(argv, 'n:k:h', ['filename=', 'seq=', 'choices=', 'help', 'compliment'])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == '-n':
            n = int(a)
        elif o == '-k':
            k = int(a)
        elif o == '--filename':
            filename = a
        elif o == '--compliment':
            count_compliments = True
        elif o =='--seq':
            seq = a
        elif o in ('-h', '--help'):
            usage()
            sys.exit()
        else:
            print o, a
            assert False, 'Unhandled option'

    if filename:
        with open(filename) as f:
            lines = f.readlines()
            seq = lines[0].rstrip()
            k = int(lines[1])

    if not seq:
        seq = "".join(random.choice(choices) for _ in range(n))

    matches = defaultdict(int)

    #Go from the first element to the n-kth element
    #Count everytime this pattern has been seen before
    for i in range(0, len(seq)-k+1):
        matches[seq[i:i+k]] += 1

    #By caching this line you can improve performance 10x
    max_count = max(matches.values())

    #Find the keys that appear the most
    print 'Most frequent'
    most_frequent = [(key, value) for key, value in matches.items() if value==max_count]

    print " ".join(k for k,v in most_frequent)

    if count_compliments:
        print 'Reverse compliments'
        compliments = find_compliments(most_frequent, seq)
        for k, v in compliments:
            print k, ':', v


def find_compliments(most_frequent, seq):
    compliments = []
    for key, value in most_frequent:
        #reverse
        compliment = key[-1::-1]
        count = seq.count(compliment)
        compliments.append((compliment, count))
    return compliments

def usage():
    print 'Finds the most frequent k length text pattern in a sequence'
    print 'Options'
    print '-n           length of sequence'
    print '-k           length of pattern'
    print '--choices    string of characters in sequence'

if __name__ == "__main__":
    main(sys.argv[1:])