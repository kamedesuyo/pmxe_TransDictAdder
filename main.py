import pymeshio.pmx.reader as pmxreader
import glob
import os

# 拡張子の設定
file_extension = '*.pmx'

# 対象ファイルの取得
directory_path = "pmx"

# 拡張子のファイルを取得
file_list = glob.glob(os.path.join(directory_path, file_extension))

error_list = []
material_list = []
# ファイルの読み込み
for file in file_list:
    file.replace('\\', '/')
    try:
        pmx = pmxreader.read_from_file(file)
        for material in pmx.materials:
            material_list.append(material.name)
    except Exception as e:
        print(e)
        error_list.append(file)
print(set(material_list))
print(str(error_list)+"でエラーが発生しました。")