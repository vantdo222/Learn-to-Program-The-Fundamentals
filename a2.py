def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1)>len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num_nucleotide = 0
    for nu in dna:
        if nu == nucleotide:
            num_nucleotide = num_nucleotide + 1
    return num_nucleotide

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (That is, it contains no characters other than 'A', 'T', 'C', and 'G')

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATXEGC')
    False

    """

    valid = True
    for nu in dna:
        if nu not in 'ATCG':
            valid = False
    return valid

def insert_sequence(dna1, dna2, int):
    """(str, str, int) -> str

    Return the DNA sequence obtained by inserting dna2 into dna1 at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ATCT', 'GG', 3)
    'ATCGGT'

    """

    return dna1[:int] + dna2 + dna1[int:]

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.
    
    >>> get_complement('A')
    T
    >>> get_complement('C')
    G

    """

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

def get_complementary_sequence(dna):
    """(str) -> str

    Return the DNA sequence that is complementary to dna.

    >>> get_complementary_sequence('ATCG')
    TAGC
    >>> get_complementary_sequence('CCGA')
    GGCT

    """

    complementary_sequence = ''
    for nu in dna:
        complementary_sequence = complementary_sequence + get_complement(nu)
    return complementary_sequence
