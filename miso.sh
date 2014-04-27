#!/bin/sh -login
#PBS -l nodes=4:ppn=4,mem=24gb,walltime=24:00:00
#PBS -m abe
#PBS -N Miso_${PBS_JOBID}
#PBS -A ged-intel11

#source ~/.bash_profile
module load SciPy/0.13.0
module load NumPy/1.8.0
module load BEDTools/2.17.0

cd ${PBS_O_WORKDIR}

run_events_analysis.py --compute-genes-psi ${index_dir} ${input_bam} --output-dir ${output_dir} --read-len 75 --settings-filename=~/miso-protocol/miso_settings.txt --use-cluster --event-type ${event} --chunk-jobs 100
