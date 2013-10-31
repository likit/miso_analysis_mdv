#!/bin/sh -login
#PBS -l nodes=4:ppn=4,mem=24gb,walltime=24:00:00
#PBS -m abe
#PBS -N line6i_paired_end_MISO
#PBS -A ged-intel11

source ~/.bash_profile
module load BEDTools
module load SciPy
module load NumPy

cd /mnt/ls12/preeyanon/miso_pe

run_events_analysis.py --compute-genes-psi indexes/SE line6i_tophat/accepted_hits.bam --output-dir results/SE/line6i --read-len 75 --paired-end 171.9 46.5 --settings-filename=miso_settings.txt --use-cluster --event-type SE --chunk-jobs 100

#for testing without using a cluster
#run_events_analysis.py --compute-genes-psi indexes/SE line6i_tophat/accepted_hits.bam --output-dir results/SE/line6i --read-len 75 --paired-end 171.9 46.5 --settings-filename=~/miso_settings.txt --event-type SE
