__author__ = 'Proyecto'

from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        self.client.post("/login", {"username": "admin", "password": "admin"})

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000

