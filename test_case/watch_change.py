import os
import time
from watchdog.events import *
from watchdog.observers import Observer
from pathlib import Path


current_folder = Path(__file__).absolute().parent


class MyHandler(FileSystemEventHandler):

    def parse_filename(self, event_file):
        return os.path.basename(event_file)

    def on_any_event(self, event):
        return super().on_any_event(event)

    def on_modified(self, event):
        event_file = event.src_path
        changed_file = self.parse_filename(event_file)
        print("file changed %s" % changed_file)
        if changed_file.startswith("test") and changed_file.endswith(".py"):
            # 调用Linux的开门狗，实时监测，在改变代码时save以后，重新运行，配合pytest使用
            cmd = f"pytest -s {event_file}"
            print(cmd)
            os.system(cmd)

    def on_created(self, event):
        print("file created %s" % event.src_path)


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, current_folder, recursive=True)
    print(f"监控目录 {current_folder}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Python中，仅在每个进程的主线程中引发KeyboardInterrupt异常
        observer.stop()
    observer.join()
