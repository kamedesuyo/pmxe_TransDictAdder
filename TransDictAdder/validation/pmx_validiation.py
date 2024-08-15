import pymeshio.pmx.reader as pmxreader
from TransDictAdder.model_loader.load_models import get_pmxfile_path

def get_valid_pmx_paths(pmx_paths:list,show_detail_info:bool = True) -> list:
    load_models_name = []
    load_models_error = []
    load_models_paths = []
    
    pmx_paths = get_pmxfile_path()
    for pmx_path in pmx_paths:
        try:
            pmx = pmxreader.read_from_file(pmx_path)
            load_models_name.append(pmx_path.split('\\')[-1])
            load_models_paths.append(pmx_path)
        except TypeError as e:
            load_models_error.append(f"エラー: 追加UVが存在します。 {pmx_path}")
        except Exception as e:
            load_models_error.append(f"エラー: {pmx_path}  {str(e)}")
    if show_detail_info:
        print(f"{len(load_models_name)}体のモデルさんの読み込みに成功しました。\n   [{", ".join(load_models_name)}]")
        print(f"{len(load_models_error)}体のモデルさんの読み込み時にエラーが発生しました。\n   {"\n   ".join(load_models_error)}")
    return load_models_paths