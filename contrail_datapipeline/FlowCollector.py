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

import requests
import json
from pprint import pprint
import logging

LOG = logging.getLogger(__name__)

class FlowCollector:
    """
    FlowCollector: Singleton class
    
    """
    
    def __init__(self,contrail_analytics_url):
        LOG.info('Initlizaing FlowCollector Class')
        self.contrail_analytics_url = contrail_analytics_url
        self.flow_sample = None 
        
    def getContrailFlowStats(self,query_start_time):
        url = self.contrail_analytics_url.strip('"') 

        headers = { 'Content-Type': 'application/json' }

        data = {
	        "table": "FlowRecordTable",
                "start_time" : query_start_time,
	        "end_time": "now",
	        "select_fields":
		        ["vrouter",
			        "sourcevn", 
			        "sourceip",
			        "sport",
			        "destvn",
			        "destip",
			        "dport",
			        "protocol",
			        "agg-packets",
			        "action", 
			        "setup_time", 
			        "teardown_time" ]
        }


        try:
            LOG.info('Retrieving Flow stats from Contrail `%s`', url)
            response = requests.post(url=url, data=json.dumps(data), headers=headers)
            LOG.info('Retrieval Complete.')
        except requests.exceptions.RequestException as e:
            LOG.error(str(e))
            LOG.error('Contrail Data Pipeline exiting')
            system.exit(1)


        #if pipeline.CONF.DEFAULT.debug is True:
        #    pprint(response.text)

        json_response = json.loads(response.text)

        filtered_response = [] 
        for i in json_response['value']:
            flow_sample = {}
            flow_sample['action']        = i['action']
            flow_sample['destip']        = i['destip']
            flow_sample['dport']         = i['dport']
            flow_sample['sourceip']      = i['sourceip']
            flow_sample['sport']         = i['sport']
            flow_sample['setup_time']    = i['setup_time']
            flow_sample['teardown_time'] = i['teardown_time']
            flow_sample['protocol']      = i['protocol']

            #if pipeline.CONF.DEFAULT.debug is True:
            #    pprint(flow_sample)

            filtered_response.append(flow_sample)

        #if pipeline.CONF.DEFAULT.debug is True:
        #    print 'Dumping Filtered Response ...'
        #    pprint(filtered_response)

        self.flow_sample = filtered_response 

        return self.flow_sample


