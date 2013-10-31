Trouble shooting
================

* __tagBam__ included in MISO package does not work. __tagBam__ has to be from the latest version of BEDtools.
* BAM needed to be indexed prior to running MISO to calculate expression.
* SciPy and NumPy have to be available. For PBS system, you may have to add paths of those modules to .bash_profile to be loaded when a job is run by MISO.
