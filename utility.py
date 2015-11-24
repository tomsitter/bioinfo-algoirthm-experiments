from string import maketrans

def reverse_complement(seq):
    '''Given a DNA sequence, prints the reverse complement'''
    forward = 'ATGC'
    reverse = 'TACG'

    revseq = seq[-1::-1]
    comp = revseq.translate(maketrans(forward, reverse))

    return comp

def all_occurences(pattern, seq):
    '''Return list of all occurences of a pattern in a sequence'''
    occurences = []
    for i, _ in enumerate(seq):
        if seq[i:i+len(pattern)] == pattern:
           occurences.append(i)
    return occurences