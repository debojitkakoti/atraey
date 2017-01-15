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
    
    def es_request_metric_single(self, metric_value):
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
    "size":1,
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
            #return 'Click below link for metric data\n' + HOST_URL + '/' + img_name
            self.send_card(title='Metric Graph link',
                       body='Click below link for metric data\n',
                       link=HOST_URL + '/' + img_name,
                       color='red',
                       in_reply_to=mess)
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
        
    @botcmd
    def get_metric_apache_status_requests(self, mess, args):
        res = self.es_request_metric('apache.status.requests_per_sec')
        
        if  res['hits']['hits']:
            xdata =  list();
            ydata =  list();
            for hit in res['hits']['hits']:
                xdata.append(hit['_source']['@timestamp'])
                ydata.append(hit['_source']['apache']['status']['requests_per_sec'])
            img_name = "apache_status_requests_" + str(uuid.uuid4())+".html"
            plot([go.Scatter(x=xdata, y=ydata)], filename='/var/www/html/'+img_name,image='jpeg')
            return 'Click below link for metric data\n' + HOST_URL + '/' + img_name
        else:
            return "Oops no enough data to measure apache status requests per second"
        
    @botcmd
    def get_metric_apache_status_bps(self, mess, args):
        res = self.es_request_metric('apache.status.bytes_per_sec')
        
        if  res['hits']['hits']:
            xdata =  list();
            ydata =  list();
            for hit in res['hits']['hits']:
                xdata.append(hit['_source']['@timestamp'])
                ydata.append(hit['_source']['apache']['status']['bytes_per_sec'])
            img_name = "apache_status_bps_" + str(uuid.uuid4())+".html"
            plot([go.Scatter(x=xdata, y=ydata)], filename='/var/www/html/'+img_name,image='jpeg')
            return 'Click below link for metric data\n' + HOST_URL + '/' + img_name
        else:
            return "Oops no enough data to measure apache status bytes per second"
        
    @botcmd
    def get_metric_apache_status_bpr(self, mess, args):
        res = self.es_request_metric('apache.status.bytes_per_request')
        
        if  res['hits']['hits']:
            xdata =  list();
            ydata =  list();
            for hit in res['hits']['hits']:
                xdata.append(hit['_source']['@timestamp'])
                ydata.append(hit['_source']['apache']['status']['bytes_per_request'])
            img_name = "apache_status_bpr_" + str(uuid.uuid4())+".html"
            plot([go.Scatter(x=xdata, y=ydata)], filename='/var/www/html/'+img_name,image='jpeg')
            return 'Click below link for metric data\n' + HOST_URL + '/' + img_name
        else:
            return "Oops no enough data to measure apache status bytes per request"

    @botcmd
    def get_metric_apache_status_workers_busy(self, mess, args):
        res = self.es_request_metric_single('apache.status.workers.busy')
        if  res['hits']['hits'][0]:
            return 'Number of workers busy\n' + str(res['hits']['hits'][0]['_source']['apache']['status']['workers']['busy'])
        else:
            return "Oops not enough data to show busy workers"

    @botcmd
    def get_metric_apache_status_workers_idle(self, mess, args):
        res = self.es_request_metric_single('apache.status.workers.idle')
        if  res['hits']['hits'][0]:
            return 'Number of workers idle\n' + str(res['hits']['hits'][0]['_source']['apache']['status']['workers']['idle'])
        else:
            return "Oops not enough data to show idle workers"
        
    @botcmd
    def get_metric_apache_status_cpu_load(self, mess, args):
        res = self.es_request_metric_single('apache.status.cpu.load')
        if  res['hits']['hits'][0]:
            return 'CPU Load \n' + str(res['hits']['hits'][0]['_source']['apache']['status']['cpu']['load'])
        else:
            return "Oops not enough data to show cpu load"
        
    @botcmd
    def get_metric_apache_status_cpu_user(self, mess, args):
        res = self.es_request_metric_single('apache.status.cpu.user')
        if  res['hits']['hits'][0]:
            return 'CPU User \n' + str(res['hits']['hits'][0]['_source']['apache']['status']['cpu']['user'])
        else:
            return "Oops not enough data to show cpu user"
        
    @botcmd
    def get_metric_apache_status_cpu_system(self, mess, args):
        res = self.es_request_metric_single('apache.status.cpu.system')
        if  res['hits']['hits'][0]:
            return 'CPU System \n' + str(res['hits']['hits'][0]['_source']['apache']['status']['cpu']['system'])
        else:
            return "Oops not enough data to show cpu system"
        
    @botcmd
    def get_metric_apache_status_connections(self, mess, args):
        res = self.es_request_metric_single('apache.status.connections.total')
        if  res['hits']['hits'][0]:
            return 'Total Connections \n' + str(res['hits']['hits'][0]['_source']['apache']['status']['connections']['total'])
        else:
            return "Oops not enough data to show total connections"
        
    @botcmd
    def get_metric_apache_status_load(self, mess, args):
        res = self.es_request_metric_single('apache.status.load.5')
        if  res['hits']['hits'][0]:
            return 'Avg Load in last 5 minutes \n' + str(res['hits']['hits'][0]['_source']['apache']['status']['load']['5'])
        else:
            return "Oops not enough data to show avg load"
