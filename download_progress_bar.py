from tqdm import tqdm
import requests

chunk_size = 1024

url = 'https://file-examples.com/wp-content/uploads/2017/11/file_example_MP3_5MG.mp3'

r = requests.get(url, stream=True)
print(r.headers)
total_size = int(r.headers['content-length'])
print(f'File size in MB: {total_size/chunk_size}')
filename = url.split('/')[-1]

with open(filename, 'wb') as f:
	for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size/chunk_size, unit='KB'):
		f.write(data)


print(f"Download {r.headers['Content-Type'].split('/')[-1]} file complete!")
