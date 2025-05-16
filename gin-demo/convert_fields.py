import re

tmp_list = set()

def convert_field(line):
    # 定义转换规则
    patterns = {
        r'GetUserBaseInfo\(\)\.(\w+)': lambda x: x.lower(),
        r'addressInfo\.(\w+)': lambda x: x.lower(),
        r'GetOccupationInfo\(\)\.(\w+)': lambda x: f'occupation_info[X].{convert_camel_to_snake(x)}',
        r'GetIDCardInfo\(\)\.(\w+)': lambda x: f'id_card_info[X].{convert_camel_to_snake(x)}',
        r'GetKycInfo\(\)\.(\w+)': lambda x: f'kyc_info[X].{convert_camel_to_snake(x)}',
        r'GetContactInfoList\(\)\.(\w+)': lambda x: f'contact_info_list[X].{convert_camel_to_snake(x)}',
        r'GetAddressInfoList\(\)\.(\w+)': lambda x: f'address_info_list[X].{convert_camel_to_snake(x)}'
    }
    
    # def convert_camel_to_snake(name):
    #     name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    #     return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

    def convert_camel_to_snake(name):
        result = []
        for char in name:
            if char.isupper():
                if result:  # 如果不是第一个字符，就加下划线
                    result.append('_')
                result.append(char.lower())
            else:
                result.append(char)
        return ''.join(result)


    for pattern, converter in patterns.items():
        match = re.search(pattern, line)
        if match:
            field_name = match.group(1)
            return converter(field_name)
    return None

def process_file(content):
    lines = content.split('\n')
    for line in lines:
        # 查找所有匹配的字段
        for pattern in [
            r'GetUserBaseInfo\(\)\.\w+',
            r'GetOccupationInfo\(\)\.\w+',
            r'GetIDCardInfo\(\)\.\w+',
            r'GetKycInfo\(\)\.\w+'
        ]:
            matches = re.finditer(pattern, line)
            for match in matches:
                original = match.group(0)
                converted = convert_field(original)
                if converted:
                    out =  converted.replace('get_', '')
                    tmp_list.add(out)
                    # print(f"Original: {original} -> Converted: {out}")
                    # print(f"{out}")

def main():
    # 直接指定输入文件路径
    input_file = './input/convert.txt'
    try:
        with open(input_file, 'r') as f:
            content = f.read()
            print(f"Processing file: {input_file}")
            process_file(content)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except Exception as e:
        print(f"Error processing file: {str(e)}")
    sorted_list = sorted(tmp_list)
    [print(item,";") for item in sorted_list]



if __name__ == "__main__":
    main() 