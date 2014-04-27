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

	#cd miso; run_miso.py --summarize-samples results/SE/line6u results/SE/line6u
	cd miso; run_miso.py --summarize-samples results/SE/line6i results/SE/line6i
	cd miso; run_miso.py --summarize-samples results/SE/line7u results/SE/line7u
	cd miso; run_miso.py --summarize-samples results/SE/line7i results/SE/line7i
