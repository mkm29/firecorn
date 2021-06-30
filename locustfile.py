from locust import HttpUser, task, between

from src.db import db
from src.models.comment import Comments
from src.models.post import Post
from src.models.user import User


class FirecornUserTest(HttpUser):

    """
    Refers to the wait time between the execution of task.
    For load testing this should be 0.0

    Refer to other built-ins: https://docs.locust.io/en/stable/api.html#module-locust.wait_time
    """

    wait_time = between(0.5, 3.0)

    def _create_user(self):
        user = User()
        user.name = "John Doe"
        user.address = "United States of Nigeria"
        user.phone_number = 123456789
        user.sex = "male"
        user.save()

        return user

    def _create_post(self, user):
        post = Post()
        post.title = "Test Title"
        post.body = "this is the post body and can be as long as possible"

        user.posts().save(post)

        return post

    def _create_comment(self, user, post):
        comment = Comments()
        comment.body = "This is a comment body"

        user.comments().save(comment)
        post.comments().save(comment)

        return comment

    def on_start(self):
        """on_start is called when a Locust start before any task is scheduled"""

        # Create a User
        user = self._create_user()

        # Create a Post
        post = self._create_post(user=user)
        db.disconnect()

    def on_stop(self):
        """on_stop is called when the TaskSet is stopping"""

        pass
        # # Remove all records from database
        # for table in ("comments", "users", "posts"):
        #     db.table(table).delete()

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
            headers={
                "Accept": "application/graphql",
            },
            json={"query": mutation},
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
            headers={
                "Accept": "application/graphql",
            },
            json={"query": query},
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
            headers={
                "Accept": "application/graphql",
            },
            json={"query": mutation},
        )

    @task(2)
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
            headers={
                "Accept": "application/graphql",
            },
            json={"query": query},
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

    @task(2)
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
            headers={
                "Accept": "application/graphql",
            },
            json={"query": query},
        )
