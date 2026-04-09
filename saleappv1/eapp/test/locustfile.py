from locust import HttpUser, task, between, wait_time

class MyUser(HttpUser):
    wait_time = between(1, 5)  # thời gian nghỉ giữa các request

    @task(2)
    def get_courses(self):
        self.client.get("/courses/")

    @task(1)
    def get_lessons(self):
        self.client.get("/courses/1/lessons/")

