#!/opt/local/bin/python
'''Filters results from MISO with CI and other criteria.'''

import sys


def check_CI(info, ci_range=0.20):
    '''Retrun true if all CIs are smaller than the cutoff.'''

    sample1_lo = info[2].split(',')
    sample1_hi = info[3].split(',')
    sample2_lo = info[5].split(',')
    sample2_hi = info[6].split(',')

    for i in range(len(sample1_lo)):
        r = float(sample1_hi[i]) - float(sample1_lo[i])
        if r > ci_range:
            # print info[0], r
            return False

    for i in range(len(sample2_lo)):
        r = float(sample2_hi[i]) - float(sample2_lo[i])
        if r > ci_range:
            # print info[0], r
            return False

    return True


def check_skipped_exon_max(info, se_max=1):
    for isoform in info[9].split(','):
        if (len(isoform.split('_')) - 2) > se_max:
            # print info[0], isoform.split('_'),
            # print 'exceeded', len(isoform.split('_')) - 2
            return False
    return True


def check_delta_psi(info, delta_psi):
    for dp in info[7].split(','):
       if abs(float(dp)) >= delta_psi:
           return True

    return False


def check_bayes_factor(info, bayes_factor):
    for bf in info[8].split(','):
        if float(bf) >= bayes_factor:
            return True

    return False


def filter_SE(input_file, ci_range, delta_psi, bayes_factor, se_max):
    total_events = 0
    passed_events = 0
    for event in open(input_file):
        total_events += 1
        info = event.split()
        if info[0] == 'event_name':
            continue
        if not check_skipped_exon_max(info, se_max):
            continue
        if not check_delta_psi(info, delta_psi):
            continue
        elif not check_bayes_factor(info, bayes_factor):
            continue
        elif not check_CI(info, ci_range):
            continue
        else:
            print '\t'.join(info)
            passed_events += 1
    return total_events, passed_events


def filter_ASS(input_file, ci_range, delta_psi, bayes_factor):
    total_events = 0
    passed_events = 0
    for event in open(input_file):
        total_events += 1
        info = event.split()
        if info[0] == 'event_name':
            continue
        if not check_delta_psi(info, delta_psi):
            continue
        elif not check_bayes_factor(info, bayes_factor):
            continue
        elif not check_CI(info, ci_range):
            continue
        else:
            print '\t'.join(info)
            passed_events += 1
    return total_events, passed_events


def main():
    filters = {'SE':filter_SE,
                'ASS': filter_ASS,
                }

    input_file = sys.argv[1]
    event_type = sys.argv[2]
    ci_range = float(sys.argv[3])
    delta_psi = float(sys.argv[4])
    bayes_factor = float(sys.argv[5])

    if event_type == 'SE':
        skipped_exon_max = int(sys.argv[6])  # for SE only
        total, passed = filter_SE(input_file, ci_range, delta_psi, bayes_factor, skipped_exon_max)
    else:
        filter = filters[event_type]
        total, passed = filter(input_file, ci_range, delta_psi, bayes_factor)

    print >> sys.stderr, 'Total %d events, passed %d events' % (total, passed)

if __name__=='__main__':
    main()
