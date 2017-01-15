from errbot import BotPlugin, botcmd
from elasticsearch import Elasticsearch
import plotly.plotly as py
import plotly.graph_objs as go
import random

from config import ES_HOST, METRIC_INDEX

class Metricsbot(BotPlugin):
    def es_request_metric(self, metric_value):
        res = es.search(index=METRIC_INDEX, body={
    		"query": {
        		"bool":{
            "must":{
                "range" : {
                    "@timestamp" : {
                        "gte" : "now-1h"
                    }
                }
            },
            "filter": {
                "exists": {
                    "field": metric_value
                }
            }
        }
    },
    "_source" : [metric_value,"@timestamp"],
    "size":100,
    "sort" : [
        {
            "@timestamp" : {"order" : "asc"}
        }
    ]
})
        return res

    def random_alphanumeric(limit):
        #ascii alphabet of all alphanumerals
        r = (range(48, 58) + range(65, 91) + range(97, 123))
        random.shuffle(r)
        return reduce(lambda i, s: i + chr(s), r[:random.randint(0, len(r))], "")

    @botcmd
    def get_metric_apache_cpu_load(self, mess, args):
        res = self.es_request_metric('apache.status.cpu.load')
        
        if not res['hits']['hits']:
            x-data = []
            y-data = []
            for hit in res['hits']['hits']
                x-data.append(hit['_source']['@timestamp'])
                y-data.append(hit['_source']['apache']['status']['cpu']['load'])
            
            fig = {'data': [{'x': x-data, 'y': y-data, 'type': 'line'}]}
            img_name = "apache_status_cpu_load_" + self.random_alphanumeric(6) 
            py.image.save_as(fig, '/var/www/html/' + img_name, scale = 3)
            return HOST_URL + '/' + img_name
            return self.connect_server().version
       else:
            return "Oops no enough data to measure apache cpu load"

    @botcmd
    def get_running_jobs(self, mess, args):
        jobs = self.connect_server().get_jobs
        if jobs is None:
            return "No running job!"
        job_list = " "
        for job_name, job_instance in jobs:
             job_list += job_instance.name
        return job_list
 
    @botcmd
    def get_jenkins_plugins(self, mess, args):
        return self.connect_server().get_plugins_info
