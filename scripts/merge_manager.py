import json
import os
import glob

BASE_DIR = os.getcwd() 
DB_FOLDER = os.path.join(BASE_DIR, "database")
SUBMISSIONS_FOLDER = os.path.join(BASE_DIR, "submissions")

def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def merge_data():
    ensure_folder(DB_FOLDER)
    
    files = glob.glob(os.path.join(SUBMISSIONS_FOLDER, "*.json"))
    
    if not files:
        print(">> Nenhuma submissão nova encontrada na Inbox.")
        return

    print(f">> Encontrados {len(files)} arquivos para processar...")

    for submission_path in files:
        filename = os.path.basename(submission_path)
        
        if filename.startswith("."): continue
        
        print(f"Processando: {filename}")
        
        try:           
            parts = filename.rsplit('_', 1)
            
            if len(parts) > 1:
                master_name = parts[0] + ".json"
            else:
                master_name = filename

            master_path = os.path.join(DB_FOLDER, master_name)
            
            if not os.path.exists(master_path):
                print(f"   [AVISO] Arquivo mestre '{master_name}' não existe. Será criado um novo.")
            else:
                print(f"   [OK] Mesclando com mestre existente: {master_name}")

            # ------------------------------------

            with open(submission_path, 'r', encoding='utf-8') as f:
                sub_data = json.load(f)
            
            sub_entries = sub_data.get('entries', {})
            if not sub_entries:
                print("   [!] Arquivo vazio. Deletando.")
                os.remove(submission_path)
                continue

            master_data = {"meta": {"version": 2}, "entries": {}}
            if os.path.exists(master_path):
                with open(master_path, 'r', encoding='utf-8') as f:
                    master_data = json.load(f)
            
            initial_count = len(master_data['entries'])
            master_data['entries'].update(sub_entries)
            final_count = len(master_data['entries'])
            
            print(f"   -> SUCESSO! Master foi de {initial_count} para {final_count} mods.")

            with open(master_path, 'w', encoding='utf-8') as f:
                json.dump(master_data, f, indent=2, ensure_ascii=False)
            
            os.remove(submission_path)
            print("   -> Arquivo de submissão deletado.")

        except Exception as e:
            print(f"   [ERRO CRÍTICO] Falha ao processar {filename}: {e}")

if __name__ == "__main__":
    merge_data()
