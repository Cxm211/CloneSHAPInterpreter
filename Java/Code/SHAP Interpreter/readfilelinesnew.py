import numpy

from model import Model
from transformers import (RobertaConfig, RobertaModel, RobertaTokenizer)
import torch
import os
import pandas as pd

def getm1linescount(filepath):

    linecount = 0
    device = torch.device("cpu")
    path = filepath
    clone_files = os.listdir(path)

    def read_file_java(file_name):
        with open(f'{path}/{file_name}') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        method_1, method_2 = [], []
        i = lines.index('')
        m_1 = '\n '.join(lines[:i])
        m_2 = '\n '.join(lines[i:])[2:-5]

        # print("m1", m_1)
        # print("m2", m_2)

        return m_1, m_2

    clone_files

    def remove_class_info(method):

        method = method.split('\n')
        # method is a list with a line of code on each index
        clean_method = []
        first = True
        code_lines = False
        for line in method:
            if first and ('public' in line or 'private' in line or 'static' \
                          in line or 'Node' in line or 'protected' in line or 'int' in line \
                          or 'boolean' in line):
                first = False
            elif not first and ('public' in line or 'private' in line or 'static' \
                                in line or 'Node' in line or 'protected' in line or 'int' in line \
                                or 'boolean' in line):
                code_lines = True
                clean_method.append(line)
            elif not first and code_lines:
                clean_method.append(line)

        clean_method = '\n'.join(clean_method)
        return clean_method.strip()

    # generate dissimilar pairs
    pairs = []
    for file_name in clone_files:
        code_1, code_2 = read_file_java(file_name)
        pairs.append((remove_class_info(code_1), code_2))

    code_1, code_2 = pairs[0]

    import re
    lineendindices = res = [i.start() for i in re.finditer('\n', code_1)]
    linecount = len(lineendindices)-1
    return linecount

def getm1linescountfromfile(folderpath, filename):

    linecount = 0
    device = torch.device("cpu")

    def read_file_java(file_name):
        with open(f'{folderpath}/{file_name}') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        method_1, method_2 = [], []
        i = lines.index('')
        m_1 = '\n '.join(lines[:i])
        m_2 = '\n '.join(lines[i:])[2:-5]

        # print("m1", m_1)
        # print("m2", m_2)

        return m_1, m_2

    # clone_files

    def remove_class_info(method):

        method = method.split('\n')
        # method is a list with a line of code on each index
        clean_method = []
        first = True
        code_lines = False
        for line in method:
            if first and ('public' in line or 'private' in line or 'static' \
                          in line or 'Node' in line or 'protected' in line or 'int' in line \
                          or 'boolean' in line):
                first = False
            elif not first and ('public' in line or 'private' in line or 'static' \
                                in line or 'Node' in line or 'protected' in line or 'int' in line \
                                or 'boolean' in line):
                code_lines = True
                clean_method.append(line)
            elif not first and code_lines:
                clean_method.append(line)

        clean_method = '\n'.join(clean_method)
        return clean_method.strip()

    # generate dissimilar pairs
    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_java(filename)
    pairs.append((remove_class_info(code_1), code_2))

    code_1, code_2 = pairs[0]

    import re
    lineendindices = res = [i.start() for i in re.finditer('\n', code_1)]
    linecount = len(lineendindices)

    return linecount

def getm2linescountfromfile(folderpath, filename):

    linecount = 0
    device = torch.device("cpu")

    def read_file_java(file_name):
        with open(f'{folderpath}/{file_name}') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        method_1, method_2 = [], []
        i = lines.index('')
        m_1 = '\n '.join(lines[:i])
        m_2 = '\n '.join(lines[i:])[2:-5]

        # print("m1", m_1)
        # print("m2", m_2)

        return m_1, m_2

    # clone_files

    def remove_class_info(method):

        method = method.split('\n')
        # method is a list with a line of code on each index
        clean_method = []
        first = True
        code_lines = False
        for line in method:
            if first and ('public' in line or 'private' in line or 'static' \
                          in line or 'Node' in line or 'protected' in line or 'int' in line \
                          or 'boolean' in line):
                first = False
            elif not first and ('public' in line or 'private' in line or 'static' \
                                in line or 'Node' in line or 'protected' in line or 'int' in line \
                                or 'boolean' in line):
                code_lines = True
                clean_method.append(line)
            elif not first and code_lines:
                clean_method.append(line)

        clean_method = '\n'.join(clean_method)
        return clean_method.strip()

    # generate dissimilar pairs
    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_java(filename)
    pairs.append((remove_class_info(code_1), code_2))

    code_1, code_2 = pairs[0]

    import re
    lineendindices = res = [i.start() for i in re.finditer('\n', code_2)]
    linecount = len(lineendindices)

    return linecount

def myfunc(filepath, m1lines):

    device = torch.device("cpu")
    path = filepath
    clone_files = os.listdir(path)

    def read_file_java(file_name, m1lines):
        with open(f'{path}/{file_name}') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        method_1, method_2 = [], []
        i = lines.index('')
        m_1 = '\n '.join(lines[:i])
        m_2 = '\n '.join(lines[i:])[2:-5]

        # print("m1", m_1)
        # print("m2", m_2)

        return m_1, m_2

    clone_files

    def remove_class_info(method):

        method = method.split('\n')
        # method is a list with a line of code on each index
        clean_method = []
        first = True
        code_lines = False
        for line in method:
            if first and ('public' in line or 'private' in line or 'static' \
                          in line or 'Node' in line or 'protected' in line or 'int' in line \
                          or 'boolean' in line):
                first = False
            elif not first and ('public' in line or 'private' in line or 'static'\
                                in line or 'Node' in line or 'protected' in line or 'int' in line \
                                or 'boolean' in line):
                code_lines = True
                clean_method.append(line)
            elif not first and code_lines:
                clean_method.append(line)

        clean_method = '\n'.join(clean_method)
        return clean_method.strip()

    pairs = []
    for file_name in clone_files:
        code_1, code_2 = read_file_java(file_name, m1lines)
        pairs.append((remove_class_info(code_1), code_2))

    len(clone_files)

    BLOCK_SIZE = 400

    def convert_examples_to_features(code_1, code_2):

        code1_tokens=tokenizer.tokenize(code_1)
        code1_tokens=code1_tokens[:BLOCK_SIZE-2]
        code1_tokens =[tokenizer.cls_token]+code1_tokens+[tokenizer.sep_token]
        code1_ids=tokenizer.convert_tokens_to_ids(code1_tokens)
        padding_length = BLOCK_SIZE - len(code1_ids)
        code1_ids+=[tokenizer.pad_token_id]*padding_length

        code2_tokens=tokenizer.tokenize(code_2)
        code2_tokens=code2_tokens[:BLOCK_SIZE-2]
        code2_tokens =[tokenizer.cls_token]+code2_tokens+[tokenizer.sep_token]
        code2_ids=tokenizer.convert_tokens_to_ids(code2_tokens)
        padding_length = BLOCK_SIZE - len(code2_ids)
        code2_ids+=[tokenizer.pad_token_id]*padding_length

        source_tokens=code1_tokens+code2_tokens
        source_ids=code1_ids+code2_ids
        return torch.tensor(source_ids).to(device)

    remove_comments = False
    predictions = []


    code_1, code_2 = pairs[0]

    import re
    lineendindices = res = [i.start() for i in re.finditer('\n', code_1)]
    m2lineendindices = res = [i.start() for i in re.finditer('\n', code_2)]
    remainingcode = [code_1[lineendindices[x-1]+1:lineendindices[x]+1] for x in m1lines[0]]
    modifiedcode1 = ''.join(remainingcode)


    iput_ids = convert_examples_to_features(code_1, code_2)
    input_ids_mod = convert_examples_to_features(modifiedcode1, code_2)


    return input_ids_mod

def getm2InputIDS(folderpath, file_name, m2lines):

    device = torch.device("cpu")

    def read_file_java(file_name):
        with open(f'{folderpath}/{file_name}') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        method_1, method_2 = [], []
        i = lines.index('')
        m_1 = '\n '.join(lines[:i])
        m_2 = '\n '.join(lines[i:])[2:-5]

        # print("m1", m_1)
        # print("m2", m_2)

        return m_1, m_2

    # clone_files

    def remove_class_info(method):

        method = method.split('\n')
        # method is a list with a line of code on each index
        clean_method = []
        first = True
        code_lines = False
        for line in method:
            if first and ('public' in line or 'private' in line or 'static' \
                          in line or 'Node' in line or 'protected' in line or 'int' in line \
                          or 'boolean' in line):
                first = False
            elif not first and ('public' in line or 'private' in line or 'static'\
                                in line or 'Node' in line or 'protected' in line or 'int' in line \
                                or 'boolean' in line):
                code_lines = True
                clean_method.append(line)
            elif not first and code_lines:
                clean_method.append(line)

        clean_method = '\n'.join(clean_method)
        return clean_method.strip()

    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_java(file_name)
    pairs.append((remove_class_info(code_1), code_2))

    # len(clone_files)

    BLOCK_SIZE = 400



    def convert_examples_to_features(code_1, code_2):

        code1_tokens=tokenizer.tokenize(code_1)
        code1_tokens=code1_tokens[:BLOCK_SIZE-2]
        code1_tokens =[tokenizer.cls_token]+code1_tokens+[tokenizer.sep_token]
        code1_ids=tokenizer.convert_tokens_to_ids(code1_tokens)
        padding_length = BLOCK_SIZE - len(code1_ids)
        code1_ids+=[tokenizer.pad_token_id]*padding_length

        code2_tokens=tokenizer.tokenize(code_2)
        code2_tokens=code2_tokens[:BLOCK_SIZE-2]
        code2_tokens =[tokenizer.cls_token]+code2_tokens+[tokenizer.sep_token]
        code2_ids=tokenizer.convert_tokens_to_ids(code2_tokens)
        padding_length = BLOCK_SIZE - len(code2_ids)
        code2_ids+=[tokenizer.pad_token_id]*padding_length

        source_tokens=code1_tokens+code2_tokens
        source_ids=code1_ids+code2_ids
        return torch.tensor(source_ids).to(device)

    remove_comments = False
    predictions = []

    # for pair in tqdm(pairs, total=len(clone_files)):
    code_1, code_2 = pairs[0]

    # add the code to get the lines specified in m1lines
    # get the indices of \n
    import re
    m2lineendindices = [-1]
    m2lineendindices.extend([i.start() for i in re.finditer('\n', code_2)])
    remainingcode2 = [code_2[m2lineendindices[x - 1] + 1:m2lineendindices[x] + 1] for x in m2lines[0]]
    modifiedcode2 = ''.join(remainingcode2)
    input_ids_mod = convert_examples_to_features(code_1, modifiedcode2)
    return input_ids_mod

def getm1InputIDs(folderpath, file_name, m1lines):

    device = torch.device("cpu")
    def read_file_java(file_name, m1lines):
        with open(f'{folderpath}/{file_name}') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        method_1, method_2 = [], []
        i = lines.index('')
        m_1 = '\n '.join(lines[:i])
        m_2 = '\n '.join(lines[i:])[2:-5]

        # print("m1", m_1)
        # print("m2", m_2)

        return m_1, m_2

    # clone_files

    def remove_class_info(method):

        method = method.split('\n')
        # method is a list with a line of code on each index
        clean_method = []
        first = True
        code_lines = False
        for line in method:
            if first and ('public' in line or 'private' in line or 'static' \
                          in line or 'Node' in line or 'protected' in line or 'int' in line \
                          or 'boolean' in line):
                first = False
            elif not first and ('public' in line or 'private' in line or 'static'\
                                in line or 'Node' in line or 'protected' in line or 'int' in line \
                                or 'boolean' in line):
                code_lines = True
                clean_method.append(line)
            elif not first and code_lines:
                clean_method.append(line)

        clean_method = '\n'.join(clean_method)
        return clean_method.strip()

    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_java(file_name, m1lines)
    pairs.append((remove_class_info(code_1), code_2))

    # len(clone_files)

    BLOCK_SIZE = 400


    def convert_examples_to_features(code_1, code_2):

        code1_tokens=tokenizer.tokenize(code_1)
        code1_tokens=code1_tokens[:BLOCK_SIZE-2]
        code1_tokens =[tokenizer.cls_token]+code1_tokens+[tokenizer.sep_token]
        code1_ids=tokenizer.convert_tokens_to_ids(code1_tokens)
        padding_length = BLOCK_SIZE - len(code1_ids)
        code1_ids+=[tokenizer.pad_token_id]*padding_length

        code2_tokens=tokenizer.tokenize(code_2)
        code2_tokens=code2_tokens[:BLOCK_SIZE-2]
        code2_tokens =[tokenizer.cls_token]+code2_tokens+[tokenizer.sep_token]
        code2_ids=tokenizer.convert_tokens_to_ids(code2_tokens)
        padding_length = BLOCK_SIZE - len(code2_ids)
        code2_ids+=[tokenizer.pad_token_id]*padding_length

        source_tokens=code1_tokens+code2_tokens
        source_ids=code1_ids+code2_ids
        return torch.tensor(source_ids).to(device)

    remove_comments = False
    predictions = []

    # for pair in tqdm(pairs, total=len(clone_files)):
    code_1, code_2 = pairs[0]

    # add the code to get the lines specified in m1lines
    # get the indices of \n
    import re
    lineendindices = [-1]
    lineendindices.extend([i.start() for i in re.finditer('\n', code_1)])
    m2lineendindices = res = [i.start() for i in re.finditer('\n', code_2)]
    remainingcode = [code_1[lineendindices[x-1]+1:lineendindices[x]+1] for x in m1lines[0]]
    modifiedcode1 = ''.join(remainingcode)
    iput_ids = convert_examples_to_features(code_1, code_2)
    input_ids_mod = convert_examples_to_features(modifiedcode1, code_2)
    return input_ids_mod

def getInputIDS(filepath):

    device = torch.device("cpu")
    path = filepath
    clone_files = os.listdir(path)

    def read_file_java(file_name):
        with open(f'{path}/{file_name}') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        method_1, method_2 = [], []
        i = lines.index('')
        m_1 = '\n '.join(lines[:i])
        m_2 = '\n '.join(lines[i:])[2:-5]

        # print("m1", m_1)
        # print("m2", m_2)

        return m_1, m_2

    clone_files

    def remove_class_info(method):

        method = method.split('\n')
        # method is a list with a line of code on each index
        clean_method = []
        first = True
        code_lines = False
        for line in method:
            if first and ('public' in line or 'private' in line or 'static' \
                          in line or 'Node' in line or 'protected' in line or 'int' in line \
                          or 'boolean' in line):
                first = False
            elif not first and ('public' in line or 'private' in line or 'static'\
                                in line or 'Node' in line or 'protected' in line or 'int' in line \
                                or 'boolean' in line):
                code_lines = True
                clean_method.append(line)
            elif not first and code_lines:
                clean_method.append(line)

        clean_method = '\n'.join(clean_method)
        return clean_method.strip()

    pairs = []
    for file_name in clone_files:
        code_1, code_2 = read_file_java(file_name)
        pairs.append((remove_class_info(code_1), code_2))

    len(clone_files)

    BLOCK_SIZE = 400

    def convert_examples_to_features(code_1, code_2):

        code1_tokens=tokenizer.tokenize(code_1)
        code1_tokens=code1_tokens[:BLOCK_SIZE-2]
        code1_tokens =[tokenizer.cls_token]+code1_tokens+[tokenizer.sep_token]
        code1_ids=tokenizer.convert_tokens_to_ids(code1_tokens)
        padding_length = BLOCK_SIZE - len(code1_ids)
        code1_ids+=[tokenizer.pad_token_id]*padding_length

        code2_tokens=tokenizer.tokenize(code_2)
        code2_tokens=code2_tokens[:BLOCK_SIZE-2]
        code2_tokens =[tokenizer.cls_token]+code2_tokens+[tokenizer.sep_token]
        code2_ids=tokenizer.convert_tokens_to_ids(code2_tokens)
        padding_length = BLOCK_SIZE - len(code2_ids)
        code2_ids+=[tokenizer.pad_token_id]*padding_length

        source_tokens=code1_tokens+code2_tokens
        source_ids=code1_ids+code2_ids
        return torch.tensor(source_ids).to(device)

    remove_comments = False
    predictions = []

    # for pair in tqdm(pairs, total=len(clone_files)):
    code_1, code_2 = pairs[0]

    iput_ids = convert_examples_to_features(code_1, code_2)
    return iput_ids

def getInputIDSFromFile(path, filename):

    device = torch.device("cpu")

    def read_file_java(file_name):
        with open(f'{path}/{file_name}') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        method_1, method_2 = [], []
        i = lines.index('')
        m_1 = '\n '.join(lines[:i])
        m_2 = '\n '.join(lines[i:])[2:-5]

        # print("m1", m_1)
        # print("m2", m_2)

        return m_1, m_2

    # clone_files

    def remove_class_info(method):

        method = method.split('\n')
        # method is a list with a line of code on each index
        clean_method = []
        first = True
        code_lines = False
        for line in method:
            if first and ('public' in line or 'private' in line or 'static' \
                          in line or 'Node' in line or 'protected' in line or 'int' in line \
                          or 'boolean' in line):
                first = False
            elif not first and ('public' in line or 'private' in line or 'static'\
                                in line or 'Node' in line or 'protected' in line or 'int' in line \
                                or 'boolean' in line):
                code_lines = True
                clean_method.append(line)
            elif not first and code_lines:
                clean_method.append(line)

        clean_method = '\n'.join(clean_method)
        return clean_method.strip()

    # generate dissimilar pairs
    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_java(filename)
    pairs.append((remove_class_info(code_1), code_2))

    # len(clone_files)

    BLOCK_SIZE = 400

    def convert_examples_to_features(code_1, code_2):

        code1_tokens=tokenizer.tokenize(code_1)
        code1_tokens=code1_tokens[:BLOCK_SIZE-2]
        code1_tokens =[tokenizer.cls_token]+code1_tokens+[tokenizer.sep_token]
        code1_ids=tokenizer.convert_tokens_to_ids(code1_tokens)
        padding_length = BLOCK_SIZE - len(code1_ids)
        code1_ids+=[tokenizer.pad_token_id]*padding_length

        code2_tokens=tokenizer.tokenize(code_2)
        code2_tokens=code2_tokens[:BLOCK_SIZE-2]
        code2_tokens =[tokenizer.cls_token]+code2_tokens+[tokenizer.sep_token]
        code2_ids=tokenizer.convert_tokens_to_ids(code2_tokens)
        padding_length = BLOCK_SIZE - len(code2_ids)
        code2_ids+=[tokenizer.pad_token_id]*padding_length

        source_tokens=code1_tokens+code2_tokens
        source_ids=code1_ids+code2_ids
        return torch.tensor(source_ids).to(device)

    remove_comments = False
    predictions = []

    # for pair in tqdm(pairs, total=len(clone_files)):
    code_1, code_2 = pairs[0]
    iput_ids = convert_examples_to_features(code_1, code_2)
    return iput_ids

print("calling :")
filepath = 'pythontestfolder'
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')