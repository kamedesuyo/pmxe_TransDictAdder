from TransDictAdder.model_loader.load_models import load_materials_dict
from TransDictAdder.utils.file_operations import write_file, read_file,write_dictionary,read_dictionary
from TransDictAdder.validation.material_valid import verify_materials, verify_dict_path
from TransDictAdder.model_renamer.model_rename import model_rename

materials_path = "materials.txt"
trans_result_path = "trans_result.txt"
dictionary_path = "dictionary.txt"
dict_path = "dict_path.txt"

def main():
    try:
        # dict_path内のパスを読み込む
        global dictionary_path
        dictionary_path = verify_dict_path(dict_path, dictionary_path)
        # 辞書の先読み
        dictionary_data = read_dictionary(dictionary_path)
        # pmxの読み込みと書き込み
        materials = load_materials_dict(dictionary_data)
        if not materials:
            input("追加する材質名が見つかりませんでした。\n全て登録済み、またはmodelsフォルダが存在していない可能性があります。")
            return
        print(f"\n読み込んだ材質名:{len(materials)}個\n{", ".join(materials.keys())}")
        write_file(materials_path,materials)
        # 翻訳結果の入力
        while True:
            input("materials.txtの翻訳結果をtrans_result.txtに入力し、Enterを押してください。(Ctrl+Cで中断)")
            trans_materials = read_file(trans_result_path)
            if verify_materials(materials,trans_materials):
                break
        materials_dict = dict(zip(materials,trans_materials))
        #model情報取得 → material読み込み → material_dictからrename → pmx更新
        while True:
            do_model_rename = input("リネーム済みモデルを生成しますか？(y/n):").lower()
            if do_model_rename == "y" or do_model_rename == "n":
                model_rename(materials_dict)
                break

        # 辞書への書き込み
        write_dictionary(dictionary_path,materials_dict)
        input("全ての処理が完了しました。Enterを押して終了...")

    except KeyboardInterrupt: 
        input("\n処理を中断しました。")
if __name__ == "__main__":
    main()