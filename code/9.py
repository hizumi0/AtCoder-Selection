import re
#正規表現を扱うためのPythonの標準ライブラリ`re`をインポートしています。
S = input()
print("YES" if re.match("^(dream|dreamer|erase|eraser)+$", S) else "NO")
#正規表現パターン`"^(dream|dreamer|erase|eraser)+$"`は、文字列が「dream」、「dreamer」、「erase」、「eraser」のいずれかの単語の繰り返しで構成されているかどうかを判定します。
