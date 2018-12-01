# Definition of global for path to files
global_data = {
    'path': 'dataset/',
    'log_seq_file_name': 'log_sequence_process.csv',
    'label_file_name': 'label_process.csv',
    'label_ori': 'anomaly_label.csv',
    'log_ori': 'HDFS.log_structured.csv',
    'path_result_log_parsing_dir': 'results/',
    'path_result_log_parsing': 'results/HDFS.log_structured.csv',
    'log_event_ori': 'results/HDFS.log_templates.csv',
}

path_file_name = {
    'path_result': 'results/',
    'label_raw': 'anomaly_labels.csv',
    'label_process': 'labels.csv',
    'log_parser': 'HDFS.log_structured.csv',
    'log_feat_extract': 'log_sequence.csv'
}

# Log format
log_name = 'HDFS'
log_format = {'HDFS': '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>'}

# Log parsing
IPLom_settings = {
    'HDFS': {
        'CT': 0.35,
        'lowerBound': 0.25,
        'regex': [r'blk_(|-)[0-9]+','(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)']
    }
}

# Log anomaly
para = {
    'IM': {
        'path': global_data['path'],  # directory for input data
        'log_seq_file_name': global_data['log_seq_file_name'],  # filename for log sequence data file
        'label_file_name': global_data['label_file_name'],  # filename for label data file
        'epsilon': 2.0,  # threshold for the step of estimating invariant space
        'threshold': 0.98,  # percentage of vector Xj in matrix satisfies the condition that |Xj*Vi|<epsilon
        'scale_list': [1, 2, 3],  # list used to sacle the theta of float into integer
        'stop_invar_num': 3,  # stop if the invariant length is larger than stop_invar_num. None if not given
    },
    'LOG_CLUSTER': {
        'path': global_data['path'],  # directory for input data
        'log_seq_file_name': global_data['log_seq_file_name'],  # filename for log sequence data file
        'label_file_name': global_data['label_file_name'],  # filename for label data file
        'train_base_per': 0.6,
        'train_online_per': 0.2,
        'max_d': 0.3,  # the threshold for cutoff the cluster process
        'repre_threshold': 0.2,
        'fail_threshold': 0.1,
        'succ_threshold': 0.99,
    },
    'PCA': {
        'path': global_data['path'],  # directory for input data
        'log_seq_file_name': global_data['log_seq_file_name'],  # filename for log sequence data file
        'label_file_name': global_data['label_file_name'],  # filename for label data file
        'train_base_per': 0.6,
        'fraction': 0.95,
        'tf-idf': True,
    }
}