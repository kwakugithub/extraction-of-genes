import requests
import sys
import pandas as pd


def lookup(genes):
    server = "https://rest.genenames.org/"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    ext = f"/fetch/symbol/{genes}"
    http = server + ext

    r = requests.get(http, headers=headers)
    return r


def extract_ids(response):# the extract function pass
    response = response["response"]
    docs = response["docs"]
    gene_info = docs[0]

    keys = [
        'hgnc_id', 'ena', 'entrez_id', 'mgd_id', 'refseq_accession',
        'vega_id', 'ensembl_gene_id', 'ccds_id', 'omim_id',
        'uniprot_ids', 'ucsc_id', 'rgd_id', 'agr', 'mane_select'
    ]
    ids = {}

    for key in keys:
        if key in gene_info:
            ids[key] = gene_info[key]
        else:
            ids[key] = None

    return ids


gene_list = ["ALDH3A1","CRABP1","EREG","FKBP10","GSTM1","LTBP2","LXN","MRC2","MSLN", "NOV","P4HA1", "QPCT", "SEMA7A", "TNC"]
all_rows = []  # Store all rows for both genes

for gene in gene_list:
    results = lookup(gene)
    if not results.ok:
        results.raise_for_status()
        sys.exit()
    decoded = results.json()
    extracted_ids = extract_ids(decoded)

    rows = []
    for key, value in extracted_ids.items():
        if isinstance(value, list):
            for element in value:
                rows.append([key, element])
        else:
            rows.append([key, value])

    print(rows)  # Print rows for the current gene
    all_rows.extend(rows)  # Add current gene's rows to the all_rows list

    keys = {
        'hgnc_id': 'HGNC',
        'ena': 'ENA',
        'entrez_id': 'Entrez_id',
        'mgd_id': 'MGD',
        'refseq_accession': 'RefSeq',
        'vega_id': 'Vega',
        'ensembl_gene_id': 'Ensembl',
        'ccds_id': 'CCDS',
        'omim_id': 'OMIM',
        'uniprot_ids': 'UniProt',
        'ucsc_id': 'UCSC',
        'rgd_id': 'RGD',
        'agr': 'AGR',
        'mane_select': 'MANE'
    }


    df = pd.DataFrame(rows, columns=["Type", "ID"])
    df["Type"] = df["Type"].replace(keys)
    print(df)
   

    filename = f"geneticsds_{gene}.csv"  # Use a different filename for each gene
    df.to_csv(filename, index=False)
  
    print("Data saved:", filename)

# Create a dataframe containing all rows for both genes
all_df = pd.DataFrame(all_rows, columns=["Genes", "identifier"])


# all_filename = "geneticsds_all.csv"  # Use a different filename for combined data
# all_df.to_csv(all_filename, index=False)
# print("Combined data saved:", all_filename)

    




    






       




  
  

