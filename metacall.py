import asyncio
from threading import Thread, Event

try:
    from server import main

    print('Running uvicorn in a background thread', flush=True)

    loop_started_event = Event()

    def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
        asyncio.set_event_loop(loop)
        loop_started_event.set()
        loop.run_forever()

    loop = asyncio.new_event_loop()
    t = Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()

    loop_started_event.wait()
    loop.call_soon_threadsafe(asyncio.create_task, main())

except KeyboardInterrupt:
    pass
except Exception as e:
    print('An exception occurred: {}'.format(e), flush=True)
