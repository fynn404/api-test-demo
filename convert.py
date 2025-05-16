import re


def camel_to_snake(name):
    # Convert CamelCase to snake_case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def extract_info(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Find all occurrences of the pattern
    pattern = r'Get(\w+)\(\)\.(\w+)'
    matches = re.findall(pattern, data)

    extracted_info = {}
    for section, field in matches:
        section_snake = camel_to_snake(section)
        field_snake = camel_to_snake(field)
        extracted_info[field] = f"{section_snake}.{field_snake}"

    return extracted_info


# Example usage
file_path = 'your_file.txt'
info = extract_info(file_path)
for original, transformed in info.items():
    print(f"{original} -> {transformed}")
