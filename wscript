#!/usr/bin/env waf

import os
import os.path as osp


def configure(cfg):

    cfg.find_program('emacs',var='EMACS')
    cfg.find_program('root-config',var='ROOT-CONFIG')


from waflib.Task import Task
from waflib import TaskGen

class org2body(Task):
    run_str = "${EMACSRUNNER} ${ORG2BODY} org2body ${SRC} ${TGT}"
    ext_out = ['.body']

class org2json(Task):
    run_str = "${EMACSRUNNER} ${ORG2JSON} org2json ${SRC} ${TGT}"
    ext_out = ['.json']

class org2revs(Task):
    run_str = "git log --pretty=format:'%%H %%at' --reverse -- ${SRC} > ${TGT}"
    ext_out = ['.revs']

class org2html(Task):
    run_str = "${JOY} render ${SRC[0].abspath()} topic.html ${TGT}"
    ext_out = ['.html']

@TaskGen.extension(".org")
def process_org_task(self, node):
    outs = list()
    for op in 'body json revs'.split():
        out = node.change_ext('.%s'%op)
        outs.append(out)
        self.create_task('org2%s'%op,node,out)

    print node
    for o in outs:
        print '\t',o

    self.create_task('org2html',[node]+outs,node.change_ext('.html'))

def build(bld):

    # fixme: move all this stuff into a joy Python package.
    bld.env.ORG2BODY = bld.path.find_resource('org2body.el').abspath()
    bld.env.ORG2JSON = bld.path.find_resource('org2json.el').abspath()
    bld.env.EMACSRUNNER = bld.path.find_resource('emacsrunner').abspath()
    bld.env.JOY = bld.path.find_resource('joy.py').abspath()

    for topic in bld.path.ant_glob("topics/this/index.org"):
        for org in topic.parent.ant_glob("*.org"):
            bld(source=org)
    return

    
