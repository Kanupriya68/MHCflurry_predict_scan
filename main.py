import subprocess
import csv
import re

rows = []
def mhcflurry(protein:str,allele:str) -> None:
    if not re.match("^HLA-[A-Z]\*\d{2}:\d{2,3}$", allele):
        raise ValueError(
            "Allele name has to have the form of XXX-X*00:00")
    elif not re.match("^[ACDEFGHIKLMNPQRSTVWY]+$", protein):
        raise ValueError(
            "Incorrect protein sequence/Not a protein sequence")
    else:
        subprocess.check_output(["mhcflurry-predict-scan", "--sequences", protein
                                    , "--alleles", allele, "--out", "output.csv"])
        with open("output.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
        return [header,rows]

#Example code to call the function (Hashed to avoid issues with unit testing)
# result = mhcflurry('MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSV','HLA-A*02:01')
# print(result)

