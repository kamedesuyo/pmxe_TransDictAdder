from TransDictAdder.validation.pmx_validiation import get_valid_pmx_paths
import pymeshio.pmx.reader as pmxreader
import pymeshio.pmx.writer as pmxwriter

def model_rename(materials_dict:dict):
    write_model_name = []
    error_model_name = []
    #model情報取得 → material読み込み → material_dictからrename → pmx更新
    files = get_valid_pmx_paths(show_detail_info=False)
    for file in files:
        pmx = pmxreader.read_from_file(file)
        for material in pmx.materials:
            material.name = materials_dict[material.name]
        try:
            model_name = file.replace(".pmx","_rename.pmx")
            pmxwriter.write_to_file(pmx,model_name)
            write_model_name.append(model_name.split("\\")[-1])
        except Exception as e:
            error_model_name.append(f"エラー: {e} {file}")
    print("\n\nリネームモデルの生成が終了しました。")
    if len(error_model_name):
            print(f"{len(error_model_name)}体のモデルさんの読み込み時にエラーが発生しました。\n   {"\n   ".join(error_model_name)}")
    print(f"生成したモデル名:\n[{', '.join(write_model_name)}]\n")