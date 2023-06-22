
import requests, sys



   

def lookup(genes):
    server = "https://rest.ensembl.org"
    ext = f"/lookup/symbol/homo_sapiens"
    http = server + ext
    headers={"Content-Type": "application/json", "Accept": "application/json"}
    data = {"symbols" : genes}
   
    r = requests.post(http, headers=headers, json=data)
    return r



results = lookup(["BRCA2", "BRAF", "MFAP5"])
print(results)

if not results.ok:
    results.raise_for_status()
    sys.exit() 

decoded = results.json() 
 

def extract_position(decoded):
    seq_region_name = decoded["seq_region_name"]
    start = decoded["start"]
    end = decoded["end"]
    return seq_region_name,start,end






# for key, value in decoded.items():
#     print(f" {key} \n  {value}")

for x, inner in decoded.items():
    position = extract_position(inner)
    # print(len(x)) 
    # print(len(inner.keys()))
    # print(inner.keys())
    # print(f"Gene: {gene}")
    print(x)
    print("Position: ", position) 
    print("Seq Region Name: ", position[0])
    print("Start: ", position[1])
    print("End:", position[2])
    
# gene_names = position

# for seq_region_name, start, end in position:
#     print(f"Seq Region Name: {seq_region_name}")
#     print(f"Start: {start}")
#     print(f"End: {end}")

    
   
    

 





    
    
           
# [
#   ['BRCA2', seq_region_name, start, end],
#   ['BRAF', seq_region_name, start, end],
#   ['MFAP5', seq_region_name, start, end]
# ]
