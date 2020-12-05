from typing import Any
import io

BUFFER_SIZE: Any

class BaseStream(io.BufferedIOBase): ...

class DecompressReader(io.RawIOBase):
    def readable(self): ...
    def __init__(self, fp, decomp_factory, trailing_error=..., **decomp_args): ...
    def close(self): ...
    def seekable(self): ...
    def readinto(self, b): ...
    def read(self, size: int = ...) -> bytes: ...
    def seek(self, offset, whence=...): ...
    def tell(self): ...
