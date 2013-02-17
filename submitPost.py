#!/usr/bin/python
import requests
import re
#file_path = raw_input('Filename?')
file_path = 'test.md'
blog_file = open(file_path)
blog_text = blog_file.read()

title_pattern = '=+\n'
tags_pattern = '[Tt]ags:(.*)\n'
title_end = re.search(title_pattern, blog_text).start()
body_start = re.search(title_pattern, blog_text).end()

body_end = re.search(tags_pattern, blog_text).start()

title = blog_text[:title_end].strip()
#print title

body = blog_text[body_start:body_end].strip()
#print body

meta_data = blog_text[body_end:]

tags = re.search(tags_pattern, meta_data).groups()[0].split(",")
published = True if re.search('published', meta_data) else False
promoted = True if re.search('promoted', meta_data) else False

blog_data = {
    'body': body,
    'title':title,
    'promoted':promoted,
    'published':published,
    'tags':tags
}


response = requests.post('http://codegur.us/api/posts/', auth=('jake', '4ecr3fra'), data=blog_data)
#response = requests.get('http://codegur.us/api/posts/')
print response