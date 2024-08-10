def read_file(path:str)->list:
    # fileを読み込む
    with open(path, "r",encoding="utf-8") as f:
        return f.read().strip().split("\n")
    
def read_dictionary(path:str)->dict:
    with open(path,"r",encoding="utf-8") as f:
        return {line.split(",")[0].strip():line.split(",")[1].strip() for line in f.readlines()}

def write_file(path:str,materials:dict):
    # materials.txtに材質名を書き込む
    with open(path,"w",encoding="utf-8") as f:
        f.write('\n'.join(materials.keys()))
        print(f"{path}への書き込みが完了しました。")

def write_dictionary(path:str,materials:dict):
    with open(path,"a+",encoding="utf-8") as f:
        f.write("\n".join([f"{k}, {v}" for k,v in materials.items()]))
        print(f"{path}への書き込みが完了しました。")
