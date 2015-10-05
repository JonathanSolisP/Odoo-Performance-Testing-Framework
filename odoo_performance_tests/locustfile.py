import xmlrpclib
from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):

    @task
    def my_task(self):
        print "Locust instance (%r) executing my_task" % self


class MyLocust(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
    host = 'http://172.24.28.24:8069'

"""class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000"""

