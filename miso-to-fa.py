#!/opt/local/bin/python
import sys
import csv

from Bio import SeqIO


def get_sequence(infile, genome):
    '''Reads input from Miso and get sequences from 
    the genome or transcripts.

    '''

    sequences = set()
    reader = csv.reader(open(infile), dialect='excel-tab')
    for rec in reader:
        seqid = rec[0].split('.')[0].replace('-', ':')
        sequences.add(seqid)

    for rec in SeqIO.parse(genome, 'fasta'):
        rec.description = ''
        recid = rec.id.split('.')[0]
        if recid in sequences:
            SeqIO.write(rec, sys.stdout, 'fasta')


def main():
    infile = sys.argv[1]
    genome = sys.argv[2]

    get_sequence(infile, genome)


if __name__ == '__main__':
    main()
