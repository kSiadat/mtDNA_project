def subSeq(centre, window, seq):
    '''Get a windowed subset of a circular string/sequence'''
    start = centre - window
    end = centre + window
    if start >= 0 and end < len(seq):
        subseq = seq[start:(end+1)]
    elif start < 0 and end >= len(seq):
        subseq = seq[start:]+seq+seq[0:(end-len(seq)+1)]
    elif start < 0:
        subseq = seq[start:]+seq[0:(end+1)]
    elif end >= len(seq):
        subseq = seq[start:]+seq[0:(end-len(seq)+1)]
    return(subseq)
