import pandas as pd
import os
import glob

# caminho para ler os arquivos
folder_path = 'src\\data\\raw'

# listar todos os arquivos do excel
excel_files = glob.glob(os.path.join(folder_path,'*.xlsx'))

if not excel_files:
    print('Nenhum arquivo compátivel encontrado')
else:
    
    dfs = []
    
    for excel_file in excel_files:
        
        try:
            # ler o arquivo do excel
            df_temp = pd.read_excel(excel_file) 
            
            # pegar o nome do arquivo
            file_name = os.path.basename(excel_file)
            
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            elif 'italian' in file_name.lower():
                df_temp['location'] = 'it'
               
            # criar uma nova coluna chamada campaign
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')   
            
            print(df_temp)
            
        except Exception as e:
            print(f'Erro ao ler o arquivo`{excel_file} : {e}')
