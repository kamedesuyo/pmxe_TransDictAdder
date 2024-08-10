from TransDictAdder.model_loader.load_models import load_materials_dict
from TransDictAdder.utils.file_operations import write_file, read_file,write_dictionary,read_dictionary
from TransDictAdder.validation.material_valid import verify_materials, verify_dict_path

materials_path = "materials.txt"
trans_result_path = "trans_result.txt"
dictionary_path = "dictionary.txt"
dict_path = "dict_path.txt"

def main():
    try:
        global dictionary_path
        dictionary_path = verify_dict_path(dict_path, dictionary_path)
        # 辞書の先読み
        dictionary_data = read_dictionary(dictionary_path)
        # pmxの読み込みと書き込み
        materials = load_materials_dict(dictionary_data)
        if not materials:
            print("追加する材質名が見つかりませんでした。\n全て登録済み、またはmodelsフォルダが存在していない可能性があります。")
            return
        print(f"\n読み込んだ材質名:{len(materials)}個\n{", ".join(materials.keys())}")
        write_file(materials_path,materials)
        # 翻訳結果の入力
        while True:
            trans_materials = read_file(trans_result_path)
            input("materials.txtの翻訳結果をtrans_result.txtに入力し、Enterを押してください。(Ctrl+Cで中断)")
            if verify_materials(materials,trans_materials):
                break
        # 辞書への書き込み
        write_dictionary(dictionary_path,dict(zip(materials,trans_materials)))
        input("全ての処理が完了しました。Enterを押して終了...")

    except KeyboardInterrupt: 
        print("\n処理を中断しました。")
    
    except Exception as e:
        print(f"\nエラーが発生しました。{e}")
if __name__ == "__main__":
    main()