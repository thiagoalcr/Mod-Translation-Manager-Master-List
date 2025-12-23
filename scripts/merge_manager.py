import json
import os
import glob
import re

# Configuração das Pastas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FOLDER = os.path.join(BASE_DIR, "database")
SUBMISSIONS_FOLDER = os.path.join(BASE_DIR, "submissions")

def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def merge_data():
    ensure_folder(DB_FOLDER)
    
    # 1. Pega todos os JSONs na pasta submissions
    files = glob.glob(os.path.join(SUBMISSIONS_FOLDER, "*.json"))
    
    if not files:
        print(">> Nenhuma submissão nova encontrada na Inbox.")
        return

    print(f">> Encontrados {len(files)} arquivos para processar...")

    for submission_path in files:
        filename = os.path.basename(submission_path)
        
        # Pular arquivos de sistema
        if filename.startswith("."): continue
        
        print(f"Processando: {filename}")
        
        try:
            # 2. Descobrir quem é o "Pai" (Master) desse arquivo
            # O App gera: {game}_{lang}_{suffix}.json
            # Precisamos remover o _{suffix} final para achar o nome do Master.
            
            # Regex: Pega tudo até o último underline seguido de alphanumérico e .json
            # Ex: skyrim_pt_br_123a.json -> skyrim_pt_br
            match = re.match(r"(.+)_[a-f0-9]+\.json$", filename)
            
            if match:
                master_name = match.group(1) + ".json"
            else:
                print(f"   [!] Nome de arquivo inválido/antigo: {filename}. Ignorando suffix.")
                master_name = filename # Tenta usar direto se falhar

            master_path = os.path.join(DB_FOLDER, master_name)
            
            # 3. Ler a Submissão
            with open(submission_path, 'r', encoding='utf-8') as f:
                sub_data = json.load(f)
            
            sub_entries = sub_data.get('entries', {})
            if not sub_entries:
                print("   [!] Arquivo vazio ou inválido. Deletando.")
                os.remove(submission_path)
                continue

            # 4. Ler (ou Criar) o Master
            master_data = {"meta": {"version": 2}, "entries": {}}
            if os.path.exists(master_path):
                with open(master_path, 'r', encoding='utf-8') as f:
                    master_data = json.load(f)
            
            # 5. MERGE (A mágica acontece aqui)
            # Atualiza o dicionário Master com as entradas novas.
            # Se a chave já existir, a submissão nova SOBRESCREVE a antiga (atualização).
            initial_count = len(master_data['entries'])
            master_data['entries'].update(sub_entries)
            final_count = len(master_data['entries'])
            
            print(f"   -> Merged! Master foi de {initial_count} para {final_count} mods.")

            # 6. Salvar Master
            with open(master_path, 'w', encoding='utf-8') as f:
                json.dump(master_data, f, indent=2, ensure_ascii=False)
            
            # 7. Limpar a Inbox (Deletar a submissão)
            os.remove(submission_path)
            print("   -> Arquivo de submissão deletado.")

        except Exception as e:
            print(f"   [ERRO] Falha ao processar {filename}: {e}")

if __name__ == "__main__":
    merge_data()
