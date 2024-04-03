import asyncio

# try:
from GUI import AsyncWindow
from EncryptionManagement import make_private_key

if __name__ == "__main__":
    make_private_key()
    loop = asyncio.get_event_loop()
    app = AsyncWindow(loop)
    loop.run_forever()
    loop.close()
# except Exception as e:
#     print(e.with_traceback(None))
#     print(__file__.replace("\\", "/")[:__file__.replace("\\", "/").rindex("/")])
#     input("Press enter to continue...")
