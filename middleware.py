class AuthenticationMiddleware:
    def __init__(self, app: ASGIApp, user_model: type) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope['type'] in ('http', 'websocket'):
            scope['user'] = await self.get_user(scope)
        await self.app(scope, receive, send)

    async def get_user(self, scope):
        assert 'session' in scope, ('Enable SessionMiddleware before AuthenticationMiddleware')
        session = scope['session']
        return await user_model.objects.get(session['user_id'])
