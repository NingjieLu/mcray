# -*- coding: utf-8 -*-
import os
import jieba

LTP_DATA_DIR = 'e:/aa/LTP/ltp_data/'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`


text = "左侧基底节及放射冠区、左侧颞枕叶交界处脑梗塞，合并少许出血可能，建议头颅MRI"
# print (text)
#fileObject.close()

# words = list(jieba.cut(text))

from pyltp import Segmentor
segmentor = Segmentor()  # 初始化实例
segmentor.load_with_lexicon(cws_model_path, '')
words = segmentor.segment(text)  # 分词
print ('\t'.join(words))
segmentor.release()  # 释放模型

pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
from pyltp import Postagger
postagger = Postagger() # 初始化实例
postagger.load_with_lexicon(pos_model_path, 'e:/aa/LTP/ltp_data/lexicon.model')  # 加载模型
postags = postagger.postag(words)  # 词性标注
# print ('\t'.join(postags))
postagger.release()  # 释放模型


par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
from pyltp import Parser
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型
arcs = parser.parse(words, postags)  # 句法分析
#
parser.release()  # 释放模型


ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
from pyltp import NamedEntityRecognizer
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load(ner_model_path)  # 加载模型
netags = recognizer.recognize(words, postags)  # 命名实体识别
# print ('\t'.join(netags))
recognizer.release()  # 释放模型

srl_model_path = os.path.join(LTP_DATA_DIR, 'srl')
from pyltp import SementicRoleLabeller
labeller = SementicRoleLabeller() # 初始化实例
labeller.load(srl_model_path)  # 加载模型
roles = labeller.label(words, postags, netags, arcs)  # 语义角色标注
# for role in roles:
#     print (words[role.index], "".join(
#         ["%s:(%s%s)" % (arg.name, words[arg.range.start], words[arg.range.end]) for arg in role.arguments]))
for role in roles:
	print (words[role.index], end=' ')
	for arg in role.arguments:
		ran = arg.range.start
		print (arg.name, end=':')
		while (ran <= arg.range.end):
			print (words[ran], end='')
			ran = ran + 1
		print (end=' ')
	print ()

for role in roles:
	# print (words[role.index], end=' ')
	for arg in role.arguments:
		ran = arg.range.start
		if arg.name=='A0':
			# print (arg.name, end=':')
			while (ran <= arg.range.end):
				print (words[ran], end='')
				ran = ran + 1
			print (end=' ')
	print ()
labeller.release()  # 释放模型
