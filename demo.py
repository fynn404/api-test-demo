import json

def print_json_paths(data, path=''):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            print_json_paths(value, new_path)
    elif isinstance(data, list):
        for index, item in enumerate(data):

            new_path = f"{path}[X]"
            print_json_paths(item, new_path)
    else:
        print(path)

if __name__ == '__main__':
    # 从文件读取 JSON 数据
    file_path = './gin-demo/input/2.json'  # 替换为你的文件路径

    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 打印 JSON 路径
    print_json_paths(json_data)
