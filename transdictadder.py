from TransDictAdder.model_loader.load_models import load_materials_dict
from TransDictAdder.utils.file_operations import write_file, read_file, write_dictionary, read_dictionary
from TransDictAdder.validation.material_valid import verify_materials, verify_dict_path
from TransDictAdder.model_renamer.model_rename import model_rename

materials_path = "materials.txt"
trans_result_path = "trans_result.txt"
dictionary_path = "dictionary.txt"
dict_path = "dict_path.txt"


def process_materials():
    """
    dictionary.txtから材質名を読み込み、未登録の材質名をmaterials.txtに書き込む。
    その後、materials.txtの翻訳結果をtrans_result.txtに入力する。
    """
    global dictionary_path
    dictionary_path = verify_dict_path(dict_path, dictionary_path)
    dictionary_data = read_dictionary(dictionary_path)
    materials = load_materials_dict(dictionary_data)
    
    if not materials:
        print("追加する材質名が見つかりませんでした。\n全て登録済み、またはmodelsフォルダが存在していない可能性があります。")
        check_do_rename(materials, dictionary_data)
        input("Enterで終了...")
        return None, None

    print(f"\n読み込んだ材質名:{len(materials)}個\n{', '.join(materials.keys())}")
    write_file(materials_path, materials)
    return materials, dictionary_data

def process_translations(materials):
    """
    materials.txtの翻訳結果をtrans_result.txtに入力し、materialsと翻訳結果を辞書にして返す。
    """
    while True:
        input("materials.txtの翻訳結果をtrans_result.txtに入力し、Enterを押してください。(Ctrl+Cで中断)")
        trans_materials = read_file(trans_result_path)
        if verify_materials(materials, trans_materials):
            return dict(zip(materials, trans_materials))

def check_do_rename(materials: dict, dictionary_data: dict):
    """
    モデルのリネームを行うか確認する。
    """
    while True:
        do_model_rename = input("リネーム済みモデルを生成しますか？(y/n):").lower()
        if do_model_rename in {"y", "n"}:
            if do_model_rename == "y":
                model_rename(materials | dictionary_data)
            break

def main():
    try:
        materials, dictionary_data = process_materials()
        if materials is None:
            return
        materials_dict = process_translations(materials)
        # renameの確認
        check_do_rename(materials_dict, dictionary_data)
        # 辞書への書き込み
        write_dictionary(dictionary_path, materials_dict)
        input("全ての処理が完了しました。Enterを押して終了...")

    except KeyboardInterrupt:
        input("\n処理を中断しました。")

if __name__ == "__main__":
    main()
