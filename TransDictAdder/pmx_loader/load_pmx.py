import pymeshio.pmx.reader as pmxreader
import glob


def load_materials_dict(dictionary_data:dict) -> dict:
    load_models_name = []
    load_models_error = []
    load_models_material = {}

    # pmxファイルを読み込む
    pmx_files = glob.glob("pmx/*.pmx")
    for pmx_file in pmx_files:
        try:
            pmx = pmxreader.read_from_file(pmx_file)
            load_models_name.append(pmx.name)
            # 材質名を取得(辞書形式)
            for material in pmx.materials:
                if material.name not in dictionary_data:
                    load_models_material[material.name] = ""
        except TypeError as e:
            load_models_error.append(f"{pmx_file} エラー: 追加UVが存在します。")
        except Exception as e:
            load_models_error.append(f"{pmx_file} エラー: {str(e)}")
    print(f"以下のモデルさんを読み込みました。\n   [{", ".join(load_models_name)}]")
    print(f"以下のモデルさんでエラーが発生しました。\n   {"\n   ".join(load_models_error)}")

    return load_models_material