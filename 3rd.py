import pandas as pd
import re

def extrct_code(filename):
    df = pd.read_csv(filename, header=None, names=["text"])
    codes = re.findall(r'\d+', ' '.join(df['text']))
    return list(map(int, codes))

def extract_numberatend(filename):
    df = pd.read_csv(filename, header=None, names=["text"])
    words_with_numbers = re.findall(r'\b\w+\d+\b', ' '.join(df['text']))
    return words_with_numbers

if __name__ == "__main__":
    filename = 'C:/PS1_A/Python/doc.txt' 
    
    codes = extrct_code(filename)
    print(codes)
    
    words_with_numbers = extract_numberatend(filename)
    print((words_with_numbers))
