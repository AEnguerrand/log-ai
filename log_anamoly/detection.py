import config
from loglizer.models import mining_invariants as mi
from loglizer.models import log_clustering as cluster
from loglizer.models import PCA as PCA
from loglizer.utils import data_loader
from datetime import datetime

def run_im():
    starttime = datetime.now()
    raw_data, label_data = data_loader.hdfs_data_loader(config.para['IM'])
    r = mi.estimate_invar_spce(config.para['IM'], raw_data)
    invar_dict = mi.invariant_search(config.para['IM'], raw_data, r)
    mi.evaluate(raw_data, invar_dict, label_data)
    print("[IM][RUNTIME]: ", datetime.now() - starttime)


def run_pca():
    starttime = datetime.now()
    raw_data, label_data = data_loader.hdfs_data_loader(config.para['PCA'])
    weigh_data = PCA.weighting(config.para['PCA'], raw_data)
    threshold, C = PCA.get_threshold(config.para['PCA'], weigh_data)
    PCA.anomaly_detection(weigh_data, label_data, C, threshold)
    print("[PCA][RUNTIME]: ", datetime.now() - starttime)


def run_log_cluster():
    starttime = datetime.now()
    raw_data, label_data = data_loader.hdfs_data_loader(config.para['LOG_CLUSTER'])
    weighted_matrix, total_inst_num = cluster.weighting(raw_data)
    succ_index_list, fail_index_list, train_base_data, train_online_data, testing_data, train_base_label, train_online_label, testing_label = cluster.split_data(
        config.para['LOG_CLUSTER'], weighted_matrix, label_data)
    cluster.anomalyDetect(config.para['LOG_CLUSTER'], succ_index_list, fail_index_list, train_base_data, train_online_data,
                          testing_data,
                          train_online_label, testing_label, total_inst_num)
    print("[LOG CLUSTER][RUNTIME]: ", datetime.now() - starttime)