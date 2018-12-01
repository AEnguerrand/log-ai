import config
import pandas as pd

path_to_dir= config.path_file_name['path_result']
path_to_file_ori= config.path_file_name['label_raw']
path_to_file_dest= config.path_file_name['label_process']

def pre_process_label(path_to_dir, path_to_file_ori, path_to_file_dest):
    out_data = []

    pre_df = pd.read_csv(path_to_dir + path_to_file_ori)
    print("LOAD !")
    for line in pre_df["Label"]:
        if line == "Anomaly":
            out_data.append(1)
        else:
            out_data.append(0)
    out_data_csv = pd.DataFrame(data=out_data)
    out_data_csv.to_csv(path_to_dir + path_to_file_dest, header=None)

if __name__ == "__main__":
    pre_process_label(path_to_dir, path_to_file_ori, path_to_file_dest)