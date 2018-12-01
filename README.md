# log-ai
Parse, extract and analyse raw log with AI. Demo repository on example Hadoop Distributed File System log.


## Dependencies

- Python 3.6 >=

## Usage

### Install requirements
```bash
pip install -r requirements.txt
```
### Run
```bash
python3 run.py
```
___
## Work related use

This demo is based on two toolkits:
- [logpai/logparser](https://github.com/logpai/logparser/tree/dev)
- [logpai/loglizer](https://github.com/logpai/loglizer)

_logparser_ is a toolkit with a list of algorithms for log parsing. And _loglizer_ is another toolkit with a list of algorithms for anomaly detection.

Dataset (rawlog and labeles use for demonstration is based on [logpai/loghub](https://github.com/logpai/loghub) and [SOSP 2009 Log Dataset](http://iiis.tsinghua.edu.cn/~weixu/sospdata.html). 
