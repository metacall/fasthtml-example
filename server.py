import uvicorn
from multiprocessing import Process
import time

try:
    def main():
        uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")
    proc = Process(target=main, args=(), daemon=True)
    proc.start()
    print('Process launched')
    time.sleep(5)
except Exception as e:
    print(e)
