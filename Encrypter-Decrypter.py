import asyncio
from GUI import AsyncWindow
from EncryptionManagement import make_private_key

if __name__ == "__main__":
    make_private_key()
    loop = asyncio.get_event_loop()
    app = AsyncWindow(loop)
    loop.run_forever()
    loop.close()
