# encoding=utf-8
import json
import re
from urllib.parse import quote,unquote


def clean_name(text,is_ment):
  text = text.strip()
  if not is_ment:
    text = text.replace('nhttps://en.wikipedia.org/wiki/', '').replace('hhttps://en.wikipedia.org/wiki/', ''). \
      replace(']https://en.wikipedia.org/wiki/', '').replace('https://en.wikipedia.org/wiki/', '').replace(
      'ttps://en.wikipedia.org/wiki/', '').replace('_', ' ').replace('-', ' ')
  text = unquote(text)
  return text

def is_in_cands(gold,ents):
  cleaned_gold = clean_name(gold, is_ment=False)
  for ent in ents:
    if ent == gold or \
       ent == cleaned_gold or \
       clean_name(ent, is_ment=False) == gold or \
       clean_name(ent, is_ment=False) == cleaned_gold:
       return True
  return False

def readCorpus():
  print('Reading datasets...')
  with open(path_train_with_cands, 'r', encoding='utf-8') as fr:
    trainData = json.load(fr)
  with open(path_dev_with_cands, 'r', encoding='utf-8') as fr:
    devData = json.load(fr)
  with open(path_test_with_cands, 'r', encoding='utf-8') as fr:
    testData = json.load(fr)
  return trainData, devData, testData

def test_recall(topk,raw_corpus):
  n_hit=0;n_total=0;n_failed=0
  for [caption, img, ment, ment_type, lctx, rctx, entity, cands, topic, start, end] in raw_corpus:
    entity = re.sub(r"(nhttps)|(hhttps)|(\]https)|(\])|(\[)", "https", entity)
    if entity.lower()=='nil':
      continue
    n_total += 1
    tmp_cands=[]
    for c in cands:
      if len(tmp_cands) == topk:
        break
      if c not in tmp_cands:
        tmp_cands.append(c)
    if is_in_cands(entity, tmp_cands):
      n_hit += 1
  print('{:.4f}%'.format(n_hit/n_total*100))
  return

if __name__=='__main__':
  topk=10

  path_train_with_cands = 'wikidiverse_w_cands/train_w_10cands.json'
  path_dev_with_cands = 'wikidiverse_w_cands/valid_w_10cands.json'
  path_test_with_cands = 'wikidiverse_w_cands/test_w_10cands.json'

  trainData, devData, testData=readCorpus()
  print('train:')
  test_recall(topk, trainData)
  print('dev:')
  test_recall(topk, devData)
  print('test:')
  test_recall(topk, testData)
  print('-'*100)

