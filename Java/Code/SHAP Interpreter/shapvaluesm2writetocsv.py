from readfilelinesnew import *
from model import Model
from transformers import (RobertaConfig, RobertaModel, RobertaTokenizer)
import torch
from collections import Counter
import re
import pandas as pd
from torch.utils.data import DataLoader, Dataset, SequentialSampler, RandomSampler
from transformers import WEIGHTS_NAME, AdamW, get_linear_schedule_with_warmup
theindex = 0

def replaceTokenIDsFromLine(bg2, mycounter):
    t = bg2[0]
    print((t == 50118).nonzero(as_tuple=True)[0])
    indexesOf50118 = (t == 50118).nonzero(as_tuple=True)[0]
    indexoffirstmethodending = (t == 2).nonzero(as_tuple=True)[0]
    # mycounter is line number which needs to be deleted
    linestartindex = indexesOf50118[mycounter-2]
    lineendindex = indexesOf50118[mycounter-1]
    if lineendindex > indexoffirstmethodending[0]:
        lineendindex = indexoffirstmethodending[0]
    theindex =  lineendindex
    # iterate between linestartindex and lineendindex and replace all values with 50118
    for thex in range(linestartindex+1,lineendindex):
        bg2[0][thex] = 1
    return bg2


def main(folderpath, file_name):

    buckets = []
    # get m1lines
    m2linecount = getm2linescountfromfile(folderpath, file_name)
    for i in range(0, m2linecount):
        buckets.append(50118)
    # print(buckets)
    bt = torch.IntTensor([buckets])
    buckets = []
    for i in range(0, 800):
        buckets.append(50118)
    # print(buckets)
    bt2 = torch.IntTensor([buckets])

    def f(X):
        global m
        if m == 1:
            m = m + 1
            ind = torch.tensor(bt2.numpy(),dtype=torch.int64)
            out = model(ind).detach().numpy()
            # set base value to 0.5 for both class predictions, this is based on avg. training dataset values
            out[0] = 0.5

        elif m == 2:
            m = m + 1
            # here we calculate the prediction for test input sample that we want to explain locally
            ind = torch.tensor(test_samples2.numpy(), dtype=torch.int64)
            ind = getInputIDSFromFile(folderpath, file_name)
            outfortorch = model(ind)
            out = outfortorch.detach().numpy()
            prediction = int(torch.argmax(outfortorch))
            print(prediction)
            List.extend([file_name,prediction])

        elif m == 3:
            m = m + 1
            import numpy as np
            # replace the background2 with masked 800 tokens
            out = model(background2).detach().numpy()
            arr = out

            for thatsmth in X:
                # get indices from X[smth] where X[smth][i] is 80015
                import re
                indexesOfLinestoinclude = np.where(thatsmth != 50118)
                linenumberstoinclude = [x + 1 for x in indexesOfLinestoinclude]
                ln = numpy.array(linenumberstoinclude)
                inputIDs = getm2InputIDS(folderpath,file_name, ln)
                out = model(inputIDs).detach().numpy()
                arr = np.concatenate((out, arr))

            arr = arr[1:]
            out = arr
        return out

    data = pd.DataFrame(bt.numpy())
    explainer = shap.KernelExplainer(f, data)
    shap_values = explainer.shap_values(test_samples2.numpy(), nsamples="auto")
    print(shap_values)
    List.extend(shap_values)
    with open('100_m2_shap.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()


from csv import writer
device = torch.device("cpu")
dummy_data = pd.read_csv('dummy.csv')
config = RobertaConfig.from_pretrained('roberta-base')
model = RobertaModel.from_pretrained('microsoft/codebert-base')
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = Model(model, config, tokenizer)
model_path = 'model/mymodel.bin'
model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
model.to(device)
BLOCK_SIZE = 400

class InputFeatures(object):
    """A single training/test features for a example."""
    def __init__(self,
                 input_ids,
                 label):
        self.input_ids = input_ids
        self.label = label

def replacer(match):
    s = match.group(0)
    if s.startswith('/'):
        return " "  # note: a space and not an empty string
    else:
        return s

def convert_examples_to_features(code_1, code_2, label=None, remove_comments=None):
    code1_tokens = tokenizer.tokenize(code_1)
    code1_tokens = code1_tokens[:BLOCK_SIZE - 2]
    code1_tokens = [tokenizer.cls_token] + code1_tokens + [tokenizer.sep_token]
    code1_ids = tokenizer.convert_tokens_to_ids(code1_tokens)

    padding_length = BLOCK_SIZE - len(code1_ids)
    code1_ids += [tokenizer.pad_token_id] * padding_length

    code2_tokens = tokenizer.tokenize(code_2)
    code2_tokens = code2_tokens[:BLOCK_SIZE - 2]
    code2_tokens = [tokenizer.cls_token] + code2_tokens + [tokenizer.sep_token]
    code2_ids = tokenizer.convert_tokens_to_ids(code2_tokens)
    padding_length = BLOCK_SIZE - len(code2_ids)
    code2_ids += [tokenizer.pad_token_id] * padding_length

    source_tokens = code1_tokens + code2_tokens
    source_ids = code1_ids + code2_ids
    if label is not None:
        return source_ids, label
    else:
        return source_ids

remove_comments = False

class TextDataset(Dataset):
    def __init__(self):
        self.examples = []

        for i, row in dummy_data.iterrows():
            example = convert_examples_to_features(row['method_1'],
                                                   row['method_2'],
                                                   row['label'],
                                                   remove_comments)

            self.examples.append(InputFeatures(example[0], example[1]))

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, item):
        return torch.tensor(self.examples[item].input_ids), torch.tensor(self.examples[item].label)

dummy_dataset = TextDataset()
dummy_sampler = RandomSampler(dummy_dataset)
import shap
dummy_dataloader = DataLoader(dummy_dataset, sampler=dummy_sampler, batch_size=1)
batch = next(iter(dummy_dataloader))
x, _ = batch
background2 = x[:1]
test_samples2 = x[:1]
List = []
prediction= -1
folderpath = 'pythontestfolder'
clone_files = os.listdir(folderpath)
for file_name in clone_files:
    List = []
    print(file_name)
    m = 1
    main(folderpath, file_name)
