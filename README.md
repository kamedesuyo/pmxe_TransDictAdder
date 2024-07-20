# pmxe_TransDictAdder<br>
「TransDictAdder」は、Pmxeditorを使用して材質名などを翻訳するための補助ツールです。
source.txtに材質名、translate.txtに翻訳後材質名を入れることで辞書に対して追加で書き込みを行います。

ベースの辞書としてかんな様の配布のcn→jp変換辞書の使用を推奨します。具体的な使い方も載っているので見てみてください。
https://note.com/kanna3939/n/na94bcef393c3

<h1>使用方法</h1>
    <ol>
        <li>TransDictAdderを「PmxEditor_XXXX_data\テンプレート」（和英変換.txtと同階層）に展開する</li>
        <li>PmxEditorを開き、材質タブに移動し、編集 → 名称の一択編集 → プルダウンから材質を選択</li>
        <li>和名をクリックし、全材質の名前をコピーする</li>
        <li>deepl等の翻訳サイトに行き、翻訳する</li>
        <li>翻訳前のテキストを「PmxEditor_XXXX_data\テンプレート\source.txt」に書き込む</li>
        <li>翻訳後のテキストを「PmxEditor_XXXX_data\テンプレート\translate.txt」に書き込む</li>
        <li>TransDictAdder.exeを起動し、指示に従う。</li>
        <li>PmxEditorの名称の一択編集画面に戻り、編集 → 「辞書から和名→英名作成(E) Ctrl+E」をクリック</li>
        <li>編集 → 「確定(D) Ctrl+P」をクリック</li>
        <li>編集 → 「辞書から英名→和名作成(J) Ctrl+J」をクリック</li>
        <li>編集 → 「確定(D) Ctrl+P」をクリック</li>
        <li>保存して完了</li>
    </ol>

<h1>使用条件</h1>
必須事項: 禁止事項に触れないよう利用し、公式配布モデルの規約に同意できる方のみ使用可能。
任意事項: クレジット表記は必須ではないが可能であれば明示を推奨。

<h1>禁止事項</h1>
パッケージまたは一部ファイルの再配布・販売（改変後も含む）は禁止。
規約範囲外の行為や権利者に迷惑がかかる行為は厳禁。
他者の誹謗中傷目的の利用は禁止。
政治および宗教関連での使用は禁止。

<h1>免責事項</h1>
使用によって生じたいかなる問題に対しても、作者は一切の責任を負いません。

<h1>クレジット</h1>
作者：かめのこ
Twitter: @kamenoko_mmd

release
v1.0 - (2024/7/20)新規リリース
