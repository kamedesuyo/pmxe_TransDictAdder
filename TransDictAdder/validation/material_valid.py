def verify_materials(materials,trans_materials)->bool:
    if len(materials) != len(trans_materials):
        print("材質名の数が一致しません。")
        return False
    return True

def verify_load_materials(materials:dict):
    if not materials or len(materials) == 0:
        print("追加する材質名が見つかりませんでした。")
        return