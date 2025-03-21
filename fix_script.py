import re

# 修正対象のファイル
file_path = "script.py"

# ファイルを読み込む
with open(file_path, "r") as file:
    content = file.read()

# 非推奨の np.int を np.int32 に置き換える
updated_content = re.sub(r'\bnp\.int\b', 'np.int32', content)

# 修正内容をファイルに書き込む
with open(file_path, "w") as file:
    file.write(updated_content)

print(f"Updated {file_path}: replaced 'np.int' with 'np.int32'")