Trouble shooting
================

* __tagBam__ included in MISO package does not work. __tagBam__ has to be from the latest version of BEDtools.
* __BAM files__ needed to be __indexed__ prior to running MISO to calculate expression.
* SciPy and NumPy have to be available. For PBS system, you may have to add command that load these modules as described below.
* To add code to a job script created by MISO, insert code to make_batch_script function in __cluster_utils.py__ in __misopy__ module.
