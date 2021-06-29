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
        mutation = """
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
            json={"query": mutation}
        )

    @task(2)
    def query_users(self):
        query = """
        query {
            getUsers {
                name
                address
            }
        }
        """
        _ = self.client.post(
            "http://localhost:8080/",
            name="GetUsers",
            headers={"Accept": "application/graphql",},
            json={"query": query}
        )

    @task(3)
    def create_post(self):
        mutation = """
        mutation createPost {
        createPost(postDetails: {
            userId: 1,
            title: "My first Post",
            body: "This is a Post about myself"
        })
        {
            id
            body
        }
        }
        """
        _ = self.client.post(
            "http://localhost:8080/",
            name="CreatePost",
            headers={"Accept": "application/graphql",},
            json={"query": mutation}
        )

    @task(4)
    def get_posts(self):
        query = """
        query {
            getPosts {
                id
                body
            }
        }
        """
        _ = self.client.post(
            "http://localhost:8080/",
            name="GetPosts",
            headers={"Accept": "application/graphql",},
            json={"query": query}
        )

    @task(5)
    def create_comment(self):
        mutation = """
        mutation createComment {
            createComment(commentDetails: {
                userId: 1,
                postId: 1,
                body: "Another Comment"
            })
            {
                id
                body
            }
        }
        """
        _ = self.client.post(
            "http://localhost:8080/",
            name="CreateComment",
            headers={"Accept": "application/graphql",},
            json={"query": mutation}
        )

    @task(6)
    def get_comments(self):
        query = """
        query {
            getComments {
                id
                body
            }
        }
        """
        _ = self.client.post(
            "http://localhost:8080/",
            name="GetPosts",
            headers={"Accept": "application/graphql",},
            json={"query": query}
        )