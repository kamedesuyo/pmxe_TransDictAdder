def verify_materials(materials,trans_materials)->bool:
    if len(materials) != len(trans_materials):
        print("材質名の数が一致しません。")
        return False
    return True