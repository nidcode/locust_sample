from locust import HttpUser, TaskSet, task, between

class SimpleHttpTask(HttpUser):
    @task
    def get_index(self):
        self.client.get("/", name="index")
