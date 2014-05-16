'''Reads mRNA start and end from MISO output and call samtools mpileup
and bcftools to call SNPs within the mRNA.

'''

import sys
import subprocess
import csv

def main():
    regions = set()
    with open(sys.argv[1]) as miso:
        reader = csv.reader(miso, 'excel-tab')
        for rec in reader:
            starts = [int(s) - 1 for s in rec[-2].split(',')]
            ends = rec[-1].split(',')
            chrom = rec[-4]
            event = rec[0]
            for i in range(len(starts)):
                region = '%s:%d-%s' % (chrom, starts[i], ends[i])
                if region not in regions:
                    regions.add(region)
                    genome = sys.argv[2]
                    outfile = sys.argv[3]
                    bamfiles = ' '.join(sys.argv[4:])
                    command = 'samtools mpileup -uf %s -r %s %s |' \
                                'bcftools view -cvg - | grep -v \# > %s' \
                                % (genome, region, bamfiles, outfile + '_' + event)
                    subprocess.call(command, shell=True)

if __name__=='__main__':
    usage = '\n\nUsage: miso-call-snps.py miso-file genome output-file bam1 bam2 ...\n'
    if len(sys.argv) == 1:
        print >> sys.stderr, usage
    else:
        main()
