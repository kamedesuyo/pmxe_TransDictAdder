def preprocess_translate_text(translate_path: str) -> None:
    """重複する単語に連番を付与して空白削除"""
    try:
        with open(translate_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError as e:
        print(f"ファイルが見つかりませんでした。{e}")
        input("続行するにはEnterキーを押してください...")
        exit(-1)

    word_count = {}
    processed_lines = []
    for line in lines:
        words = line.strip().split()
        processed_words = []
        for word in words:
            if word in word_count:
                word_count[word] += 1
                processed_words.append(f"{word}{word_count[word]}")
            else:
                word_count[word] = 1
                processed_words.append(word)
        processed_lines.append(' '.join(processed_words))
    with open(translate_path, "w", encoding="utf-8") as f:
        for line in processed_lines:
            print(line.replace(" ", "_"),file=f)


def create_dict(source_path:str, translate_path:str)->dict:
    """翻訳前言語と日本語のテキストファイルから辞書を生成する"""
    #translate.txtの前処理
    preprocess_translate_text(translate_path)
    source_translate_dict = {}
    try:
        with open(source_path, "r", encoding="utf-8") as f:
            source = f.readlines()
        if(len(source)==0):
            print("source.txtが空です。")
            input("続行するにはEnterキーを押してください...")
            exit(-1)
        with open(translate_path, "r", encoding="utf-8") as f:
            translate = f.readlines()
        if(len(translate)==0):
            print("translate_path.txtが空です。")
            input("続行するにはEnterキーを押してください...")
            exit(-1)
    except FileNotFoundError as e:
        print(f"ファイルが見つかりませんでした。{e}")
        input("続行するにはEnterキーを押してください...")
        exit(-1)
    if(len(source)!=len(translate)):
        print("source.txtとtranslate.txtの行数が一致しません。")
        input("続行するにはEnterキーを押してください...")
        exit(-1)

    for i in range(len(source)):
        source_translate_dict[source[i].strip()] = translate[i].strip()
    return source_translate_dict

def search_template_and_remove_unused_keys(dict_path:tuple, template_path:str)->dict:
    """テンプレート内で使用されていない辞書のキーを削除する"""
    source_translate_dict = create_dict(*dict_path)
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            template = f.readlines()
    except FileNotFoundError as e:
        print(f"和英変換.txtが見つかりませんでした。{e}")
        input("続行するにはEnterキーを押してください...")
        exit(-1)
        
    keys_to_check = set(source_translate_dict.keys())
    for line in template:
        keys_to_remove = set()
        for key in keys_to_check:
            if key in line.split(","):
                keys_to_remove.add(key)
        keys_to_check -= keys_to_remove
        for key in keys_to_remove:
            del source_translate_dict[key]
    return source_translate_dict

def main():
    dict_path = ("source.txt", "translate.txt")
    template_path = "和英変換.txt"
    source_translate_dict = search_template_and_remove_unused_keys(dict_path,template_path)
    print(source_translate_dict)
    print("辞書の生成が完了しました。")
    print("書き込み中...")
    try:
        with open(template_path,"a",encoding="utf-8") as f:
            for k,v in source_translate_dict.items():
                f.write(f"{v.strip()}, _{k.strip()}\n")
            for key in source_translate_dict.keys():
                f.write(f"{key.strip()}, _{key.strip()}\n")
    except IOError as e:
         print(f"ファイルの書き込み中にエラーが発生しました: {e}")
         input("続行するにはEnterキーを押してください...")
         exit(-1)
         
    print("書き込み終了")
    print("処理が完了しました。")
    input("続行するにはEnterキーを押してください...")
    
if __name__ == "__main__":
    main()