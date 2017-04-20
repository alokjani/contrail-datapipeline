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
import logging

from pprint import pprint
from oslo_config import cfg

LOG = logging.getLogger(__name__)

class FlowSender:
   
    def __init__(self):
        LOG.info('Initializing FlowSender Class')
        
    def makePost(self, target_http_server, flow_sample):
        """ Posts are made to an external HTTP Receiver
        Args:
          target_http_server(string): The HTTP Service that will receive the FlowSample
          flow_sample(string): Json encoded string containing details of a collection of Contrail flows
          
        """

        try:
            LOG.info('Sending Flow Sample to `%s`', target_http_server)
            response = requests.post(target_http_server, data=json.dumps(flow_sample))
            LOG.info('Delivery Success.')
        except requests.exceptions.Timeout as e:
            LOG.error(str(e))
            # Insert retry logic
        except requests.exceptions.ConnectionError as e:
            LOG.error(str(e))
            # Insert retry logic
        except requests.exceptions.HTTPError as e:
            LOG.error(str(e))
            # this is rare
        except requests.exceptions.RequestException as e:
            LOG.error(str(e))

