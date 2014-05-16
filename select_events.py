''' Selects DEU exons from GFF file. The script requires MISO output and
an splicing annotation file.

'''

#!/opt/local/bin/python

import sys
import csv
from itertools import islice


starts_ends = {}  # for retained intron

def read_gff(infile):
    reader = csv.reader(open(infile), dialect="excel-tab")
    transcripts = []
    first_gene = False
    for row in reader:
        if not first_gene:
            first_gene = True
            transcripts.append(row)
        elif row[2] == "gene":
            yield transcripts
            transcripts = [row]
        else:
            transcripts.append(row)

    yield transcripts


def select_RI(transcripts):
    exon3 = transcripts[5]
    exonid = exon3[8].split(';')[0].lstrip('ID=')
    exon1_end = int(transcripts[2][4])
    exon2_start = int(transcripts[3][3])
    # print >> sys.stderr, exon3[-1], exon1_end, exon2_start

    '''add 10 bp flanking nucleotides to both ends'''
    starts_ends[exonid] = (str(exon1_end - 10), str(exon2_start + 10))

    yield [exon3]


def select_SE(transcripts):
    exons = []
    for trns in transcripts:
        if trns[2] == 'mRNA':
            if len(exons) > 2:
                yield exons[1:-1]
                exons = []
        if trns[2] == 'exon':
            exons.append(trns)

    if len(exons) > 2:
        yield exons[1:-1]


def select_A5SS(transcripts):
    strand = transcripts[0][6]
    # exons = [x for x in transcripts if x[2] == 'exon']
    if strand == '-':
        exons = islice([x for x in transcripts if \
                x[2] == 'exon'], 1, None, 2)
        exons = sorted(exons, key=lambda x: (int(x[3]), int(x[4])))
    else:
        exons = islice([x for x in transcripts if \
                x[2] == 'exon'], 0, None, 2)
        exons = sorted(exons, key=lambda x: (int(x[3]), int(x[4])),
                                                        reverse=True)
    yield [exons[0]]

def main():
    annot_file = sys.argv[1]
    result_file = sys.argv[2]

    events = {'SE': select_SE,
                'A5SS': select_A5SS,
                #'RI': select_RI,
            }
    select = events[sys.argv[3]]

    deu = set()
    reader = csv.reader(open(result_file), dialect='excel-tab')
    for rec in reader:
        deu.add(rec[0])

    selected_exons = set()
    for transcripts in read_gff(annot_file):
        for exons in select(transcripts):
            for exon in exons:
                exonid = exon[8].split(';')[0].lstrip('ID=')
                geneid, eventid = exonid.split('.')[:2]
                exn = '.'.join([geneid, eventid])
                if exn in deu:
                    selected_exons.add(exonid)

    with open(annot_file) as af:
        reader = csv.reader(af, 'excel-tab')
        for rec in reader:
            exonid = rec[-1].split(';')[0].lstrip('ID=')
            if exonid in selected_exons:
                print '\t'.join(rec)


if __name__ == '__main__':
    main()
