import asyncio
from threading import Thread
import uvicorn
from main import main
import atexit

try:
    def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
        asyncio.set_event_loop(loop)
        loop.run_forever()

    loop = asyncio.new_event_loop()
    t = Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()

    task = asyncio.run_coroutine_threadsafe(main(), loop)

    def exit_handler():
        loop.stop()

    atexit.register(exit_handler)
except KeyboardInterrupt:
    pass
except Exception as e:
    print('An exception occurred: {}'.format(e))
