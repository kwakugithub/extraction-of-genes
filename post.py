import requests, sys
 
server = "https://rest.ensembl.org"
ext = "/lookup/symbol/homo_sapiens"
headers={ "Content-Type" : "application/json", "Accept" : "application/json"}
r = requests.post(server+ext, headers=headers, data='{ "symbols" : ["BRCA2", "BRAF" ] }')
 
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
import requests, sys
 
server = "https://rest.ensembl.org"
ext = "/lookup/symbol/homo_sapiens"
headers={ "Content-Type" : "application/json", "Accept" : "application/json"}
r = requests.post(server+ext, headers=headers, data='{ "symbols" : ["BRCA2", "BRAF","MFAP5" ] }')
 
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
print(repr(decoded))
    


def lookup(genes):
    if genes in decoded:
        gene_info = decoded[genes]
        seq_region_name = gene_info["seq_region_name"]
        start= gene_info["start"]
        end = gene_info["end"]
        return seq_region_name,start,end
    else:
        return None
 
gene_names = ["BRCA2", "BRAF","MFAP5"]    
gene_names_list = []
results = lookup("genes")
print(results)

for genes in gene_names:
    results = lookup(genes)
    if results is not None:
        seq_region_name,start,end = results
        gene_names_list.append({"genes":genes, "seq_region_name": seq_region_name, "start":start,"end":end })
    else:
        print(f"lookup {genes} not found")    
for gene_info in gene_names_list:
    print(f"Gene: {gene_info['genes']}, seq_region_name: {gene_info['seq_region_name']}, Start: {gene_info['start']}, End: {gene_info['end']}")

    






       




  
  


# [
#   ['BRCA2', seq_region_name, start, end],
#   ['BRAF', seq_region_name, start, end],
#   ['MFAP5', seq_region_name, start, end]
# ]