# python3

def read_input():
    input_text = input().rstrip()
    if input_text == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_text == 'F':
        file_name = '06'
        with open(file_name, 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 101
    p_len = len(pattern)
    t_len = len(text)
    p_hash = sum(ord(c) for c in pattern)
    t_hash = sum(ord(c) for c in text[:p_len])
    occurrences = []

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            occurrences.append(i)
        if i < t_len - p_len:
            t_hash = t_hash - ord(text[i]) + ord(text[i+p_len])
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

