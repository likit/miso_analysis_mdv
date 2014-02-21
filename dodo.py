'''A dodo.py for finding differential exon usage using MISO.'''

import os
import doit

def task_build_SE_annot():
    '''builds skipped exons splicing annotation'''

    os.chdir(doit.initial_workdir)
    cmd = 'python protocol/find_SE.py ../asm_cuff_ref_models.flt.bed > asm_cuff_ref_models.flt.SE.gff'
    return {
            'actions': [cmd],
            }

def task_build_SE_index():
    '''builds an index for skipped exons'''

    os.chdir(doit.initial_workdir)
    cmd = 'index_gff.py --index asm_cuff_ref_models.flt.SE.gff cuffref-index/SE'
    return {
            'actions': [cmd],
            }

def task_run_MISO_SE():
    '''run MISO for skipped exons'''

    os.chdir(doit.initial_workdir)
    for sample in ['line6u', 'line6i', 'line7u', 'line7i']:
        cmd = 'qsub -v "input_bam=bam-data/%s.bam,index_dir=cuffref-index/SE' \
                ',output_dir=cuffref-results/SE,event=SE"' \
                ' protocol/miso.sh' % (sample)

        yield {
                'actions': [cmd],
                'name': sample,
                }
