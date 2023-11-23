# -*- coding: utf-8 -*-
# Author: Mr.Jack _ Công ty www.BICweb.vn
# Date: 23 November 2023

# https://huggingface.co/datasets/squad
# Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

import pyarrow.parquet as pq

file_name ='data/train-00000-of-00001-bfe7c79c7c608223.parquet'

parquet_file = pq.ParquetFile(file_name)
print(parquet_file.metadata)
print(parquet_file.schema)

ViSQuAD = pq.read_table(file_name, columns=['context', 'question', 'text']).to_pandas() # pq.read_table ; pq.read_pandas

print(f"### Tham khảo:",ViSQuAD['context'].loc[0])
print(f"### Câu hỏi:",ViSQuAD['question'].loc[0])
print(f"### Trả lời:",ViSQuAD['text'].loc[0])

"""
<pyarrow._parquet.FileMetaData object at 0x7f83682d1c10>
  created_by: parquet-cpp-arrow version 9.0.0
  num_columns: 7
  num_rows: 19240
  num_row_groups: 20
  format_version: 2.6
  serialized_size: 64441
<pyarrow._parquet.ParquetSchema object at 0x7f83684487c0>
required group field_id=-1 schema {
  optional binary field_id=-1 Id (String);
  optional binary field_id=-1 title (String);
  optional binary field_id=-1 context (String);
  optional binary field_id=-1 question (String);
  optional int64 field_id=-1 ans_start;
  optional binary field_id=-1 text (String);
  optional int64 field_id=-1 __index_level_0__;
}

### Tham khảo: Phạm Văn Đồng (1 tháng 3 năm 1906 – 29 tháng 4 năm 2000) là Thủ tướng đầu tiên của nước Cộng hòa Xã hội chủ nghĩa Việt Nam từ năm 1976 (từ năm 1981 gọi là Chủ tịch Hội đồng Bộ trưởng) cho đến khi nghỉ hưu năm 1987. Trước đó ông từng giữ chức vụ Thủ tướng Chính phủ Việt Nam Dân chủ Cộng hòa từ năm 1955 đến năm 1976. Ông là vị Thủ tướng Việt Nam tại vị lâu nhất (1955–1987). Ông là học trò, cộng sự của Chủ tịch Hồ Chí Minh. Ông có tên gọi thân mật là Tô, đây từng là bí danh của ông. Ông còn có tên gọi là Lâm Bá Kiệt khi làm Phó chủ nhiệm cơ quan Biện sự xứ tại Quế Lâm (Chủ nhiệm là Hồ Học Lãm).
### Câu hỏi: Tên gọi nào được Phạm Văn Đồng sử dụng khi làm Phó chủ nhiệm cơ quan Biện sự xứ tại Quế Lâm?
### Trả lời: Lâm Bá Kiệt
"""