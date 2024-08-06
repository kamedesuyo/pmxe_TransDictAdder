import pymeshio.pmx.reader as pmxreader
import glob
import os

material_list_path = "material_list.txt"
material_trans_list_path = "material_trans_list.txt"
dictionary_path = "dictionary.txt"

file_list = glob.glob(os.path.join("pmx", "*.pmx"))

dictionary_data = {}
material_list = []
material_trans_list = []
error_list = []

def get_material_list():
    for file in file_list:
        file.replace('\\', '/')
        try:
            pmx = pmxreader.read_from_file(file)
            for material in pmx.materials:
                material_list.append(material.name)
        except Exception as e:
            error_list.append(f"{file}の読み込みに失敗しました。")

def get_material_trans_list():
    global material_trans_list
    while(1):
        try:    
            input("material_trans_list.txtに翻訳結果を入力後、enterキーを押してください。(終了:Ctrl+C)")
            with open(material_trans_list_path, 'r', encoding="utf-8") as f:
                material_trans_list = f.read().replace(" ", "").split("\n")
                # 空の行を削除
                for trans in material_trans_list:
                    if trans == "":
                        trans.delete()
        # 翻訳結果が空の場合、行数チェ  ック、keyboardInterruptの場合は終了
            if not material_trans_list:
                print("翻訳結果が空です。")
            elif len(material_list) != len(material_trans_list):
                print("マテリアル名と翻訳結果の行数が一致しません。")
            else:
                return material_trans_list
        except KeyboardInterrupt:
            print("\n終了しています...")
            exit(-1)

def get_dictionary_data():
    global dictionary_data
    with open(dictionary_path, "r", encoding="utf-8") as f:
        dictionary_list = f.read().replace(" ", "").split("\n")
        for i in range(len(dictionary_list)-1):
            try:
                k = dictionary_list[i].split(",")[0]
                v = dictionary_list[i].split(",")[1]
            except Exception as e:
                print(e)
            dictionary_data[k] = v

def write_material_names() -> None:
    with open(material_list_path, 'w',encoding="utf-8") as f:    
        for material in material_list:
            try:
                f.write(f"{material}\n")
            except Exception as e:
                error_list.append(f"ファイル書き込み中にエラーが発生しました:{e}")

def show_load_error():
    for error in error_list:
        print(error)

def main():
    # 流れ: pmxファイルからマテリアル名取得 -> 翻訳結果取得 -> 辞書作成 -> dictionary.txtを読み込んで辞書化 -> 辞書アップデート -> dictionary.txtに書き込む
    # ※辞書内に存在すれば、翻訳結果を追加しない
    global material_list
    global material_trans_list
    global dictionary_data

    # マテリアル名取得、書き出し処理
    get_material_list()
    material_list = sorted(list(set(material_list)))
    write_material_names()
    print(f"マテリアル名取得処理が完了しました。:\n{material_list}\n")
    show_load_error()

    # 翻訳結果取得、辞書作成
    get_material_trans_list()
    trans_dict = {}
    for k, n in zip(material_list, material_trans_list):
        trans_dict[k] = n 
    # 元の辞書データを取得、辞書化してアップデート
    get_dictionary_data()
    trans_dict.update(dictionary_data)
    
    with open(dictionary_path, 'w', encoding="utf-8") as f:
        for k,v in trans_dict.items():
            f.write(f"{k},{v}\n")
    input("処理終了\ndictionary.txtに書き込みが完了しました。enterキーを押して終了...")

    

if __name__ == '__main__':
    main()