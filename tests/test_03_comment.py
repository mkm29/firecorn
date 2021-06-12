def test_create_comment(client, user, post):
    mutation = """
    mutation createComment {
        createComment(commentDetails: {
            userId: %s,
            postId: %s,
            body: "Another Comment"
        })
        {
            id
            body
        }
    }
    """ % (user.id, post.id)

    result = client.execute(mutation)
    assert result['data']['createComment']['id'] == 1
    assert result['data']['createComment']['body'] == "Another Comment"

def test_get_comments(client):
    query = """
    query {
        getComments {
            id
            body
        }
    }
    """

    result = client.execute(query)
    assert type(result['data']['getComments']) == list


def test_get_comment(client, comment):
    query = """
    query {
        getComment(commentId: %s){
            body
        }
    }
    """ % comment.id
    result = client.execute(query)

    assert result['data']['getComment'] is not None
    assert result['data']['getComment']['body'] == comment.body