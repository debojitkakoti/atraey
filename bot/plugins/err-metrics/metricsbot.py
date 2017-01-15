from errbot import BotPlugin, botcmd
from elasticsearch import Elasticsearch 
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot
import random
import uuid
import json
from plotly.offline import init_notebook_mode, plot_mpl
from config import ES_HOST, METRIC_INDEX, HOST_URL

class Metricsbot(BotPlugin):
    def es_request_metric(self, metric_value):
        es = Elasticsearch(ES_HOST)
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

    def random_alphanumeric(self,limit):
        #ascii alphabet of all alphanumerals
        r = (range(48, 58) + range(65, 91) + range(97, 123))
        random.shuffle(r)
        return reduce(lambda i, s: i + chr(s), r[:random.randint(0, len(r))], "")

    @botcmd
    def get_metric_apache_cpu_load(self, mess, args):
        res = self.es_request_metric('apache.status.cpu.load')
        
        if  res['hits']['hits']:
            xdata =  list();
            ydata =  list();
            for hit in res['hits']['hits']:
                xdata.append(hit['_source']['@timestamp'])
                ydata.append(hit['_source']['apache']['status']['cpu']['load']) 
            img_name = "apache_status_cpu_load_" + str(uuid.uuid4())+".html"
            plot([go.Scatter(x=xdata, y=ydata)], filename='/var/www/html/'+img_name,image='jpeg')
            return 'Click below link for metric data\n' + HOST_URL + '/' + img_name
        else:
            return "Oops no enough data to measure apache cpu load"
        
    @botcmd
    def get_metric_apache_status_kb(self, mess, args):
        res = self.es_request_metric('apache.status.total_kbytes')
        
        if  res['hits']['hits']:
            xdata =  list();
            ydata =  list();
            for hit in res['hits']['hits']:
                xdata.append(hit['_source']['@timestamp'])
                ydata.append(hit['_source']['apache']['status']['total_kbytes'])
            img_name = "apache_status_kb_" + str(uuid.uuid4())+".html"
            plot([go.Scatter(x=xdata, y=ydata)], filename='/var/www/html/'+img_name,image='jpeg')
            return 'Click below link for metric data\n' + HOST_URL + '/' + img_name
        else:
            return "Oops no enough data to measure apache status kbytes served"
        
    @botcmd
    def get_metric_apache_status_accesses(self, mess, args):
        res = self.es_request_metric('apache.status.total_accesses')
        
        if  res['hits']['hits']:
            xdata =  list();
            ydata =  list();
            for hit in res['hits']['hits']:
                xdata.append(hit['_source']['@timestamp'])
                ydata.append(hit['_source']['apache']['status']['total_accesses'])
            img_name = "apache_status_accesses_" + str(uuid.uuid4())+".html"
            plot([go.Scatter(x=xdata, y=ydata)], filename='/var/www/html/'+img_name,image='jpeg')
            return 'Click below link for metric data\n' + HOST_URL + '/' + img_name
        else:
            return "Oops no enough data to measure apache status total accesses"
