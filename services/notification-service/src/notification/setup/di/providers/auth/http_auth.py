from dishka import Provider, provide, Scope


class HttpAuthProvider(Provider):
    scope = Scope.REQUEST
