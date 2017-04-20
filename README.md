# Contrail Data Pipeline 

Pipeline for moving data between Contrail Analytics and On-premise collectors, log aggregators, analyzers etc. 

Currently is supports exporting of Contrail Flows in HTTP format.

# Install

```  
  ❯ sudo apt install python-requests python-oslo-config python-setuptools
  ❯ git clone https://github.com/alokjani/contrail-datapipeline
  ❯ cd contrail-datapipeline/
  ❯ sudo python setup.py install
```

Tested with Ubuntu 16.04

# Configure & Run

Sample configuration file is at `contrail-datapipeline.conf.sample`.

```
  ❯ cp contrail-datapipeline.conf.sample /etc/contrail-datapipeline.conf
```

Execute

```
  ❯ contrail-datapipeline /etc/contrail-datapipeline.conf
	INFO     2017-04-20 12:40:09 [contrail_datapipeline.FlowCollector; FlowCollector.py:32] Initlizaing FlowCollector Class
	INFO     2017-04-20 12:40:09 [contrail_datapipeline.FlowCollector; FlowCollector.py:62] Retrieving Flow stats from Contrail `http://127.0.0.1:8081/analytics/query`
	INFO     2017-04-20 12:40:09 [contrail_datapipeline.FlowCollector; FlowCollector.py:64] Retrieval Complete.
	INFO     2017-04-20 12:40:09 [contrail_datapipeline.FlowSender; FlowSender.py:30] Initializing FlowSender Class
	INFO     2017-04-20 12:40:09 [contrail_datapipeline.FlowSender; FlowSender.py:41] Sending Flow Sample to `http://127.0.0.1:9090/rest`
	INFO     2017-04-20 12:40:09 [contrail_datapipeline.FlowSender; FlowSender.py:43] Delivery Success.
  ❯
```

# Author

Alok Jani S.
