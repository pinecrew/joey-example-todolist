def login(scope, user):
    """
    Persist a user id and a backend in the request. This way a user doesn't
    have to reauthenticate on every request. Note that data set during
    the anonymous session is retained when the user logs in.
    """
    if 'session' in scope and isinstance(scope['session'], dict):
        scope['session']['user_id'] = user.id

def logout(scope):
    """
    Remove the authenticated user's ID from the request and flush their session
    data.
    """
    if 'session' in scope and 'user_id' in scope['session']:
        del scope['session']['user_id']
