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
            
            df_temp['filename'] = file_name
            
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            elif 'italian' in file_name.lower():
                df_temp['location'] = 'it'
               
            # criar uma nova coluna chamada campaign
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')   
            
            # guarda dados tratados dentro de um dataframe comum
            dfs.append(df_temp)
            
        except Exception as e:
            print(f'Erro ao ler o arquivo`{excel_file} : {e}')

if dfs:
    
    # concatena todas as tabelas salvas no dfs em uma única tabela
    result = pd.concat(dfs, ignore_index=True)
    
    # caminho de saída
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')
    
    # configurar motor de escrita
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    
    # leva os dados do resultado a serem escritos no motor de excel configurado
    result.to_excel(writer, index=False)
    
    # salva o arquivo de excel
    writer._save()
else:
    print('Nenhum dado para ser salvo.')