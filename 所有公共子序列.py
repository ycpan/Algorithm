def find_subsequences(source, target):
    """在 source 中找到所有子序列形式的 target，并返回索引。"""
    base_target = target
    target = base_target * (len(source) // len(base_target))
    source_len = len(source)
    all_found = []
    current_found = ''
    all_indices, current_indices = [], []
    for i in target:
        if i in source:
            current_found += i
            index = source.index(i)
            current_indices.append(source_len - (len(source) - index))
            source = source[(index+1):]
        if current_found == base_target:
            all_indices.append(current_indices)
            all_found.append(base_target)
            current_found = ''
            current_indices = []
        if not source or len(source) < len(base_target) or not set(source).intersection(set(base_target)):
            break
    return all_found, all_indices
if __name__ == '__main__':
    target = '违禁词'
    source = 'asdf违asdf禁aa词as违1禁2词3词禁aa违词as违1禁2词3'
    wanted = ['违禁词', '违禁词'], [[4, 9, 12], [15, 17, 19]]
    all_found,all_indices = find_subsequences(source, target)
    print(all_found)
    print(all_indices)
