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


results = lookup("ZNF3")
print(results)

if not results.ok:
     results.raise_for_status()
     sys.exit()

decoded = results.json()
# print(decoded)



def extract_ids(response):
    response = response["response"]
    docs = response["docs"]
    gene_info = docs[0]

    keys = ['hgnc_id', 'ena', 'entrez_id', 'mgd_id', 'refseq_accession', 'vega_id', 'ensembl_gene_id', 'ccds_id', 'omim_id', 'uniprot_ids', 'ucsc_id', 'rgd_id', 'agr', 'mane_select']
    ids = {}

    for key in keys:
        if key in gene_info:
            ids[key] = gene_info[key]
        else:
            ids[key] = None

    return ids

extracted_ids = extract_ids(decoded)
# print(extracted_ids)




# df = pd.DataFrame(extracted_ids.items() , columns = ["Type","ID"])

# # extracted_ids = {'Type': ['hgnc_id', 'ena', 'entrez_id', 'mgd_id', 'refseq_accession', 'vega_id', 'ensembl_gene_id', 'ccds_id', 'omim_id', 'uniprot_ids', 'ucsc_id', 'rgd_id', 'agr','mane_select','mane_select'],
# # 'ID': [['HGNC:13089'], ['AF027136'], ['7551'], ['MGI:1929116'], ['NM_017715'], ['OTTHUMG00000154596'], ['ENSG00000166526'], ['CCDS94152', 'CCDS43619', 'CCDS43618'], ['194510'], ['P17036'], ['uc031syk.2'], ['RGD:6489147'], ['HGNC:13089'],['ENST00000299667.9'],['MM_032924.5']]}
# # df = pd.DataFrame(extracted_ids)
# df['ID'] = df['ID'].apply(lambda x: x[0] if isinstance(x, list) else x)


# print(df)
                  
# Kwaku ver
# rows = []
# for key,value in extracted_ids.items():
#     if isinstance(value,list):
#         for element in value:
#             rows.append({'Type':key, 'ID':element})
#     else:
#         rows.append({'Type': key, 'ID': value})

# YC ver
rows = list()
for key, value in extracted_ids.items():
    if isinstance(value, list):
        for element in value:
            rows.append([key, element])
    else:
        rows.append([key, value])      
print(rows)

df = pd.DataFrame(rows)
print(df)


    

    

# for key,value in decoded.items():
    #  print(f"{key}\n {value}")




# {'hgnc_id': 'HGNC:13089', 'ena': ['AF027136'], 'entrez_id': '7551', 'mgd_id': ['MGI:1929116'], 'refseq_accession': ['NM_017715'], 'vega_id': 'OTTHUMG00000154596', 
# 'ensembl_gene_id': 'ENSG00000166526', 'ccds_id': ['CCDS94152', 'CCDS43619', 'CCDS43618'], 'omim_id': ['194510'], 'uniprot_ids': ['P17036'], 'ucsc_id': 'uc031syk.2', 'rgd_id': ['RGD:6489147'], 'agr': 'HGNC:13089', 'mane_select': ['ENST00000299667.9', 'NM_032924.5']}
              

        
  

