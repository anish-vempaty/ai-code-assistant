import os

def get_code_files(project_dir, exts=(".py", ".js", ".ts", ".java")):
    code_files = []
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(exts):
                code_files.append(os.path.join(root, file))
    return code_files