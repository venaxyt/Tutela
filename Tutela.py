from psutil import process_iter

def tutela():
    while True:
        for process in process_iter():
            if "fiddler" in process.name().lower() or "hack" in process.name() or "x32dbg" in process.name() or "x64dbg" in process.name() or "x96dbg" in process.name() or "IDA" in process.name() or "toolkit" in process.name().lower():
                process.kill()
        time.sleep(0.15)

threading.Thread(target=tutela).start()  # You can kill the thread with signal

# Here you have to put your script and the requests listeners in the list will be killed
