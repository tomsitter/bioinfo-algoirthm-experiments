from collections import defaultdict
from string import maketrans

def reverse_complement(seq):
    '''Given a DNA sequence, prints the reverse complement'''
    forward = 'ATGC'
    reverse = 'TACG'

    revseq = seq[-1::-1]
    comp = revseq.translate(maketrans(forward, reverse))

    return comp

def list_occurences(pattern, seq):
    '''Return list of all occurences of a pattern in a sequence'''
    occurences = []
    for i, _ in enumerate(seq):
        if seq[i:i+len(pattern)] == pattern:
           occurences.append(i)
    return occurences

def count_occurences(pattern, seq):
    return len(list_occurences(pattern, seq))

def calc_skew(sequence):
    '''Returns a list of the skew of the sequence in respect to CG'''
    skew_list = [0]
    skew = 0
    for n in sequence:
        if n =='G':
            skew += 1
        elif n == 'C':
            skew -= 1
        skew_list.append(skew)

    return skew_list

def minimum_skew(sequence):
    '''Return location with minimum skew (ori c)'''
    skew = calc_skew(sequence)

    minima = min(skew)

    ori_c = [i for i, s in enumerate(skew) if s==minima]
    
    return ori_c

def hamming_distance(seq1, seq2):

    if len(seq1) != len(seq2):
        raise ValueError('Both sequences must be same length')

    distance = 0
    for s1, s2 in zip(seq1, seq2):
            if s1 != s2:
                distance+=1
    return distance

def approx_match(pattern, distance, sequence):
    matches = []
    for i in range(len(sequence)-len(pattern)+1):
        section = sequence[i:i+len(pattern)]
        if hamming_distance(pattern, section) <= distance:
                matches.append(i)

    return matches

def count_approx_matches(pattern, distance , sequence):
    return len(approx_match(pattern, distance, sequence))

def most_frequent_approximate_matches(sequence, k, distance):
    kmers = {}

    for i,_ in enumerate(sequence):
        pattern = sequence[i:i+k]
        kmers[pattern] = 0

def mutations(pattern, distance):
    mutations = [pattern]
    for i, p in enumerate(pattern):
        translations = set(language) - set(p)
        for e in translations:
            mutations.append(
                pattern[:i] + e + pattern[i+1:]
            )
    return mutations



3 * 4 = 12