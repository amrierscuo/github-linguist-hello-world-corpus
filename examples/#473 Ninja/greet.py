from pathlib import Path
Path('greeting.txt').write_text('Hello, ' + 'World!', encoding='ascii')
