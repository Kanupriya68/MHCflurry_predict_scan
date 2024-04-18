# MHCflurry_predict_scan
**This repository demonstrates how to run Predict Scan tool of MHCFlurry tool using this python script.**
> Conda Version 24.1.2 is used to create environment for this project

> [!IMPORTANT]
> Dependencies are listed in **mhcflurry-env-spec.yml**

### Steps to follow

1. Clone this repository to your local Python IDE
2. Deploy/Re-create mhcflurry-env by running this in your terminal : 
```console
conda env create -n mhcflurry-env-replica -f=mhcflurry-env-spec.yml
```
3. Run (This step is only required for the first time you are activating a conda environment)
```console
conda init
```
4. Then run this in terminal
```console
conda activate mhcflurry-env-replica
```
> [!IMPORTANT]
> Once the environment is activated, make sure to point at the correct Python interpreter. 
5. Call **'mhcflurry'** function with protein and allele strings in **'main.py'**
6.  Check the working directory for results in **output.csv**
7. To run the unit test run this from the terminal :
```console
python -m unittest test_main.py
```
> [!Note]
> Need to hash function call in main.py before running unit test to avoid parallel calls.
> Tests if output.csv has header columns and rows populated in it.

