def verify_materials(materials:dict,trans_materials:list)->bool:
    if len(materials) != len(trans_materials):
        print("材質名の数が一致しません。")
    elif list(materials.keys()) == trans_materials:
        print("材質名と翻訳結果が同じです。")
    else:
        return True
    return False