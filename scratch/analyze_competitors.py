import os
import json

def get_insights(file_path, comp_name):
    print(f"=== {comp_name} ===")
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        if line.startswith('[h1]') or line.startswith('[h2]') or line.startswith('[h3]'):
            print(line.strip())
            
    print("\n")

get_insights('scratch/competitor1.txt', 'Yuvrit Knee Pain')
get_insights('scratch/competitor2.txt', 'ResearchAyu Knee Pain')
