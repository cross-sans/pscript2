import re
import os
import argparse
import subprocess

def compile_pscript(file):
    with open(file, 'r') as f:
        code = f.read()

    # Replace "set" statements with Python-style variable assignment
    code = re.sub(r'set\s+(\w+)\s+to\s+(.+)', r'\1 = \2', code)

    # Replace "input" function calls with Python's "input" function
    code = re.sub(r'input\s*\((.*)\)', r'input(\1)', code)

    # Replace ">" and "<" message delimiters with Python print statements
    code = re.sub(r'>:"(.*)":<', r'print("\1")', code)

    # Replace "arr" with Python list syntax
    code = re.sub(r'arr\s+(\w+)\s*=>\s*\[(.*)\]', r'\1 = [\2]', code)

    # Replace "func" with Python "def" syntax
    code = re.sub(r'func\s+(\w+)\s*\((.*)\)', r'def \1(\2):', code)

    # Replace "<comment>" with Python "# comment" syntax
    code = re.sub(r'<<(.*)>>', r'# \1', code)

    # Add indentation
    indent_level = 0
    lines = code.split('\n')
    code = ''
    for line in lines:
        if line.endswith('[') or line.endswith(':'):
            # Increase indentation level
            code += '    ' * indent_level + line + '\n'
            indent_level += 1
        elif line.startswith('end'):
            # Decrease indentation level
            indent_level -= 1
            code += '    ' * indent_level + line + '\n'
        else:
            # Use current indentation level
            code += '    ' * indent_level + line + '\n'

    # Remove the "class main[]" and "end[]" lines
    code = re.sub(r'class main\[\]\n', '', code)
    code = re.sub(r'end\[\]\n', '', code)

    # Remove empty lines
    code = '\n'.join(line for line in code.split('\n') if line.strip())

    # Wrap code in a "main" function and call it
    code = f'def main():\n{code}\n\nif __name__ == "__main__":\n    main()'
    with open(file.replace(".pscript",".py"),"w")as f:
        f.write(code)
