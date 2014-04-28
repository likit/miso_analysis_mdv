#!/opt/local/bin/python

'''Coordinates in the ouput is 1-based.'''

import sys
import csv


def read_filtered_results(infile):
    events = []
    reader = csv.reader(open(infile), dialect='excel-tab')
    for row in reader:
        if row[0] == 'event_name':
            continue
        else:
            events.append(row[0])
    return events


def read_snps(infile, events):
    snps = set()
    reader = csv.reader(open(infile), dialect='excel-tab')
    writer = csv.writer(sys.stdout, dialect='excel-tab')
    for row in reader:
        exonid = row[-1].split(';')[0].lstrip('ID=')
        geneid, eventid, mrnaid, exnid = exonid.split('.')
        id = geneid + '.' + eventid
        if id in events:
            strand = row[-3]
            if strand == '-':
                rel_exon_end = int(row[-5]) - int(row[-6]) + 1
                rel_snp_pos = int(row[1]) - int(row[-6]) + 1
                rel_snp_pos = rel_exon_end - (rel_snp_pos - 1)
            else:
                rel_snp_pos = (int(row[1]) - int(row[-6])) + 1

            new_snp = ":".join([row[1], str(rel_snp_pos),
                            row[0], row[-6], row[-5]])

            attribs = "ID=%s;exonStart=%s;exonEnd=%s;strand=%s;line7_alt=%s;relpos=%d"\
                        % (exonid, row[13], row[14], row[-3],row[8], rel_snp_pos)

            if new_snp not in snps:
                writer.writerow([row[0], row[1], '.', row[3], row[4],
                                    row[5], '.', attribs,
                                    ])
                snps.add(new_snp)


def main():
    result_file = sys.argv[1]
    snps_file = sys.argv[2]

    events = read_filtered_results(result_file)
    read_snps(snps_file, events)


if __name__ == '__main__':
    main()
