#    Copyright 2017 Reliance Jio Infocomm, Ltd.
#    Author: Alok Jani <Alok.Jani@ril.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# -----------------------------------------------------------

import sys
import fcntl
import json
import urllib2
import time
import logging

from oslo_config import cfg

from FlowCollector import FlowCollector
from FlowSender import FlowSender


CONF = cfg.CONF
LOG = logging.getLogger(__name__)


def init_logging():
    formatter = logging.Formatter(
        fmt='%(levelname)-8s %(asctime)s '\
            '[%(name)s; %(filename)s:%(lineno)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    root_logger = logging.getLogger()

    if CONF.DEFAULT.debug is True:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(logging.INFO)

    for handler in (logging.FileHandler(CONF.DEFAULT.log_file),
                    logging.StreamHandler()):
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)
        root_logger.addHandler(handler)

    # reduce logging from requests library
    logging.getLogger("requests").setLevel(logging.WARNING)


def init_config(conf_files):
    CONF.register_opts([
        cfg.StrOpt('log_file', 
            required=True, 
            help='local path to log file')
    ], 'DEFAULT')

    CONF.register_opts([
        cfg.BoolOpt('debug',
            required=True,
            help='set debug level')
    ], 'DEFAULT')

    CONF.register_opts([
        cfg.StrOpt('query_start_time', 
            required=True, 
            help='Specify the minutes from now back in time')
    ], 'contrail')    

    CONF.register_opts([
        cfg.StrOpt('analytics_api', 
            required=True, 
            help='Contrail Analytics Query URL')
    ], 'contrail')    

    CONF.register_opts([
        cfg.StrOpt('http_receiver', 
            required=True, 
            help='SIEM HTTP Server')
    ], 'log_aggregator')
 
    conf_file = [conf_files[0] if conf_files else 'contrail_export.conf']
    
    CONF(default_config_files=conf_file, args='')
    
    CONF.log_opt_values(LOG, logging.DEBUG)

def main():

    if (len(sys.argv) != 2):
        print "contrail-datapipeline accepts exactly 1 argument"
        sys.exit(1)

    init_config(sys.argv[1:])

    init_logging()
    
    a = FlowCollector(CONF.contrail.analytics_api)
    a.getContrailFlowStats(CONF.contrail.query_start_time)
    
    b = FlowSender()
    b.makePost(CONF.log_aggregator.http_receiver, a.flow_sample)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

