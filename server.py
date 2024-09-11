
import asyncio
import uvicorn

async def main():
    print('Startup the uvicorn server', flush=True)
    config = uvicorn.Config('main:app', host='0.0.0.0', port=5000, log_level='info')
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        exit(0)
