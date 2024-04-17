# MHCflurry_predict_scan
**This repository demonstrates how to run Predict Scan tool of MHCFlurry tool using this python script.**

> [!IMPORTANT]
> Dependencies are listed in **mhcflurry-env-spec.yml**

### Steps to follow

1. Clone this repository to your local Python IDE
2. Deploy/Re-create mhcflurry-env by running this in your terminal : 
```console
conda env create -n mhcflurry-env-replica -f=mhcflurry-env-spec.yml
```
3. Run
```console
conda init
```
4. Then run this in terminal
```console
conda activate mhcflurry-env-replica
```
4. Call **'mhcflurry'** function with protein and allele strings in **'main.py'**
5.  Check working directory for results in **output.csv**
6. To run unit test run this from terminal :
```console
python -m unittest test_main.py
```

