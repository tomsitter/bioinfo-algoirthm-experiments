with open('dataset_2_6.txt') as f:
    lines = f.readlines()

    seq = lines[0].rstrip()
    pattern = lines[1].rstrip()

    count = 0
    for i in range(0, len(seq) - len(pattern) + 1):
        if seq[i:i+len(pattern)] == pattern:
            count+=1

    print count

