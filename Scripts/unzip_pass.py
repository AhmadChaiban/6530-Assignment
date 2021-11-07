from glob import glob as globlin
from zipfile import ZipFile
from tqdm import tqdm

paths = globlin("./*.zip")

for path in tqdm(paths):
    with ZipFile(path) as zf:
        zf.extractall(pwd=b'infected')
