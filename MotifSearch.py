import random

'''Implement random motif search algorithm'''

class RandomSearch:
    '''Performs random motif search algorithm on a set of sequences'''
    def __init__(self):
        pass


class Profile:
    '''Contains sequences of DNA with an implanted motif'''
    def __init__(self, num_seq=1000, len_seq=500, motif='AAAAAA', language='ACGT', mut_rate=0):
        self.num_seq = num_seq
        self.len_seq = len_seq
        self.motif = motif
        self.profile = []
        self.language = 'ACGT'

        self.create_profile()
        #self.implant_motif()

    def create_profile(self):

        for s in range(self.num_seq):
            sequence = "".join(
                random.choice(self.language) for i in range(self.len_seq)
            )
            self.profile.append(
                self.implant_motif(sequence)
            )

    def implant_motif(self, sequence):
        len_motif = len(self.motif)
        start_motif = random.choice(
            range(self.len_seq-len_motif)
        )
        implanted = sequence[:start_motif] + self.motif + sequence[start_motif+len_motif:]
        return implanted




