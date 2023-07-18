import os
import ast
import csv

INPUT_FOLDER = "Python_Clones"
clone_files = os.listdir(INPUT_FOLDER)

def get_two_methods(filename):
    ori_file = open(filename, "r")
    list_lines = []
    line = ori_file.readline()
    while line:
        list_lines.append(line)
        line = ori_file.readline()
    for i in range(len(list_lines)):
        if list_lines[i] == "\n" and list_lines[i+1] == "\n":
            m1 = list_lines[:i]
            m2 = list_lines[i+2:]
            break
    for i in m2:
        if i == "\n":
            m2.remove(i)
    if m1 and m2:
        return m1, m2
    else:
        print("Error occurs while detecting method 1 and method 2.")
        return None, None

def dfs(node, results):
    # Visit the current node
    # print(node)
    if isinstance(node, ast.FunctionDef):
        results.append("Function Definition")
    elif isinstance(node, ast.AsyncFunctionDef):
        results.append("Async Function Definition")
    elif isinstance(node, ast.ClassDef):
        results.append("Class Definition")
    elif isinstance(node, ast.Import):
        results.append("Import Statement")
    elif isinstance(node, ast.ImportFrom):
        results.append("Import From Statement")
    elif isinstance(node, ast.Expr):
        results.append("Expression")
    elif isinstance(node, ast.Assign):
        results.append("Variable Assignment")
    elif isinstance(node, ast.AugAssign):
        results.append("Augmented Assignment")
    elif isinstance(node, ast.If):
        results.append("IF condition")
    elif isinstance(node, ast.While):
        results.append("While Loop")
    elif isinstance(node, ast.For):
        results.append("For Loop")
    elif isinstance(node, ast.Try):
        results.append("Try Block")
    elif isinstance(node, ast.ExceptHandler):
        results.append("Except Block")
    elif isinstance(node, ast.With):
        results.append("With Block")
    elif isinstance(node, ast.Raise):
        results.append("Raise Statement")
    elif isinstance(node, ast.Return):
        results.append("Return Statement")
    elif isinstance(node, ast.Break):
        results.append("Break Statement")
    elif isinstance(node, ast.Continue):
        results.append("Continue Statement")
    elif isinstance(node, ast.Pass):
        results.append("Pass Statement")
    elif isinstance(node, ast.Delete):
        results.append("Delete Statement")
    elif isinstance(node, ast.Assert):
        results.append("Assert Statement")
    elif isinstance(node, ast.Import):
        results.append("Import Statement")
    elif isinstance(node, ast.Global):
        results.append("Global Statement")
    elif isinstance(node, ast.Nonlocal):
        results.append("Nonlocal Statement")

    # Recurse on the children of the current node
    for child_node in ast.iter_child_nodes(node):
        dfs(child_node, results)
    return results

def get_line_types(code):
    node = ast.parse(code)
    #print(ast.dump(node, indent=4))
    nodes_list = []
    results = dfs(node, nodes_list)
    return results

def main():
    for file_name in clone_files:
        if file_name != ".DS_Store":
            print("Running for " + file_name)
            f = open("stmtAnalysism1.csv", 'a')
            writer = csv.writer(f)
            m1_list, m2_list = get_two_methods(INPUT_FOLDER + "/" + file_name)
            m1 = ''.join(m1_list)
            m2 = ''.join(m2_list)
            print(m1)
            line_types = get_line_types(m1)
            print(line_types)
            for i, line in enumerate(line_types):
                if "else" in line or "elif" in line:
                    line_types.insert(i, "ELSE condition")
                row = [file_name, i,line]
                writer.writerow(row)
                print(f"line {i + 1}: {line}")
            f.close()
main()