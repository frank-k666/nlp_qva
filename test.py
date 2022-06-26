from dataset import *
import sys
import os.path
import mindspore
from mindspore import Tensor, nn, Model, context
from mindspore import load_checkpoint, load_param_into_net
from mindspore import ops
from mindspore.ops import functional as F
from mindspore.ops import composite as C
from mindspore.common.parameter import ParameterTuple
from mindspore.train.callback import LossMonitor, CheckpointConfig, ModelCheckpoint, TimeMonitor
# from mindspore.nn import WithLossCell
import numpy as np
from tqdm import tqdm
import config
import dataset
import san
import utils
import mindspore.context as context
import json
import math
from datetime import datetime

train_loader = dataset.get_loader(train=True)
from bert4ms import BertTokenizer, BertModel
bert=BertModel.load('bert-base-uncased')
tq = tqdm(train_loader, desc='{} EPOCH{:02d}'.format('train', 0), ncols=0, total=math.ceil(len(train_loader.source.questions) / config.batch_size))
for q, a, img in tq:
    # print(q.shape)
    result = bert(q)
    print(result)


# loader=get_loader(train = True).create_dict_iterator()
# # print("Loader Created")

# # print("iter:0")
# test = loader._get_next()
# # print(test['q'])
# # print(test['a'])
# # print(test['img'].shape)

# # print("iter:1")
# test = loader._get_next()
# print(test['q'].shape)
# # print(test['a'])
# # print(test['img'].shape)
# q_array = test['q'].asnumpy()
# print(q_array[0])