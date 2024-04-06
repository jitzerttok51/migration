import os
import xml.etree.ElementTree as ET
import codecs

def getLyrics(file: str) -> str:
    tree = ET.parse(file)
    root = tree.getroot()
    lyrics_tags = root.findall(".//lyrics")
    for lyrics_tag in lyrics_tags:
        return lyrics_tag.text
    
def cleanLyrics(raw: str) -> str:
    text = ''
    for line in raw.split('\n'):
        if line.startswith('.') or line.startswith('['):
            continue
        line = line.replace("_", '')
        line = ' '.join([w.strip() for w in line.split(' ') if len(w.strip()) > 0])
        if len(line) > 1 and line[0].isdigit():
            line = line[1:]
        text += line + '\n'

    # print(text)
    return text

def saveSong(filename: str, outputDir: str, content: str) -> None:
    dest = os.path.join(outputDir, f'{filename}.txt')
    with codecs.open(dest, 'w', "utf-8") as f:
        f.write(content)

inputDir = 'input'
files = {f: os.path.join(inputDir, f) for f in os.listdir('input') }
lyrics = {f: getLyrics(files[f]) for f in files}
cleanedLyrics = {f: cleanLyrics(lyrics[f]) for f in lyrics}
[saveSong(f, 'output', cleanedLyrics[f]) for f in cleanedLyrics]

