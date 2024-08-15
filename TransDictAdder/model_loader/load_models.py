from TransDictAdder.validation.pmx_validiation import get_valid_pmx_paths
import pymeshio.pmx.reader as pmxreader

def load_materials_dict(dictionary_data:dict) -> dict:
    load_models_material = {}
    pmx_files = get_valid_pmx_paths()
    for pmx_file in pmx_files:
        pmx = pmxreader.read_from_file(pmx_file)
        for material in pmx.materials:
            if material.name not in dictionary_data:
                load_models_material[material.name] = ""

    return load_models_material