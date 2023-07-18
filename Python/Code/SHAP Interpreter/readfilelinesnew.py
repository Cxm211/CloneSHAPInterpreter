import numpy

from model import Model
from transformers import (RobertaConfig, RobertaModel, RobertaTokenizer)
import torch
import os
import pandas as pd

def getm1linescount(filepath):

    linecount = 0
    device = torch.device("cpu")
    # path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/MutatedSemanticClonePairs'
    # path = 'pythontestfolder'
    path = filepath
    clone_files = os.listdir(path)
    def read_file_java(file_name):
        filename = filepath + "/" + file_name
        ori_file = open(filename, "r")
        m1 = ""
        m2 = ""
        line = ori_file.readline()
        m1 += line
        line = ori_file.readline()
        while not "def " in line:
            if line != "" and line != "\n":
                m1 += line
            line = ori_file.readline()
        # Read m2
        while line:
            if line != "" and line != "\n":
                m2 += line
            line = ori_file.readline()
        m2.remove("\n")
        return m1, m2

    clone_files
    # generate dissimilar pairs
    pairs = []
    for file_name in clone_files:
        code_1, code_2 = read_file_java(file_name)
        pairs.append((code_1, code_2))

    code_1, code_2 = pairs[0]

    import re
    lineendindices = res = [i.start() for i in re.finditer('\n', code_1)]
    linecount = len(lineendindices)-1
    return linecount

def getm1linescountfromfile(folderpath, filename):
    # include signature in linecount
    linecount = 0
    device = torch.device("cpu")
    # path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/MutatedSemanticClonePairs'
    # path = 'pythontestfolder'
    # path = filepath
    # clone_files = os.listdir(folderpath)

    def read_file_python(path, filename):
        ori_file = open(path + "/" + filename, "r")
        list_lines = []
        line = ori_file.readline()
        while line:
            list_lines.append(line)
            line = ori_file.readline()
        for i in range(len(list_lines)):
            if list_lines[i] == "\n" and list_lines[i + 1] == "\n":
                m1 = list_lines[:i]
                m2 = list_lines[i + 2:]
                break
        m2.remove("\n")
        if m1 and m2:
            m1_str = ""
            m2_str = ""
            for line in m1:
                m1_str += line
            for line in m2:
                m2_str += line
            return m1_str, m2_str
        else:
            print("Error occurs while detecting method 1 and method 2.")
            return None, None


    # generate dissimilar pairs
    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_python(folderpath, filename)
    pairs.append((code_1, code_2))

    code_1, code_2 = pairs[0]

    import re
    lineendindices = res = [i.start() for i in re.finditer('\n', code_1)]
    linecount = len(lineendindices)

    return linecount

def getm2linescountfromfile(folderpath, filename):
    # include signature in linecount
    linecount = 0
    device = torch.device("cpu")
    # path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/MutatedSemanticClonePairs'
    # path = 'G:/pythontestfolder'
    # path = filepath
    # clone_files = os.listdir(folderpath)

    def read_file_python(path, filename):
        ori_file = open(path + "/" + filename, "r")
        list_lines = []
        line = ori_file.readline()
        while line:
            list_lines.append(line)
            line = ori_file.readline()
        for i in range(len(list_lines)):
            if list_lines[i] == "\n" and list_lines[i + 1] == "\n":
                m1 = list_lines[:i]
                m2 = list_lines[i + 2:]
                break
        m2.remove("\n")
        if m1 and m2:
            m1_str = ""
            m2_str = ""
            for line in m1:
                m1_str += line
            for line in m2:
                m2_str += line
            return m1_str, m2_str
        else:
            print("Error occurs while detecting method 1 and method 2.")
            return None, None

    # generate dissimilar pairs
    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_python(folderpath, filename)
    pairs.append((code_1, code_2))

    code_1, code_2 = pairs[0]
    import re
    lineendindices = res = [i.start() for i in re.finditer('\n', code_2)]
    linecount = len(lineendindices)

    return linecount

def myfunc(filepath, m1lines):

    device = torch.device("cpu")
    # path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/MutatedSemanticClonePairs'
    # path = 'G:/pythontestfolder'
    path = filepath
    clone_files = os.listdir(path)

    def read_file_python(filename):
        ori_file = open(path + "/" + filename, "r")
        list_lines = []
        line = ori_file.readline()
        while line:
            list_lines.append(line)
            line = ori_file.readline()
        for i in range(len(list_lines)):
            if list_lines[i] == "\n" and list_lines[i + 1] == "\n":
                m1 = list_lines[:i]
                m2 = list_lines[i + 2:]
                break
        m2.remove("\n")
        if m1 and m2:
            m1_str = ""
            m2_str = ""
            for line in m1:
                m1_str += line
            for line in m2:
                m2_str += line
            return m1_str, m2_str
        else:
            print("Error occurs while detecting method 1 and method 2.")
            return None, None

    clone_files

    # generate dissimilar pairs
    pairs = []
    for file_name in clone_files:
        code_1, code_2 = read_file_python(file_name, m1lines)
        pairs.append((code_1, code_2))

    len(clone_files)

    BLOCK_SIZE = 400

    config = RobertaConfig.from_pretrained('roberta-base')
    # model = RobertaModel.from_pretrained('microsoft/codebert-base')
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

    # model = Model(model,config,tokenizer)

    # model_path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/model/mymodel.bin'
    # model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
    # model.to(device)


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
    lineendindices = res = [i.start() for i in re.finditer('\n', code_1)]
    m2lineendindices = res = [i.start() for i in re.finditer('\n', code_2)]
    # m1linesarray = numpy.asarray(m1lines)
    remainingcode = [code_1[lineendindices[x-1]+1:lineendindices[x]+1] for x in m1lines[0]]
    modifiedcode1 = ''.join(remainingcode)


    iput_ids = convert_examples_to_features(code_1, code_2)
    input_ids_mod = convert_examples_to_features(modifiedcode1, code_2)


    return input_ids_mod

def getm2InputIDS(folderpath, file_name, m2lines):

    device = torch.device("cpu")
    # path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/MutatedSemanticClonePairs'
    # path = 'G:/pythontestfolder'
    # path = filepath
    # clone_files = os.listdir(path)

    def read_file_python(path, filename):
        ori_file = open(path + "/" + filename, "r")
        list_lines = []
        line = ori_file.readline()
        while line:
            list_lines.append(line)
            line = ori_file.readline()
        for i in range(len(list_lines)):
            if list_lines[i] == "\n" and list_lines[i + 1] == "\n":
                m1 = list_lines[:i]
                m2 = list_lines[i + 2:]
                break
        m2.remove("\n")
        if m1 and m2:
            m1_str = ""
            m2_str = ""
            for line in m1:
                m1_str += line
            for line in m2:
                m2_str += line
            return m1_str, m2_str
        else:
            print("Error occurs while detecting method 1 and method 2.")
            return None, None

    # clone_files

    # generate dissimilar pairs
    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_python(folderpath, file_name)
    pairs.append((code_1, code_2))

    # len(clone_files)

    BLOCK_SIZE = 400

    config = RobertaConfig.from_pretrained('roberta-base')
    # model = RobertaModel.from_pretrained('microsoft/codebert-base')
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

    # model = Model(model,config,tokenizer)

    # model_path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/model/mymodel.bin'
    # model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
    # model.to(device)


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
    # lineendindices.extend([i.start() for i in re.finditer('\n', code_1)])
    m2lineendindices.extend([i.start() for i in re.finditer('\n', code_2)])
    # m1linesarray = numpy.asarray(m1lines)
    # remainingcode = [code_1[lineendindices[x-1]+1:lineendindices[x]+1] for x in m1lines[0]]
    # modifiedcode1 = ''.join(remainingcode)

    remainingcode2 = [code_2[m2lineendindices[x - 1] + 1:m2lineendindices[x] + 1] for x in m2lines[0]]
    modifiedcode2 = ''.join(remainingcode2)

    # iput_ids = convert_examples_to_features(code_1, code_2)
    input_ids_mod = convert_examples_to_features(code_1, modifiedcode2)


    return input_ids_mod

def getm1InputIDs(folderpath, file_name, m1lines):

    device = torch.device("cpu")
    # path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/MutatedSemanticClonePairs'
    # path = 'G:/pythontestfolder'
    # path = filepath
    # clone_files = os.listdir(path)

    def read_file_python(path,filename):
        ori_file = open(path + "/" + filename, "r")
        list_lines = []
        line = ori_file.readline()
        while line:
            list_lines.append(line)
            line = ori_file.readline()
        for i in range(len(list_lines)):
            if list_lines[i] == "\n" and list_lines[i + 1] == "\n":
                m1 = list_lines[:i]
                m2 = list_lines[i + 2:]
                break
        m2.remove("\n")
        if m1 and m2:
            m1_str = ""
            m2_str = ""
            for line in m1:
                m1_str += line
            for line in m2:
                m2_str += line
            return m1_str, m2_str
        else:
            print("Error occurs while detecting method 1 and method 2.")
            return None, None

    # generate dissimilar pairs
    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_python(folderpath, file_name)
    pairs.append((code_1, code_2))

    # len(clone_files)

    BLOCK_SIZE = 400

    config = RobertaConfig.from_pretrained('roberta-base')
    # model = RobertaModel.from_pretrained('microsoft/codebert-base')
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

    # model = Model(model,config,tokenizer)

    # model_path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/model/mymodel.bin'
    # model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
    # model.to(device)


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
    # m1linesarray = numpy.asarray(m1lines)
    remainingcode = [code_1[lineendindices[x-1]+1:lineendindices[x]+1] for x in m1lines[0]]
    modifiedcode1 = ''.join(remainingcode)


    iput_ids = convert_examples_to_features(code_1, code_2)
    input_ids_mod = convert_examples_to_features(modifiedcode1, code_2)


    return input_ids_mod

def getInputIDS(filepath):

    device = torch.device("cpu")
    # path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/MutatedSemanticClonePairs'
    # path = 'G:/pythontestfolder'
    path = filepath
    clone_files = os.listdir(path)

    def read_file_java(file_name):
        filename = filepath + "/" + file_name
        ori_file = open(filename, "r")
        m1 = ""
        m2 = ""
        line = ori_file.readline()
        m1 += line
        line = ori_file.readline()
        while not "def " in line:
            if line != "" and line != "\n":
                m1 += line
            line = ori_file.readline()
        # Read m2
        while line:
            if line != "" and line != "\n":
                m2 += line
            line = ori_file.readline()

        return m1, m2

    clone_files

    pairs = []
    for file_name in clone_files:
        code_1, code_2 = read_file_java(file_name)
        pairs.append((code_1, code_2))

    len(clone_files)

    BLOCK_SIZE = 400

    config = RobertaConfig.from_pretrained('roberta-base')
    # model = RobertaModel.from_pretrained('microsoft/codebert-base')
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

    # model = Model(model,config,tokenizer)

    # model_path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/model/mymodel.bin'
    # model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
    # model.to(device)


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
    # input_ids_mod = convert_examples_to_features(modifiedcode1, code_2)

    return iput_ids

def getInputIDSFromFile(path, filename):

    device = torch.device("cpu")
    # path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/MutatedSemanticClonePairs'
    # path = 'G:/pythontestfolder'
    # path = filepath
    # clone_files = os.listdir(path)

    def read_file_python(path, filename):
        ori_file = open(path + "/" + filename, "r")
        list_lines = []
        line = ori_file.readline()
        while line:
            list_lines.append(line)
            line = ori_file.readline()
        for i in range(len(list_lines)):
            if list_lines[i] == "\n" and list_lines[i + 1] == "\n":
                m1 = list_lines[:i]
                m2 = list_lines[i + 2:]
                break
        m2.remove("\n")
        if m1 and m2:
            m1_str = ""
            m2_str = ""
            for line in m1:
                m1_str += line
            for line in m2:
                m2_str += line
            return m1_str, m2_str
        else:
            print("Error occurs while detecting method 1 and method 2.")
            return None, None

    pairs = []
    # for file_name in clone_files:
    code_1, code_2 = read_file_python(path, filename)
    pairs.append((code_1, code_2))

    # len(clone_files)

    BLOCK_SIZE = 400

    config = RobertaConfig.from_pretrained('roberta-base')
    # model = RobertaModel.from_pretrained('microsoft/codebert-base')
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

    # model = Model(model,config,tokenizer)

    # model_path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/model/mymodel.bin'
    # model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
    # model.to(device)


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
    # input_ids_mod = convert_examples_to_features(modifiedcode1, code_2)

    return iput_ids

print("calling :")
filepath = 'G:/pythontestfolder'
# lines = [1,2,4]
# myfunc(filepath, lines)
# count = getm1linescount(filepath)
# print(count)