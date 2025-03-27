import pandas as pd
import os

def transform(data, csv_path):
    if not data or not data[0]:
        print("Erro: Nenhum dado válido extraído do PDF.")
        return
    
    df = pd.DataFrame(data[1:], columns=data[0])
    df.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial'}, inplace=True)

    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    df.to_csv(csv_path, index=False, encoding='utf-8', sep=",")
    print(f"CSV salvo em: {csv_path}")