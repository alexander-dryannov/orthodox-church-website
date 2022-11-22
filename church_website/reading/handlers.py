import json
from pathlib import Path
from django.core.files import temp as tempfile
from django.core.files.storage import FileSystemStorage


def read_file(file) -> list:
    book = FileSystemStorage(location="/tmp").save(file.name, file)
    path_to_temp_file = Path(tempfile.gettempdir()).joinpath(book)
    with open(path_to_temp_file, 'r', errors='ignore') as txt:
        lst = [line.strip() for line in txt.readlines()]
    return lst


def convert_txt_to_dict(file):
    list_strings = read_file(file)
    data = {'book_title': '', 'body': []}
    ranges = list()
    chapter_position = list()
    data['book_title'] = list_strings.pop(0)

    for idx, p in enumerate(list_strings):
        if p.isdigit():
            chapter_position.append(idx)

    for idx, i in enumerate(chapter_position):
        try:
            ranges.append((i, chapter_position[idx+1]))
        except IndexError:
            ranges.append((i, -1))

    for range in ranges:
        chapter = dict()
        start, stop = range
        ch = list_strings[start:stop]
        title_chapter = ch.pop(0)
        # body = [string for string in ch if string]
        body = list()
        for string in ch:
            if string:
                string = string.split()
                num = string.pop(0)
                txt = ' '.join(string)
                string = f'<p><b class="num">{num}</b> {txt}</p>'
                body.append(string)
        chapter[title_chapter] = body
        data['body'].append(chapter)
    return data
