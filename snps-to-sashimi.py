'''Parse SNPs from miso-to-snps.py output and write
only a gene name to a stdout.

'''

import sys

if len(sys.argv) < 2:
    print >> sys.stderr, '[Usage] snps-to-sashimi.py input1 input2 ...'
    print >> sys.stderr, 'Please specify input file(s).'
    raise SystemExit

all_genes = set()
for filename in sys.argv[1:]:
    for line in open(filename):
        gene_name = line.strip().split('\t')[5].split('.')
        gene_name = '.'.join(gene_name[:2])
        if gene_name not in all_genes:
            all_genes.add(gene_name)

for gene in all_genes:
    print gene
