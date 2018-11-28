# ai-log
Parse, extract and analyse raw log with AI. Demo repository on example Hadoop Distributed File System log (Available [here](https://github.com/logpai/loghub/tree/master/HDFS))

## Dependencies

- Python >= 3.6

This demo is based on two toolkits:
- [logpai/logparser](https://github.com/logpai/logparser/tree/dev)
- [logpai/loglizer](https://github.com/logpai/loglizer)

_logparser_ is a toolkit with a list of algorithms for log parsing. And _loglizer_ is another toolkit with a list of algorithms for anomaly detection.

## Usage

### Install requirements
```bash
pip install -r requirements.txt
```
### Run
```bash
python3 run
