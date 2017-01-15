# Atraey Bot - ChatOps for Team

Project Atraey Bot is a collaborative chatOps service for CI/CD,code repo management and infrastructure monitoring to increase ops team productivity. 

![logo](https://raw.githubusercontent.com/debojitkakoti/atraey/master/atraey-logo.png)

# Usage

## Jenkinsbot

   This is Atraey Bot plugin for jenkins management.
   
- !get_jenkins_plugins - 
- !get_running_jobs - 
- !start_build - 
- !get_jenkins_version - 

## Metricsbot

This is Atraey Bot plugin for log explorer 

- !get_metric_apache_status_workers_idle - Return Number of workers idle
- !get_metric_apache_status_bps - Return status/metric graph link regarding byte per second
- !get_metric_apache_status_cpu_load -Return apache cpu load status
- !get_metric_apache_status_load - Return Avg Load in last 5 minutes
- !get_metric_apache_status_requests - Return request per second status graph
- !get_metric_apache_status_kb - Historical graph regarding Total KB served since start
- !get_metric_apache_status_accesses - Graph over time fo total number of access requests.
- !get_metric_apache_status_cpu_user - cpu user load
- !get_metric_apache_status_connections - Number connetion at any particular time
- !get_metric_apache_status_workers_busy - number of worker busy
- !get_metric_apache_status_bpr -graph for byte per request data
- !get_metric_apache_cpu_load - cpu load historical chart over time
- !get_metric_apache_status_cpu_system - system cpu usage data
