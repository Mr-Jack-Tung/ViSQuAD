---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: Id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: ans_start
    dtype: int64
  - name: text
    dtype: string
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 24944836
    num_examples: 19240
  - name: test
    num_bytes: 5091238
    num_examples: 4065
  download_size: 4943526
  dataset_size: 30036074
---
# Dataset Card for "viquad"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
