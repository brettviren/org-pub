#!/usr/bin/env waf

import os
import os.path as osp


def configure(cfg):

    cfg.find_program('joy',var='JOY')

    # some topics need ROOT
    cfg.find_program('root-config',var='ROOT-CONFIG')


from waflib.Task import Task
from waflib import TaskGen

class org2body(Task):
    run_str = "${JOY} export -o ${TGT} ${SRC}"
    ext_out = ['.body']

class org2json(Task):
    run_str = "${JOY} export -o ${TGT} ${SRC}"
    ext_out = ['.json']

class org2revs(Task):
    run_str = "${JOY} revisions -o ${TGT} ${SRC}"
    ext_out = ['.revs']

class org2html(Task):
    run_str = "${JOY} render -o ${TGT} -b ${SRC[1].abspath()} -j ${SRC[2].abspath()} -r ${SRC[3].abspath()} topic.html ${SRC[0].abspath()}"
    ext_out = ['.html']

@TaskGen.extension(".org")
def process_org_task(self, node):
    outs = list()
    for op in 'body json revs'.split():
        out = node.change_ext('.%s'%op)
        outs.append(out)
        self.create_task('org2%s'%op,node,out)

    self.create_task('org2html',[node]+outs,node.change_ext('.html'))

def build(bld):

    for topic in bld.path.ant_glob("topics/this/index.org"):
        for org in topic.parent.ant_glob("*.org"):
            bld(source=org)
    return

    
