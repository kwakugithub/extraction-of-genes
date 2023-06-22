import requests, sys
 
server = "https://rest.ensembl.org"
ext = "/lookup/symbol/homo_sapiens/BRCA2?expand=1"

print(server+ext)

r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
print(r)
if not r.ok:
    r.raise_for_status()
    sys.exit()
 
decoded = r.json()
print(repr(decoded))


def lookup(symbol):
    server = "https://rest.ensembl.org"  
    ext = f"/lookup/symbol/homo_sapiens/{symbol}?expand=1"
    http = server + ext
    headers = {"Content-Type" : "application/json"}
    r = requests.get(http,headers=headers)
    return r
results = lookup("BRCA2")
print(results)




import requests, sys
 
server = "https://rest.ensembl.org"
ext = "/lookup/symbol/homo_sapiens"
headers={ "Content-Type" : "application/json", "Accept" : "application/json"}
r = requests.post(server+ext, headers=headers, data='{ "symbols" : ["BRCA2", "BRAF" ] }')
 
if not r.ok:
   r.raise_for_status()
   sys.exit()
 
decoded = r.json()
print(repr(decoded))
   

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

def extract_position(results):
    decoded = results.json()
    print(decoded)
    seq_region_name = decoded["seq_region_name"]
    start = decoded["start"]
    end = decoded["end"]
    return seq_region_name,start,end
position = extract_position(results)
print(position)