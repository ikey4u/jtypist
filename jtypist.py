#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import json

class Jtypist():
    def __init__(self, tabsize):
        self.tab = tabsize

    def checkindent(self, indent, line):
        if indent % self.tab != 0:
            raise SyntaxError("Indention should be times of %s => [%s]" % (str(self.tab), line))

    def _parse(self, lines, jdict, key, indent):
        if len(lines) == 0:
            return
        # remove all preceeding empty lines
        i = 0
        while len(lines[i].strip()) == 0:
            i += 1
        lines = lines[i:]

        # process all keys
        curline = lines[0].strip()
        curindent = len(lines[i]) - len(lines[i].lstrip())
        self.checkindent(curindent, lines[0])
        i = 0
        while len(curline) and curline[0] == '-' and curindent == indent:
            j = i + 1
            has_subkey = False
            has_direct_value = False
            # gather value for the current key
            while j < len(lines):
                stripline = lines[j].lstrip()
                if not len(stripline):
                    j += 1
                    continue

                curindent = len(lines[j]) - len(stripline)
                self.checkindent(curindent, lines[j])
                if curindent == indent + self.tab and stripline[0] == '-':
                    has_subkey = True

                # the next key
                if curindent < indent + self.tab:
                    break

                if curindent == indent + self.tab and lines[j][curindent] != '-':
                    has_direct_value = True
                j += 1

            # if a key has subkey, then it should not have direct value.
            # For example, the following is an invalid input since `e` has subkey `t`,
            # it should not have a direct value of `wow`.
            # - e
            #     wow
            #     - t
            if has_subkey and has_direct_value:
                raise SyntaxError("A key [%s] should not have a direct value!" % (curline))

            # current key and its value
            k = curline[1:].strip()
            sublines = lines[i + 1:j]
            if len(sublines):
                if has_subkey:
                    jdict[k] = dict()
                    self._parse(sublines, jdict[k], None, indent + self.tab)
                else:
                    self._parse(sublines, jdict, k, indent + self.tab)
            else:
                kv = curline[1:].strip().split('=')
                k = kv[0].strip()
                v = kv[1].strip() if len(kv) > 1 else ""
                jdict[k] = v

            if j < len(lines):
                curline = lines[j].strip()
                i = j
            else:
                break

        # item content
        if key:
            jdict[key] = '\n'.join([line.strip() for line in lines])

    def parse(self, fpath, tofile = None, toscreen = False):
        d = dict()
        if not fpath.endswith(".jt"):
            print("[x] Configuration must end with '.jt' suffix!")
            return d
        with open(fpath) as fconf:
            try:
                self._parse(fconf.readlines(), d, None, 0)
            except SyntaxError as e:
                print("[x] parse error => %s" % (str(e)))
                return d

        if tofile is not None:
            with open(tofile, 'w') as _:
                json.dump(d, _, ensure_ascii = False, indent = self.tab)

        if toscreen:
            self.pprint(d)

        return d

    def pprint(self, obj):
        if obj:
            print(json.dumps(obj, ensure_ascii = False, indent = self.tab))
        else:
            print("[x] Empty object!")

if __name__ == "__main__":
    jt = Jtypist(4)
    jt.parse("./test.jt", tofile = "./test.json", toscreen = True)
