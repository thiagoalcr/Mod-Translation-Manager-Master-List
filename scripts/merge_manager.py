import json
import os
import glob

BASE_DIR = os.getcwd() 
DB_FOLDER = os.path.join(BASE_DIR, "database")
SUBMISSIONS_FOLDER = os.path.join(BASE_DIR, "submissions")

def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def find_best_master_match(submission_filename, db_folder):
    """
    Estratégia 'Longest Prefix Match':
    Procura na pasta database qual arquivo mestre existente 'encaixa' melhor 
    no início do nome do arquivo submetido.
    """
    submission_clean = os.path.splitext(submission_filename)[0].lower()
    
    existing_masters = glob.glob(os.path.join(db_folder, "*.json"))
    
    candidates = []

    for master_path in existing_masters:
        master_filename = os.path.basename(master_path)
        master_stem = os.path.splitext(master_filename)[0].lower()

        if submission_clean.startswith(master_stem):
            remaining = submission_clean[len(master_stem):]
            
            if not remaining or remaining[0] in ['_', '-', ' ', '.', '(']:
                candidates.append(master_filename)
    
    if candidates:
        candidates.sort(key=len, reverse=True)
        return candidates[0] 

    parts = submission_filename.rsplit('_', 1)
    if len(parts) > 1:
        return parts[0] + ".json"
    
    return submission_filename

def merge_data():
    ensure_folder(DB_FOLDER)
    
    files = glob.glob(os.path.join(SUBMISSIONS_FOLDER, "*.json"))
    
    if not files:
        print(">> Nenhuma submissão nova encontrada.")
        return

    print(f">> Encontrados {len(files)} arquivos...")

    for submission_path in files:
        filename = os.path.basename(submission_path)
        if filename.startswith("."): continue
        
        print(f"Processando: {filename}")
        
        try:
            master_name = find_best_master_match(filename, DB_FOLDER)
            master_path = os.path.join(DB_FOLDER, master_name)

            if os.path.exists(master_path):
                print(f"   [MATCH] Mestre identificado: {master_name}")
            else:
                print(f"   [NOVO] Criando novo idioma: {master_name}")

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
            
            print(f"   -> SUCESSO! {initial_count} -> {final_count} mods.")

            with open(master_path, 'w', encoding='utf-8') as f:
                json.dump(master_data, f, indent=2, ensure_ascii=False)
            
            os.remove(submission_path)

        except Exception as e:
            print(f"   [ERRO] Falha em {filename}: {e}")

if __name__ == "__main__":
    merge_data()
