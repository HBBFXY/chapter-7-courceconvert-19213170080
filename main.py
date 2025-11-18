# 定义Python保留字列表（包含常用关键字）
RESERVED_WORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
}

# 读取原文件
with open('random_int.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 处理内容：拆分单词，保留字不变，其他小写转大写
processed_lines = []
for line in content.splitlines():
    processed_words = []
    for word in line.split():
        if word in RESERVED_WORDS:
            processed_words.append(word)
        else:
            processed_words.append(word.upper())
    processed_lines.append(' '.join(processed_words))
processed_content = '\n'.join(processed_lines)

# 保存到新文件（例如random_int_upper.py）
with open('random_int_upper.py', 'w', encoding='utf-8') as f:
    f.write(processed_content)
