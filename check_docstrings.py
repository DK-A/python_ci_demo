import ast
import glob
import sys

for file in glob.glob("*.py"):
    with open(file) as f:
        tree = ast.parse(f.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if ast.get_docstring(node) is None:
                print(f"{file}: Function '{node.name}' has no docstring")
                sys.exit(1)

print("All functions have docstrings")
