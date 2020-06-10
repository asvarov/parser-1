from pathlib import Path
from datetime import datetime

f = Path('file_example_MP3_5MG.mp3')
print(f.stat())
tf = f.stat().st_mtime
print(datetime.fromtimestamp(tf).isoformat())