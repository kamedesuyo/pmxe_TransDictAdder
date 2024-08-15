def read_file(path:str)->list:
    try:
        with open(path, "r",encoding="utf-8") as f:
            return f.read().replace(" ","").split("\n")
    except FileNotFoundError:
        open(path,"w",encoding="utf-8").close()
        return []
    
def read_dictionary(path:str)->dict:
    try:
        with open(path,"r",encoding="utf-8") as f:
            return {line.split(",")[0].strip():line.split(",")[1].strip() for line in f.readlines()}
    except FileNotFoundError:
        return {}

def write_file(path:str,materials:dict):
    with open(path,"w",encoding="utf-8") as f:
        f.write('\n'.join(materials.keys()))
        print(f"書き込みが完了しました。\n   {path}")

def write_dictionary(path:str,materials:dict):
    with open(path,"a+",encoding="utf-8") as f:
        f.write("\n".join([f"{k}, {v}" for k,v in materials.items()]))
        f.write("\n")
        print(f"書き込みが完了しました。\n   書き込み先:{path}")