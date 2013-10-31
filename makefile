calculate-insert-length:
  pe_utils.py --compute-insert-len \
  line6u_tophat/accepted_hits.bam,line6i_tophat/accepted_hits.bam,line7u_tophat/accepted_hits.bam,line7i_tophat/accepted_hits.bam  \
  exons/line67_split_cuff_models.nr99.multiexons.min_1000.const_exons.gff --output-dir insert-dist
