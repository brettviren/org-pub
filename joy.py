#!/usr/bin/env python

import os.path as osp
import time, datetime
import json
import click

me = osp.abspath(__file__)
mydir = osp.dirname(me)
blddir = osp.join(mydir, 'build')

def get_template_dirs(path):
    "Return all template directories along the path"
    path = osp.abspath(path)
    if osp.isfile(path):
        path = osp.dirname(path)
    templates = []
    while path:
        maybe = osp.join(path, 'templates')
        if osp.isdir(maybe):
            templates.append(maybe)
        if path == mydir:
            break
        path = osp.dirname(path)
        if path == "/":
            break
    templates.reverse()
    return templates

def get_env(filename):
    "Return the template environment for a given source file"
    from jinja2 import Environment, FileSystemLoader
    return Environment(loader=FileSystemLoader(get_template_dirs(filename)))

def relpath(prefix, path):
    if 0 != path.find(prefix):
        return None
    path = path[len(prefix):]
    if path.startswith("/"):
        path = path[1:]
    return path

def find_build_file(filename, ext):
    "Find the built file associated with filename and with the given extension"
    path = relpath(mydir, osp.abspath(filename))
    origext = osp.splitext(filename)[1]
    path = osp.join(blddir, path).replace(origext, ext)
    if osp.isfile(path):
        return path
    return None

def load_revs_file(revsfile):
    "Read git revs file and return list of tuple."
    ret = list()
    with open(revsfile) as fp:
        for line in fp.readlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            githash,timestamp = line.split()
            t = time.gmtime(float(timestamp))
            dt = datetime.datetime(*t[:6])
            ret.append((githash, dt))
    return ret;


def oj_section_keywords(j):
    if j[0] != "org-data": return
    section = j[2]
    if section[0] != "section": return
    ret = dict()
    for part in section[2:]:
        if part[0] != "keyword":
            continue
        kwrec = part[1]
        ret[kwrec['key'].lower()] = kwrec['value']
    return ret;

def oj_headline_structure(j):
    if j[0] != "org-data": return

    def headlines(entries, root=None):
        root = root or []
        count = 0;
        ret = list()
        for ent in entries:
            if type(ent) != list:
                print 'What is this?', str(ent)
                continue
            if not ent: continue
            if ent[0] != "headline": continue
            count += 1
            kwds = ent[1]
            thisroot = root + [count]
            ret.append((thisroot, kwds['raw-value']))
            ret += headlines(ent[2:], thisroot)
        return ret;

    return headlines(j[2:])

        
    

def orgjson_summary(j):
    return oj_section_keywords(j)

class JoyFile(object):
    '''
    Everything there is to know about a joy file.
    '''
    def __init__(self, orgfile):
        orgfile = osp.abspath(orgfile)
        self.orgpath = orgfile
        self.srcfile = osp.basename(orgfile)
        self.env = get_env(orgfile)
        self.orgjson = json.load(open(find_build_file(orgfile, '.json')))
        self.meta = oj_section_keywords(self.orgjson)
        self.headlines = oj_headline_structure(self.orgjson)
        self.revs = load_revs_file(find_build_file(orgfile, '.revs'))
        self.created = self.revs[0][1]
        self.revised = self.revs[-1][1]
        self.body = open(find_build_file(orgfile, '.body')).read()

        return

    def __str__(self):
        s = [self.orgfile]
        for h,dt in self.revs:
            s.append('\t%s %s' % (h, str(dt)))
        return '\n'.join(s)

    def render(self, template):
        '''
        Render this joy file given the template using the data members of this object.
        '''
        tmpl= self.env.get_template(template)
        if not tmpl: return
        return tmpl.render(**self.__dict__)

    pass

@click.group()
def cli():
    pass

@cli.command()
@click.argument('orgfile')
@click.argument('template')
@click.argument('output')
def render(orgfile, template, output = None):
    jf = JoyFile(orgfile)
    output = output or "/dev/stdout"
    open(output,"w").write(jf.render(template))
    return    
    

def test():
    import sys, json
    jf = JoyFile(sys.argv[1])
    #print jf.meta
    #print json.dumps(jf.orgjson, indent=2)
    #print oj_headline_structure(jf.orgjson)
    #print 'created:', jf.created()
    #print 'revised:', jf.revised()
    print jf.render("topic.html")

if '__main__' == __name__:
    cli()
