build-a3ss-models:

	cd miso; python ~/gimme/src/utils/find_A3SS.py ../asm_cuff_ref_models.flt.bed > asm_cuff_ref_models.flt.A3SS.gff

build-a3ss-index: build-a3ss-models

	cd miso; index_gff.py --index asm_cuff_ref_models.flt.A3SS.gff cuffref-index/A3SS

build-a5ss-models:

	cd miso; python ~/gimme/src/utils/find_A5SS.py ../asm_cuff_ref_models.flt.bed > asm_cuff_ref_models.flt.A5SS.gff

build-a5ss-index: build-a5ss-models

	cd miso; index_gff.py --index asm_cuff_ref_models.flt.A5SS.gff cuffref-index/A5SS

build-mxe-models:

	cd miso; python ~/gimme/src/utils/find_MXE.py ../asm_cuff_ref_models.flt.bed > asm_cuff_ref_models.flt.MXE.gff

build-mxe-index: build-mxe-models

	cd miso; index_gff.py --index asm_cuff_ref_models.flt.MXE.gff cuffref-index/MXE

summarize-se:

	cd miso; run_miso.py --summarize-samples cuffref-results/SE/line6u cuffref-results/SE/line6u
	cd miso; run_miso.py --summarize-samples cuffref-results/SE/line6i cuffref-results/SE/line6i
	cd miso; run_miso.py --summarize-samples cuffref-results/SE/line7u cuffref-results/SE/line7u
	cd miso; run_miso.py --summarize-samples cuffref-results/SE/line7i cuffref-results/SE/line7i

summarize-a3ss:

	cd miso; run_miso.py --summarize-samples cuffref-results/A3SS/line6u cuffref-results/A3SS/line6u
	cd miso; run_miso.py --summarize-samples cuffref-results/A3SS/line6i cuffref-results/A3SS/line6i
	cd miso; run_miso.py --summarize-samples cuffref-results/A3SS/line7u cuffref-results/A3SS/line7u
	cd miso; run_miso.py --summarize-samples cuffref-results/A3SS/line7i cuffref-results/A3SS/line7i

summarize-a5ss:

	cd miso; run_miso.py --summarize-samples cuffref-results/A5SS/line6u cuffref-results/A5SS/line6u
	cd miso; run_miso.py --summarize-samples cuffref-results/A5SS/line6i cuffref-results/A5SS/line6i
	cd miso; run_miso.py --summarize-samples cuffref-results/A5SS/line7u cuffref-results/A5SS/line7u
	cd miso; run_miso.py --summarize-samples cuffref-results/A5SS/line7i cuffref-results/A5SS/line7i

run-miso-a3ss:

	#cd miso; qsub -v input_bam="bam-data/line6u.bam",index_dir="cuffref-index/A3SS",output_dir="cuffref-results/A3SS/line6u",event="A3SS" \
	#	~/miso-protocol/miso.sh
	cd miso; qsub -v input_bam="bam-data/line6i.bam",index_dir="cuffref-index/A3SS",output_dir="cuffref-results/A3SS/line6i",event="A3SS" \
		~/miso-protocol/miso.sh
	cd miso; qsub -v input_bam="bam-data/line7u.bam",index_dir="cuffref-index/A3SS",output_dir="cuffref-results/A3SS/line7u",event="A3SS" \
		~/miso-protocol/miso.sh
	cd miso; qsub -v input_bam="bam-data/line7i.bam",index_dir="cuffref-index/A3SS",output_dir="cuffref-results/A3SS/line7i",event="A3SS" \
		~/miso-protocol/miso.sh

run-miso-a5ss:

	cd miso; qsub -v input_bam="bam-data/line6u.bam",index_dir="cuffref-index/A5SS",output_dir="cuffref-results/A5SS/line6u",event="A5SS" \
		~/miso-protocol/miso.sh
	cd miso; qsub -v input_bam="bam-data/line6i.bam",index_dir="cuffref-index/A5SS",output_dir="cuffref-results/A5SS/line6i",event="A5SS" \
		~/miso-protocol/miso.sh
	cd miso; qsub -v input_bam="bam-data/line7u.bam",index_dir="cuffref-index/A5SS",output_dir="cuffref-results/A5SS/line7u",event="A5SS" \
		~/miso-protocol/miso.sh
	cd miso; qsub -v input_bam="bam-data/line7i.bam",index_dir="cuffref-index/A5SS",output_dir="cuffref-results/A5SS/line7i",event="A5SS" \
		~/miso-protocol/miso.sh

compare-miso-se:

	cd miso; run_miso.py --compare-samples cuffref-results/SE/line6u cuffref-results/SE/line7u cuffref-results/SE/comparisons
	cd miso; run_miso.py --compare-samples cuffref-results/SE/line6i cuffref-results/SE/line7i cuffref-results/SE/comparisons

filter-miso-se:

	cd miso; python ~/miso-protocol/miso-filter.py cuffref-results/SE/comparisons/line6u_vs_line7u/bayes-factors/line6u_vs_line7u.miso_bf SE 0.20 0.20 10 2 > cuffref-results/SE/comparisons/line6u_vs_line7u/bayes-factors/line6u_vs_line7u.miso_bf.flt
	cd miso; python ~/miso-protocol/miso-filter.py cuffref-results/SE/comparisons/line6i_vs_line7i/bayes-factors/line6i_vs_line7i.miso_bf SE 0.20 0.20 10 2 > cuffref-results/SE/comparisons/line6i_vs_line7i/bayes-factors/line6i_vs_line7i.miso_bf.flt
