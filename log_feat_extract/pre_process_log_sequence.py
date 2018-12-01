import config
import pandas as pd
import numpy as np
import re
import os.path

path_to_dir = config.path_file_name['path_result']
path_to_file_ori = config.path_file_name['log_parser']
path_to_file_dest = config.path_file_name['log_feat_extract']
path_to_file_label_ori = config.path_file_name['label_raw']

def pre_process_log_sequence(path_to_dir, path_to_file_ori, path_to_file_dest, path_to_file_label_ori):
    pre_df = pd.read_csv(path_to_dir + path_to_file_ori, usecols=['Content', 'EventId'])
    pre_df_label = pd.read_csv(path_to_dir + path_to_file_label_ori)
    len_log = len(pre_df.index)
    print("len_log", len_log)
    len_label = len(pre_df_label.index)
    print("len_label", len_label)
    print("LOAD !")
    print("[pre-process] Define index for each log line (extract block_name)")
    if os.path.isfile(path_to_dir + "index_" + path_to_file_dest):
        print("[SKIP] cache file found")
        pre_df_tmp = pd.read_csv(path_to_dir + "index_" + path_to_file_dest)
        print("LOAD !")
        matrix_log_index = [None] * len_log
        opt = zip(pre_df_tmp['block_name'])
        i = 0
        for row in opt:
            matrix_log_index[i] = row[0]
            i += 1
    else:
        matrix_log_index = [None] * len_log
        regc = re.compile(r'(blk_[\d\-]+)')
        opt = zip(pre_df['Content'])
        i = 0
        for row in opt:
            m = regc.search(row[0])
            if m:
                matrix_log_index[i] = m.group(1)
            else:
                matrix_log_index[i] = "ERROR"
            i += 1
        print("[pre-process] Export to csv (pre-index)")
        out_data_csv = pd.DataFrame(data=matrix_log_index)
        out_data_csv.to_csv(path_to_dir + "index_" + path_to_file_dest, header=['block_name'])
    print("[pre-process] Create dict matrix for each block_name")
    list_event = pre_df['EventId'].unique()
    len_event = list_event.size
    print("len_event", len_event)
    matrix_block_name = {}
    opt = zip(pre_df_label['BlockId'])
    for row in opt:
        matrix_block_name[row[0]] = np.zeros(len_event, dtype=int)
    matrix_block_name['ERROR'] = np.zeros(len_event, dtype=int)
    print("[pre-process] Create dict matrix for event list")
    list_event_dict = {}
    index_e = 0
    opt = zip(list_event)
    for row in opt:
        list_event_dict[row[0]] = index_e
        index_e += 1
    print("[pre-process] Count event for each log line")
    opt = zip(pre_df['EventId'])
    i = 0
    for row in opt:
        matrix_block_name[matrix_log_index[i]][list_event_dict[row[0]]] += 1
        i += 1
    print("[pre-process] Export to csv (log-sequence)")
    #remove error line
    del matrix_block_name['ERROR']
    with open(path_to_dir + path_to_file_dest, 'w') as csv_file:
        csv_file.write(",".join(list_event) + "," + "block_name" + "\n")
        opt = matrix_block_name
        for key, row in opt.items():
            csv_file.write(np.array2string(row, separator=',', max_line_width=np.inf)[1:-1] + "," + key + "\n")

if __name__ == "__main__":
    pre_process_log_sequence(path_to_dir, path_to_file_ori, path_to_file_dest, path_to_file_label_ori)
