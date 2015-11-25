'''Implement random motif search algorithm'''
import random


class RandomSearch:
    '''Performs random motif search algorithm on a set of sequences'''
    def __init__(self):
        pass


class Profile:
    '''Contains sequences of DNA with an implanted motif'''

    def __init__(self, num_seq=1000, len_seq=500,  mut_rate=0, motif='AAAAAA', language='ACGT'):
        '''Create profile based on parameters passed in'''
        self.num_seq = num_seq
        self.len_seq = len_seq
        self.mut_rate = mut_rate
        self.motif = list(motif)
        self.language = list(language)
        self.profile = []

        self.create_profile()

    def __str__(self):
        output = "motif: {motif}\nprofile:\n".format(motif = "".join(self.motif))
        for sequence in self.profile:
            output += "".join(sequence) + "\n"
        return output

    def create_profile(self):
        '''Randomly generate sequences from language and randomly implant motif'''

        for s in range(self.num_seq):
            sequence = self.create_sequence()
            self.profile.append(
                self.implant_motif(sequence)
            )

    def create_sequence(self):
        mutated_sequence = self.mutate(
            [random.choice(self.language) for i in range(self.len_seq)]
        )
        return mutated_sequence

    def implant_motif(self, sequence):
        '''Implant a motif in a random location in a sequence'''

        len_motif = len(self.motif)
        start_motif = random.choice(
            range(self.len_seq-len_motif)
        )
        implanted = sequence[:start_motif] + self.motif + sequence[start_motif+len_motif:]
        return implanted

    def mutate(self, sequence, strict=False):
        '''Adds random mutations to a sequence at mut_rate'''

        #generate mutations at random positions and substitute them
        #note: a position may get changed to itself (prob = 1/len(language) -- usually 1/4)
        #note: a position may get mutated twice -- effectively reducing mutation rate
        if strict:
            '''All sequences must have mut_rate mutations'''
            pass
        for i in range(self.mut_rate):
            ''' Mutations occur sequentially and completely randomly
                mutations may overwrite previous mutations or elements may mutate to themselves
            '''
            pos = random.choice(len(sequence))
            mutation = random.choice(self.language)
            sequence[pos] = mutation

        return sequence


