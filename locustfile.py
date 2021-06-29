from locust import HttpUser, task, between

class FirecornUserTest(HttpUser):

    """ 
        Refers to the wait time between the execution of task. 
        For load testing this should be 0.0

        Refer to other built-ins: https://docs.locust.io/en/stable/api.html#module-locust.wait_time
    """
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def create_user(self):
        query = """
        mutation {
            createUser(userDetails: {
                name: "Test User",
                sex: "male",
                address: "My Address",
                phoneNumber: "123456789",
            })
            {
                id
                name
                address
            }
        }
        """
        _ = self.client.post(
            "http://localhost:8080/",
            name="CreateUser",
            headers={"Accept": "application/graphql",},
            json={"query": query}
        )