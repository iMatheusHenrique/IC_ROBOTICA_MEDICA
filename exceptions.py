class ConnectionFailed(Exception):
    """Exceção para lidar com falhas de conexão."""

    def __init__(self, message="Falha na conexão"):
        self.message = message
        super().__init__(self.message)
