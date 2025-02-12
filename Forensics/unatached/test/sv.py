import re
import os
import zlib
import hashlib

def write_file(path, content):
    with open(path, 'wb') as f:
        f.write(content)

pattern = re.compile(b'\/Type \/EmbeddedFile.+?stream\n(.+?)\nendstream', flags=re.S)
content = open('about-git.pdf', 'rb').read()
matches = pattern.findall(content)
decompressed_stream = [zlib.decompress(m) for m in matches]

# Re-build git objects hierarcy
if not os.path.exists('flag'):
    os.system('git init flag')

os.chdir('flag/.git')
for stream in decompressed_stream:
    if stream.startswith(b'DIRC'):
        write_file('index', stream)
    elif stream.startswith(b'x\x01'):
        s = zlib.decompress(stream)
        h = hashlib.sha1(s).hexdigest()

        try:
            os.mkdir(f'objects/{h[:2]}')
        except:
            pass
        finally:
            write_file(f'objects/{h[:2]}/{h[2:]}', stream)

    elif re.match(rb'^[a-f0-9]+$', stream):
        write_file('refs/heads/main', stream)

# Iterate over git-commit
os.chdir('..')
os.system("git log --oneline | awk '{print $1}' | xargs -I{} bash -c 'git diff {}' | grep -oP '(?<=-).$' | tac | paste -sd ''")