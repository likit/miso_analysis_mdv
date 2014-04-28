#!/opt/local/bin/python
import sys
import csv

from pygr import seqdb, sequtil


def get_sequence(infile, genome):
    reader = csv.reader(open(infile), dialect='excel-tab')
    for rec in reader:
        attrs = dict([(key, value) for key, value in 
                [item.split('=') for item in rec[-1].split(';')]])
        exon_start = int(attrs["exonStart"]) - 1
        exon_end = int(attrs["exonEnd"])
        chrom = rec[0]
        strand = attrs["strand"]
        id = attrs["ID"]
        exon_seq = genome[chrom][exon_start:exon_end]
        if strand == '-':
            exon_seq = str(-exon_seq)
        else:
            exon_seq = str(exon_seq)

        sequtil.write_fasta(sys.stdout, exon_seq, id=id)


def main():
    infile = sys.argv[1]
    genome = seqdb.SequenceFileDB(sys.argv[2])

    get_sequence(infile, genome)


if __name__ == '__main__':
    main()
