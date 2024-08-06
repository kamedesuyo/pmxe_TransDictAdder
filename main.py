import pymeshio.pmx.reader as pmxreader
import glob
import os

material_list_path = "material_list.txt"
material_trans_list_path = "material_trans_list.txt"
dictionary_path = "dictionary.txt"
check_list_path = [material_list_path, material_trans_list_path]

dictionary_data = {}     # 辞書データ
material_list = []       # マテリアル名リスト
material_trans_list = [] # 翻訳結果リスト
error_list = []          # pmxロード時エラーリスト

# dict_pathのチェック
# try get dict path -> 存在しない or 空の場合、dictionary.txtを作成
with open("dict_path.txt", 'r', encoding="utf-8") as f:
    path = f.read().replace(" ", "").replace("\"","")
    if 0 < len(path) and os.path.exists(path):
        dictionary_path = path
    elif 0 < len(path) and not os.path.exists(path):
        print(f"エラー: 辞書ファイルパス:{path}が存在しません。")
        print(f"同階層にdictionary.txtを生成して続行します。{dictionary_path}")

# 各種list_pathのチェック
# list,trans_listファイルが存在しない場合、空ファイルを作成
for path in check_list_path:
    if not os.path.exists(path):
        open(path, 'w', encoding="utf-8").close()

# 終了処理
def exit_process():
    input("\nenterキーを押して終了...")
    os.remove(material_list_path)
    os.remove(material_trans_list_path)
    exit(-1)

# pmxファイルロード時のエラーメッセージ表示
def show_load_error():
    for error in error_list:
        print(error)

# dictionary.txtのデータ取得
def get_dictionary_data():
    global dictionary_data
    with open(dictionary_path, "r", encoding="utf-8") as f:
        dictionary_list = f.read().replace(" ", "").split("\n")
        # 辞書化
        for i in range(len(dictionary_list)-1):
            try:
                k = dictionary_list[i].split(",")[0]
                v = dictionary_list[i].split(",")[1]
            except Exception as e:
                print(e)
            dictionary_data[k] = v

#pmxファイルからマテリアル名取得
def get_material_list():
    # pmxファイル取得
    file_list = glob.glob(os.path.join("pmx", "*.pmx"))
    for file in file_list:
        file.replace('\\', '/')
        try:
            pmx = pmxreader.read_from_file(file)
            for material in pmx.materials:
                if material.name not in dictionary_data.keys():
                    material_list.append(material.name)
        except Exception as e:
            error_list.append(f"{file}の読み込みに失敗しました。")
    if len(material_list) == 0:
        print("追加するマテリアル名が見つかりませんでした。\npmxフォルダ内にpmmが含まれているか確認してください。")
        exit_process()
        
# マテリアル名をmaterial_list.txtに書き出す
def write_material_names() -> None:
    with open(material_list_path, 'w',encoding="utf-8") as f:    
        for material in material_list:
            try:
                f.write(f"{material}\n")
            except Exception as e:
                error_list.append(f"ファイル書き込み中にエラーが発生しました:{e}")
                exit_process()

# 翻訳結果要求と取得
def get_material_trans_list():
    global material_trans_list
    while(1):
        try:    
            input("material_trans_list.txtに翻訳結果を入力後、enterキーを押してください。(終了:Ctrl+C)")
            with open(material_trans_list_path, 'r', encoding="utf-8") as f:
                material_trans_list = f.read().replace(" ", "").split("\n")
                # 翻訳結果が空、行数が違う、keyboardInterruptの場合は終了
                if material_trans_list == [""]:
                    print("翻訳結果が空です。")
                elif len(material_list) != len(material_trans_list):
                    print("マテリアル名と翻訳結果の行数が一致しません。")
                else:
                    # 空の翻訳結果リストを削除
                    for trans in material_trans_list:
                        if trans == "":
                            trans.delete()
                    return material_trans_list
        except KeyboardInterrupt:
            exit_process()
        except Exception as e:
            print(e)
            input("enterキーを押して再度実行してください。")


# main処理
def main():
    global material_list
    global material_trans_list
    global dictionary_data

    
    get_dictionary_data()
    get_material_list()
    material_list = sorted(list(set(material_list)))
    write_material_names()
    print(f"マテリアル名取得処理が完了しました。追加予定:\n{material_list}\n")
    show_load_error()

    # 翻訳結果取得、辞書作成
    get_material_trans_list()
    trans_dict = {}
    for k, n in zip(material_list, material_trans_list):
        trans_dict[k] = n 
    # dictionary.txtの内容に差分追加
    trans_dict.update(dictionary_data)
    
    # 辞書書き込み
    with open(dictionary_path, 'a', encoding="utf-8") as f:
        for k,v in trans_dict.items():
            f.write(f"{k},{v}\n")
    input(f"処理終了\n{dictionary_path}に書き込みが完了しました。")
    print("material_list.txtとmaterial_trans_list.txtを削除します")
    exit_process()

if __name__ == '__main__':
    main()