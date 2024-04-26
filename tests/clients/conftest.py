import httpx


class HTTPXAsyncClientMock(httpx.AsyncClient):
    def __init__(self, response=None, error: Exception = None):
        self.response = response
        self.error = error
        super().__init__()

    async def request(self, *args, **kwargs):
        if self.error:
            raise self.error  # pragma: nocover

        return self.response
