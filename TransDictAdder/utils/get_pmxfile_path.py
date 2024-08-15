import glob 

default_directory = "models/"

def get_pmxfile()->list:
    files = glob.glob(f"{default_directory}**/*.pmx",recursive=True)
    files = [f for f in files if "_rename" not in f]
    return files