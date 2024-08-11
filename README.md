# pmxe_TransDictAdder<br>
<h5>追加UVの存在しているモデルさんや、pmd形式には対応していません。</h5>
「TransDictAdder」は、モデル翻訳支援プラグインを使用する際の辞書を生成するためのpythonスクリプトです。releaseにexeファイルがあります。<br>
仕様としてはmodelフォルダ内に存在する.pmxファイルをすべて読み込んで材質名を吐き出し、それを翻訳して入力することで辞書が作れます。<br>
exeと同階層に存在するdict_path.txtにモデル翻訳支援プラグイン内にあるdictionaryの絶対パスを入れておくと自動で追記していってくれます。<br>

<h1>使用方法</h1>
    <ol>pmxフォルダ内に翻訳したいモデルさんのpmxをコピペ<br></ol>
    <ol>TransDictAdder.exeを起動</ol>
    <ol>material_list.txtが生成されるのでChatGPTやDeepl等で翻訳した結果をmaterial_trans_list.txtに入力<br></ol>
    <ol>dictionary.txtをプラグイン内の辞書と置き換え(dict_pathを設定している場合は不要)<br></ol>
    <ol>小ネタ:ChatGPTに以下のプロンプトを渡すとうまくいくかもしれません。<br></ol>
    <ol>「今から3DCGに関する文字を送るので,日本語に翻訳して翻訳結果だけ出力してください.注意する点:個数と順番,記号は記号のまま」<br></ol>
<h1>使用条件</h1>
必須事項: 禁止事項に触れないよう利用し、公式配布モデルの規約に同意できる方のみ使用可能。<br>
任意事項: クレジット表記は必須ではないが可能であれば明示を推奨。<br>

<h1>禁止事項</h1>
パッケージまたは一部ファイルの再配布・販売（改変後も含む）は禁止。<br>
規約範囲外の行為や権利者に迷惑がかかる行為は厳禁。<br>
他者の誹謗中傷目的の利用は禁止。<br>
政治および宗教関連での使用は禁止。<br>

<h1>免責事項</h1>
使用によって生じたいかなる問題に対しても、作者は一切の責任を負いません。<br>

<h1>クレジット</h1>
作者：かめのこ<br>
Twitter: @kamenoko_mmd
