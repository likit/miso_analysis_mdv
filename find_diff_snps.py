'''Finds SNPs from the first file that are not in the second file.'''

import sys
from collections import namedtuple, defaultdict


SNP = namedtuple('SNP', ['chr', 'position', 'ref', 'alt', 'score'])

def parse(vcf_file, comment_sign='#'):
    snps = defaultdict(dict)
    for line in open(vcf_file):

        if line.startswith(comment_sign):
            continue

        items = line.split()
        snp = SNP(items[0], items[1], items[3],
                        items[4], float(items[5]))
        snps[items[0]][items[1]] = snp

    return snps


def print_snp(snp1, snp2=None):
    if not snp2:
        print '\t'.join([snp1.chr, snp1.position, '.',
                        snp1.ref, snp1.alt, str(snp1.score),
                        '.', snp1.ref, 'NA', '.'])
    else:
        print '\t'.join([snp1.chr, snp1.position, '.', snp1.ref,
                            snp1.alt, str(snp1.score), '.', snp2.alt,
                            str(snp2.score), '.'])

def find_diff_snps(snps1, snps2, minscore):
    for chrom in snps1:
        for pos in snps1[chrom]:
            snp1 = snps1[chrom][pos]
            try:
                snp2 = snps2[chrom][pos]
            except KeyError:
                if snp1.score >= minscore:
                    print_snp(snp1)
            else:
                if snp1.alt.upper() != snp2.alt.upper():
                    if snp1.score >= minscore:
                        print_snp(snp1, snp2)

def main():
    vcf_file1 = sys.argv[1]
    vcf_file2 = sys.argv[2]
    minscore = float(sys.argv[3])

    snps1 = parse(vcf_file1)
    snps2 = parse(vcf_file2)

    find_diff_snps(snps1, snps2, minscore)


if __name__=='__main__':
    main()
