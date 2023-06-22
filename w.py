import csv
import requests
import sys


def lookup(genes):
    server = "https://rest.ensembl.org"
    ext = "/lookup/symbol/homo_sapiens"
    http = server + ext
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = {"symbols": genes}

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
    return seq_region_name, start, end

output_file = "position_output.csv"

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Gene", "Seq Region Name", "Start", "End"])

    for gene, info in decoded.items():
        position = extract_position(info)
        writer.writerow([gene, position[0], position[1], position[2]])

print(f"Results saved to {output_file}.")     