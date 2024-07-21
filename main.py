def read_file_lines(filepath: str) -> list:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
        if not lines:
            raise ValueError(f"{filepath} が空です。")
        return lines
    except FileNotFoundError as e:
        handle_error(f"{filepath} が見つかりませんでした。", e)
    except ValueError as e:
        handle_error(str(e))

def handle_error(message: str, exception: Exception = None) -> None:
    print(f"{message} {exception if exception else ''}")
    input("続行するにはEnterキーを押してください...")
    exit(-1)

def preprocess_translate_text(translate_path: str) -> str:
    """重複する単語に連番を付与して空白削除"""
    lines = read_file_lines(translate_path)
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

    processed_path = f"{translate_path}_processed.txt"
    with open(processed_path, "w", encoding="utf-8") as f:
        for line in processed_lines:
            print(line.replace(" ", "_"), file=f)
    
    return processed_path

def create_dict(source_path: str, translate_path: str) -> dict:
    """翻訳前言語と日本語のテキストファイルから辞書を生成する"""
    processed_translate_path = preprocess_translate_text(translate_path)
    source_lines = read_file_lines(source_path)
    translate_lines = read_file_lines(processed_translate_path)

    if len(source_lines) != len(translate_lines):
        handle_error("source.txt と translate.txt の行数が一致しません。")

    return {source_lines[i].strip(): translate_lines[i].strip() for i in range(len(source_lines))}

def remove_unused_keys_from_dict(source_translate_dict: dict, template_path: str) -> dict:
    """テンプレート内で使用されていない辞書のキーを削除する"""
    template_lines = read_file_lines(template_path)
    keys_to_check = set(source_translate_dict.keys())

    for line in template_lines:
        keys_to_remove = {key for key in keys_to_check if key in line.split(",")}
        keys_to_check -= keys_to_remove
        for key in keys_to_remove:
            del source_translate_dict[key]

    return source_translate_dict

def append_to_template(template_path: str, source_translate_dict: dict) -> None:
    """テンプレートファイルに辞書の内容を追加"""
    try:
        with open(template_path, "a", encoding="utf-8") as file:
            for key, value in source_translate_dict.items():
                file.write(f"{value.strip()}, _{key.strip()}\n")
            for key in source_translate_dict.keys():
                file.write(f"{key.strip()}, _{key.strip()}\n")
    except IOError as e:
        handle_error("ファイルの書き込み中にエラーが発生しました。", e)

def main():
    dict_path = ("source.txt", "translate.txt")
    template_path = "和英変換.txt"

    source_translate_dict = create_dict(*dict_path)
    source_translate_dict = remove_unused_keys_from_dict(source_translate_dict, template_path)
    append_to_template(template_path, source_translate_dict)

    print("辞書の生成が完了しました。")
    print("書き込み終了")
    print("処理が完了しました。")

    input("続行するにはEnterキーを押してください...")
    exit(0)

if __name__ == "__main__":
    main()
