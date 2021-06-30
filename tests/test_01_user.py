def test_create_user(app, client):
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

    result = client.execute(query)
    assert app is not None
    assert result["data"]["createUser"]["id"] == 1
    assert result["data"]["createUser"]["name"] == "Test User"


def test_get_user_list(client, user):
    query = """
    query {
        getUsers {
            name
            address
        }
    }
    """

    result = client.execute(query)
    assert type(result["data"]["getUsers"]) == list


def test_get_single_user(client, user):
    query = (
        """
    query {
        getUser(userId: %s){
            address
        }
    }
    """
        % user.id
    )
    result = client.execute(query)

    assert result["data"]["getUser"] is not None
    assert result["data"]["getUser"]["address"] == user.address
