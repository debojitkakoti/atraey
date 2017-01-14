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
        for job_name, job_instance in self.connect_server().get_jobs():
            self.log.debug(job_instance.name)
            return job_instance.name
