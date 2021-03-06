calculate-insert-length:
	pe_utils.py --compute-insert-len \
	line6u_tophat/accepted_hits.bam,line6i_tophat/accepted_hits.bam,line7u_tophat/accepted_hits.bam,line7i_tophat/accepted_hits.bam  \
	exons/line67_split_cuff_models.nr99.multiexons.min_1000.const_exons.gff --output-dir insert-dist

build-index:
	index_gff.py --index line67_split_cuff_models.nr99.SE.gff indexes/SE
	
compute-expression-no-cluster:
	run_events_analysis.py --compute-genes-psi indexes/SE line6u_tophat/accepted_hits.bam \
	--output-dir results/SE/line6u --read-len 75 --paired-end 171.9 46.5 \
	--settings-filename=~/miso_settings.txt --event-type SE --chunk-jobs 100
	
compute-expression-with-cluster:
	qsub line6i_miso.sh
	qsub line6u_miso.sh
	qsub line7i_miso.sh
	qsub line7u_miso.sh
	
summarize-results:
	run_miso.py --summarize-samples results/SE/line6u/ results/SE/line6u/summary
	run_miso.py --summarize-samples results/SE/line6i/ results/SE/line6i/summary
	run_miso.py --summarize-samples results/SE/line7u/ results/SE/line7u/summary
	run_miso.py --summarize-samples results/SE/line7i/ results/SE/line7i/summary
