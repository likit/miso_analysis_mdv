import sys
import csv


def read_gff(infile):
    reader = csv.reader(open(infile), dialect="excel-tab")
    transcripts = []
    first_gene = False
    for row in reader:
        if not first_gene:
            first_gene = True
            transcripts.append(row)
            continue
        if row[2] == "gene":
            yield transcripts
            transcripts = [row]
        else:
            transcripts.append(row)

    yield transcripts


def write_bed(transcript):
    exon_starts = []
    exon_sizes = []
    chrom = transcript[1][0]
    strand = transcript[1][6]
    id = transcript[1][8].split(';')[0]
    chrom_start = int(transcript[1][3])
    chrom_end = int(transcript[-2][3])

    for exon in transcript[1:-1]:
        start = int(exon[3]) - chrom_start
        size = int(exon[4]) - int(exon[3])
        exon_starts.append(str(start))
        exon_sizes.append(str(end))

    print '%s\t%d\t%d\t%s\t1000\t%s\t%d\t%d\t0,0,0\t%d\t%s\t%s' % \
            (chrom, chrom_start, chrom_end, 


def covert_skipped_exon(gene):
    transcript = []
    for item in gene:
        if item[2] == "gene":
            continue
        elif item[2] == "mRNA":
            if transcript[1:-1]:
                write_bed(transcript)
            transcript = []
        else:
            transcript.append(item)

    if transcript[1:-1]:
        write_bed(transcript)


def main():
    infile = sys.argv[1]
    convert = convert_skipped_exon
    for gene in read_gff(infile):
        convert(gene)

if __name__ == "__main__":
    main()
