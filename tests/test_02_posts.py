def test_create_post(client, user):
    mutation = """
    mutation createPost {
    createPost(postDetails: {
        userId: %s,
        title: "My first Post",
        body: "This is a Post about myself"
    })
    {
        id
        body
    }
    }
    """ % user.id

    result = client.execute(mutation)
    assert result['data']['createPost']['id'] == 1
    assert result['data']['createPost']['body'] == "This is a Post about myself"

def test_get_posts(client):
    query = """
    query {
        getPosts {
            id
            body
        }
    }
    """

    result = client.execute(query)
    assert type(result['data']['getPosts']) == list


def test_get_post(client, post):
    query = """
    query {
        getPost(postId: %s){
            body
        }
    }
    """ % post.id
    result = client.execute(query)

    assert result['data']['getPost'] is not None
    assert result['data']['getPost']['body'] == post.body