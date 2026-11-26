from dishka import Provider, provide, Scope


class BrokerAuthProvider(Provider):
    scope = Scope.REQUEST
