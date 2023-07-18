from readfilelinesnew import *
from readfilelinesnew import *
from model import Model
# from model20 import Model20
from transformers import (RobertaConfig, RobertaModel, RobertaTokenizer)
import torch
from collections import Counter
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, \
    precision_score, recall_score, f1_score, accuracy_score
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
    m1linecount = getm1linescountfromfile(folderpath, file_name)
    print("count: " + str(m1linecount))
    for i in range(0, m1linecount):
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
            # ind = torch.tensor(X, dtype=torch.int64)
            ind = torch.tensor(bt2.numpy(),dtype=torch.int64)
            out = model(ind).detach().numpy()
            # set base value to 0.5 for both class predictions, this is based on avg. training dataset values
            out[0] = 0.5


        elif m == 2:
            m = m + 1
            # here we calculate the prediction for test input sample that we want to explain locally
            # ind = torch.tensor(X, dtype=torch.int64)
            ind = torch.tensor(test_samples2.numpy(), dtype=torch.int64)
            ind = getInputIDSFromFile(folderpath, file_name)
            # out = model(ind).detach().numpy()
            outfortorch = model(ind)
            out = outfortorch.detach().numpy()
            # predictedvalues.append(out)
            prediction = int(torch.argmax(outfortorch))
            print(prediction)
            # onepredictedvalues.append(prediction)
            List.extend([file_name,prediction])
            # print(out)
        elif m == 3:
            m = m + 1
            # print(X[0])
            # here pass a tensor with normal tokenIDs
            # print("now pass a new tensor")
            # ind = torch.tensor(X, dtype=torch.int64)
            # out = model(ind).detach().numpy()
            # print(out)
            # outtemp = model(cat)

            import numpy as np
            # replace the background2 with masked 800 tokens
            out = model(background2).detach().numpy()
            arr = out
            # # for smth in range(1020):
            # indexoffirstmethodending = (background2[0] == 2).nonzero(as_tuple=True)[0]
            # realindex = indexoffirstmethodending[0]
            # indexesOf50118new = (background2[0] == 50118).nonzero(as_tuple=True)[0]
            # reached2 = False


            for thatsmth in X:
                # get indices from X[smth] where X[smth][i] is 80015
                import re
                print(thatsmth)
                indexesOfLinestoinclude = np.where(thatsmth != 50118)
                linenumberstoinclude = [x + 1 for x in indexesOfLinestoinclude]
                # linenumberstoinclude = indexesOfLinestoinclude + 1

                ln = numpy.array(linenumberstoinclude)
                # uncomment later
                inputIDs = getm1InputIDs(folderpath,file_name, ln)
                # mycounter = 0
                # for xsmth in thatsmth:
                #     mycounter += 1
                #     # indexesOf50118new = (bg2[0] == 50118).nonzero(as_tuple=True)[0]
                #     # indexesOfLinestoinclude = (thatsmth != 50118).nonzero(as_tuple=True)[0]
                #     if xsmth == 50118 and (mycounter <= 10):
                #         # get token ids from line xsmthi of background2 tensor
                #         print(xsmth)
                #         bg2 = replaceTokenIDsFromLine(background2, mycounter)
                #     elif (mycounter > 10):
                #         break

                # uncomment these two lines
                out = model(inputIDs).detach().numpy()
                arr = np.concatenate((out, arr))

                # out = model(background2).detach().numpy()
                # arr = np.concatenate((out, arr))

            # numrowsinX = len(X)
            # for smth in range(numrowsinX):
            #     arr = np.concatenate((out, arr))

            # print(arr)

            arr = arr[1:]
            # print('meow')
            out = arr
        return out

    # data = pd.DataFrame(background.numpy())
    # these lines are useful
    data = pd.DataFrame(bt.numpy())
    explainer = shap.KernelExplainer(f, data)
    shap_values = explainer.shap_values(test_samples2.numpy(), nsamples="auto")
    # shap.summary_plot(shap_values, data)
    # print(file_name)
    print("shap values: " + str(shap_values))
    # print(explainer.expected_value)
    # inputfiles.append(file_name)
    # shapvalues.append(shap_values)
    # oneshapvalues.append(shap_values[prediction])
    # List = [6, file_name, prediction, shap_values[prediction]]
    List.extend(shap_values)
    with open('sampledclonefileshaplogm1.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()


from csv import writer

device = torch.device("cpu")

train_data = pd.read_csv('semantic_clone_bench_train.csv')
# train_data.shape
# Counter(train_data.label)
# val_data = pd.read_csv('semantic_clone_bench_val.csv')
# val_data.shape
# Counter(val_data.label)
config = RobertaConfig.from_pretrained('roberta-base')
model = RobertaModel.from_pretrained('microsoft/codebert-base')
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = Model(model, config, tokenizer)
# model2 = Model20(model, config, tokenizer)
model_path = 'mymodel.bin'
model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
model.to(device)
BLOCK_SIZE = 400

# model2.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
# model2.to(device)
# BLOCK_SIZE_2 = 400

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

    # context_embeddings = model(torch.tensor(code1_ids)[None, :])[0]

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

# def convert_examples_to_features_2(code_1, code_2, label=None, remove_comments=None):
#     code1_tokens = tokenizer.tokenize(code_1)
#     code1_tokens = code1_tokens[:BLOCK_SIZE_2 - 2]
#     code1_tokens = [tokenizer.cls_token] + code1_tokens + [tokenizer.sep_token]
#     code1_ids = tokenizer.convert_tokens_to_ids(code1_tokens)
#
#     # context_embeddings = model(torch.tensor(code1_ids)[None, :])[0]
#
#     padding_length = BLOCK_SIZE_2 - len(code1_ids)
#     code1_ids += [tokenizer.pad_token_id] * padding_length
#
#     code2_tokens = tokenizer.tokenize(code_2)
#     code2_tokens = code2_tokens[:BLOCK_SIZE_2 - 2]
#     code2_tokens = [tokenizer.cls_token] + code2_tokens + [tokenizer.sep_token]
#     code2_ids = tokenizer.convert_tokens_to_ids(code2_tokens)
#     padding_length = BLOCK_SIZE_2 - len(code2_ids)
#     code2_ids += [tokenizer.pad_token_id] * padding_length
#
#     source_tokens = code1_tokens + code2_tokens
#     source_ids = code1_ids + code2_ids
#     if label is not None:
#         return source_ids, label
#     else:
#         return source_ids

remove_comments = False

class TextDataset(Dataset):
    def __init__(self):
        self.examples = []

        for i, row in train_data.iterrows():
            example = convert_examples_to_features(row['method_1'],
                                                   row['method_2'],
                                                   row['label'],
                                                   remove_comments)

            self.examples.append(InputFeatures(example[0], example[1]))

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, item):
        return torch.tensor(self.examples[item].input_ids), torch.tensor(self.examples[item].label)

# class TextDataset2(Dataset):
#     def __init__(self):
#         self.examples = []
#
#         for i, row in train_data.iterrows():
#             example = convert_examples_to_features_2(row['method_1'],
#                                                      row['method_2'],
#                                                      row['label'],
#                                                      remove_comments)
#
#             self.examples.append(InputFeatures(example[0], example[1]))
#
#     def __len__(self):
#         return len(self.examples)
#
#     def __getitem__(self, item):
#         return torch.tensor(self.examples[item].input_ids), torch.tensor(self.examples[item].label)

train_dataset = TextDataset()
# train_dataset2 = TextDataset2()
train_sampler = RandomSampler(train_dataset)
# train_sampler2 = RandomSampler(train_dataset2)
import shap
train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=1)
# train_dataloader2 = DataLoader(train_dataset2, sampler=train_sampler2, batch_size=2)
batch = next(iter(train_dataloader))
# batch2 = next(iter(train_dataloader2))
x, _ = batch
# x2, _ = batch2
# background = x[:2]
background2 = x[:1]
# cat = x[:1]
# for smth in range(200):
#     cat = torch.cat((background2, cat), 0)
# test_samples = x[1:2]
test_samples2 = x[:1]
# out = model(background2)


# List that we want to add as a new row
List = []
# with open('event.csv', 'a') as f_object:
#     writer_object = writer(f_object)
#     writer_object.writerow(List)
#     f_object.close()
# global prediction
prediction= -1
# inputfiles = []
# predictedvalues = []
# onepredictedvalues = []
# shapvalues = []
# oneshapvalues = []
folderpath = 'Python_Clones'
clone_files = os.listdir(folderpath)
for file_name in clone_files:
    List = []
    print(file_name)
    m = 1
    if file_name == ".DS_Store":
        a = 1
    else:
        main(folderpath, file_name)

# output = pd.DataFrame()
# output['file'] = inputfiles
# output['predictedvalue'] = predictedvalues
# output['shapvalues'] = shapvalues
# output['onepredictedvalue'] = onepredictedvalues
# output['oneshapvalues'] = oneshapvalues
# output.to_csv("shapoutput.csv")