import re
import os
import pandas as pd

articles_folder = "../articles"

canonical_names={}
gaz_path = "../gazetteers/geonames_gaza_selection.tsv"
with open(gaz_path,'r', encoding='utf-8') as file:
    data = file.read()

rows = data.strip().split('\n')
for row in rows[1:]:
    columns = row.split('\t')
    
    asciiname = columns[0].strip()
    canonical_name=asciiname.lower()
    
    name = columns [4].strip().lower()
    
    alternatenames = columns[5]
    alternatenames_list=[alt.strip().lower() for alt in alternatenames.split(',') if alt.strip()]

    canonical_names[canonical_name]=[canonical_name, name]+alternatenames_list
    

mentions_per_month={}

for filename in os.listdir(articles_folder):
    date=filename[:10]
    
    if date>='2023-10-07':
        month=filename[:7]
        
        file_path=os.path.join(articles_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text=file.read()
            
            for canonical_name, variants in canonical_names.items():
                regex = r'\b(' + '|'.join(map(re.escape, variants)) + r')\b'
                matches=re.findall(regex, text, flags=re.IGNORECASE)
                count=len(matches)
                if count>0:
                    if canonical_name not in mentions_per_month:
                        mentions_per_month[canonical_name]={}
                    mentions_per_month[canonical_name][month]= (mentions_per_month[canonical_name].get(month, 0)+ count)

for place, months in mentions_per_month.items():
    print (f"{place}:")
    for month, count in months.items():
        print(f"{month}:{count}")

rows=[]
for place, months in mentions_per_month.items():
    for month, count in months.items():
        rows.append((place, month, count))

def write_tsv(rows, column_list, path):
    df = pd.DataFrame.from_records(rows, columns=column_list)
    df.to_csv(path, sep="\t", index=False)

columns = ["placename", "month", "count"]
tsv_filename = "2A_aamna.tsv"
write_tsv(rows, columns, tsv_filename)
