from TransDictAdder.model_loader.load_models import get_valid_pmx_paths
import pymeshio.pmx.reader as pmxreader
import pymeshio.pmx.writer as pmxwriter

def model_rename(materials_dict:dict):
    #model情報取得 → material読み込み → material_dictからrename → pmx更新
    files = get_valid_pmx_paths()
    for file in files:
        pmx = pmxreader.read_from_file(file)
        for material in pmx.materials:
            material.name = materials_dict[material.name]
        pmxwriter.write_to_file(pmx,file.replace(".pmx","_rename.pmx"))
    