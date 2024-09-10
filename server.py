import asyncio
import uvicorn

try:
    config = uvicorn.Config("main:app", host="0.0.0.0", port=5000, log_level="info")
    server = uvicorn.Server(config)
    asyncio.run(server.serve())
except KeyboardInterrupt:
    pass
except Exception as e:
    print('An exception occurred: {}'.format(e))
