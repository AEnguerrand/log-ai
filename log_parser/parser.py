import config
from logparser.logparser import IPLoM
from datetime import datetime


def run_iplom(input_dir, log_file, log_format, logID):
    runtime = []
    output_dir = config.global_data['path_result_log_parsing_dir']

    starttime = datetime.now()

    parser = IPLoM.LogParser(log_format=log_format, indir=input_dir, outdir=output_dir,
                             CT=IPLom_settings[logID]['CT'],
                             lowerBound=config.IPLom_settings[logID]['lowerBound'],
                             rex=config.IPLom_settings[logID]['regex'])
    parser.parse(log_file)
    runtime.append(datetime.now() - starttime)

    print("Runtime: ", runtime[0])

    return runtime


def start():
    logID = config.log_name
    log_format = config.log_format
    log_name = logID
    runtime = run_iplom(input_dir='logs/' + logID + '/', log_file=log_name + '.log',
                        log_format=log_format[logID], logID=logID)
