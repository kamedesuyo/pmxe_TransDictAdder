def verify_materials(materials:dict,trans_materials:list)->bool:
    if len(materials) != len(trans_materials):
        print("材質名の数が一致しません。")
    elif list(materials.keys()) == trans_materials:
        print("材質名と翻訳結果が同じです。")
    else:
        return True
    return False

def exist_dict_path(dict_path:str)->str:
    try:
        with open(dict_path,"r",encoding="utf-8") as f:
            return f.readline().strip().replace("\"","")
    except FileNotFoundError:
        open(dict_path,"w",encoding="utf-8").close()
        return None

def verify_dict_path(dict_path:str,dictionary_path:str)->str:
    # path = dictionary.txtのパス
    path = exist_dict_path(dict_path)
    if path:
        try:
            open(path,"r",encoding="utf-8").close()
            print(f"指定された辞書ファイルを使用します。\n   {path}")
            return path
        except FileNotFoundError:
            print(f"指定された辞書ファイルが存在しません。{path}")
            print(f"デフォルトの辞書ファイルを使用します。{dictionary_path}")
    return dictionary_path