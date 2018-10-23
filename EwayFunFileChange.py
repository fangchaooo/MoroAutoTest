import re
import os


class SdkFileChange():
    def __init__(self):
        pass

    def insert_line_to_file(self, path, line, code):
        fp = open(path)
        s = fp.read()
        fp.close()
        a = s.split('\n')
        a.insert(line, code)
        s = '\n'.join(a)
        fp = open(path, 'w')
        fp.write(s)
        fp.close()

    @staticmethod
    def append_to_file(path, code):
        with open(path, 'a+') as f:
            f.write(code)

    def search_insert_line_to_file(self, path, mark, code):
        fp = open(path)
        s = fp.read()
        fp.close()
        li = s.split('\n')
        insert_line = -1
        for i in range(len(li)):
            if li[i].find(mark) != -1:
                insert_line = i+2
        if insert_line > 0:
            self.insert_line_to_file(path, insert_line, code)