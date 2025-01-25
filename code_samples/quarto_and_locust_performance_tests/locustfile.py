from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Wait between 1 and 5 seconds

    @task
    def click_link(self):
        links = ["/", "/bundle-1/", "/destination", "/public-bundle"]
        link = random.choice(links)
        self.client.get(link)