import pymeshio.pmx.reader as pmxreader
import glob


def load_materials_dict(dictionary_data:dict) -> dict:
    load_models_name = []
    load_models_error = []
    load_models_material = {}

    # pmxファイルを読み込む
    pmx_files = glob.glob("pmx/**/*.pmx",recursive=True)
    for pmx_file in pmx_files:
        try:
            pmx = pmxreader.read_from_file(pmx_file)
            load_models_name.append(pmx_file.split('\\')[-1])
            # 材質名を取得(辞書形式)
            for material in pmx.materials:
                if material.name not in dictionary_data:
                    load_models_material[material.name] = ""
        except TypeError as e:
            load_models_error.append(f"エラー: 追加UVが存在します。 {pmx_file}")
        except Exception as e:
            load_models_error.append(f"エラー: {pmx_file}  {str(e)}")
    print(f"{len(load_models_name)}体のモデルさんの読み込みに成功しました。\n   [{", ".join(load_models_name)}]")
    print(f"{len(load_models_error)}体のモデルさんの読み込み時にエラーが発生しました。\n   {"\n   ".join(load_models_error)}")

    return load_models_material