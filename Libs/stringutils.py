def generate_embed(input_string):
    def format_chunk(chunk):
        lines = chunk.split('\n')
        return '\n'.join([f'> {line}' for line in lines])
    
    max_length = 1950
    formatted_output = ""
    
    while len(input_string) > max_length:
        split_index = input_string.rfind('\n', 0, max_length)
        if split_index == -1:
            split_index = max_length
        chunk = input_string[:split_index]
        formatted_output += "> ```diff\n" + format_chunk(chunk) + "\n> ```\n"
        input_string = input_string[split_index:]
    
    formatted_output += "> ```diff\n" + format_chunk(input_string) + "\n> ```"
    
    return formatted_output

def align(input_str,sep):
    lines = input_str.strip().split('\n')
    max_length = max(len(line.split(sep)[0].strip()) for line in lines)
    formatted_lines = []
    for line in lines:
        command, description = line.split(sep)
        command = command.strip()
        description = description.strip()
        formatted_line = f"{command.ljust(max_length)} {sep} {description}"
        formatted_lines.append(formatted_line)
    result = '\n'.join(formatted_lines)
    return result
