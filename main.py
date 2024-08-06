import pymeshio.pmx.reader as pmxreader
import glob
import os

file_extension = '*.pmx'
directory_path = "pmx"
file_list = glob.glob(os.path.join(directory_path, file_extension))
error_list = []

def get_material_list(material_list:list) -> list:
    for file in file_list:
        file.replace('\\', '/')
        try:
            pmx = pmxreader.read_from_file(file)
            for material in pmx.materials:
                material_list.append(material.name)
        except Exception as e:
            error_list.append(f"{file}でエラーが発生しました")
    return material_list


def write_material_names(material_list: list) -> None:
    with open('material_list.txt', 'w',encoding="utf-8") as f:    
        for material in material_list:
            try:
                f.write(f"{material}\n")
            except Exception as e:
                error_list.append(f"ファイル書き込み中にエラーが発生しました:{e}")

def show_error():
    for error in error_list:
        print(error)

# メイン処理
def main():
    # マテリアル名取得処理
    material_list = []
    get_material_list(material_list)
    material_list = list(set(material_list))
    material_list = sorted(material_list)
    write_material_names(material_list)
    show_error()

    # 辞書作成処理
    

if __name__ == '__main__':
    main()