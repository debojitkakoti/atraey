from errbot import BotPlugin, botcmd
from jenkinsapi.jenkins import Jenkins


from config import JENKINS_URL, JENKINS_USERNAME, JENKINS_PASSWORD

class Jenkinsbot(BotPlugin):
    def connect_server(self):
        server = Jenkins(JENKINS_URL, JENKINS_USERNAME, JENKINS_PASSWORD)
        return server

    @botcmd
    def get_jenkins_version(self, mess, args):
        return self.connect_server().version

    @botcmd
    def get_running_jobs(self, mess, args):
        jobs = self.connect_server().get_jobs()
        self.log.debug(jobs)
        if jobs is None:
            return "No running job!"
        job_list = " "
        for job_name, job_instance in jobs:
             job_list += " *Job Name: " + job_instance.name + " Job Description: " + job_instance.get_description() + " Is Job running:"+ str(job_instance.is_running()) + " Is Job enabled:"+ str(job_instance.is_enabled()) +"*\n\n"
        self.send_card(title='Current Jenkins Job Details',
                       body=job_list,
                       color='green',
                       in_reply_to=mess)
 
    @botcmd
    def get_jenkins_plugins(self, mess, args):
        plugin_list = ""
        for plugin in self.connect_server().get_plugins().values():
             plugin_list +=" Short Name:" + plugin.shortName + " Long Name: " + plugin.longName + " Version: " + plugin.version + " URL: " + plugin.url + " Active: " + str(plugin.active) + " Enabled: " + str(plugin.enabled) + "\n\n"
        return plugin_list
    
    @botcmd(split_args_with=None)
    def start_build(self, mess, args):
        jobname = args.pop(0)
        params = dict([(k, v) for k,v in zip (args[::2], args[1::2])])

        self.connect_server().build_job(jobname, params)
        return "Build Triggered!"