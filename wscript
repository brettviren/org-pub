#!/usr/bin/env waf

import os
import os.path as osp


def configure(cfg):

    cfg.find_program('joy',var='JOY')

    # some topics need ROOT
    cfg.find_program('root-config',var='ROOT-CONFIG')


from waflib.Task import Task
from waflib import TaskGen


def process_org(bld, org):

    json = org.change_ext('.json')
    html = org.change_ext('.html')
    pdf = org.change_ext('.pdf')

    instdir = '${PREFIX}/' + org.parent.relpath()

    bld(source=org, target=pdf, rule="${JOY} export -o ${TGT} ${SRC}")
    bld(source=org, target=json, rule="${JOY} -c ${JOYCFG} compile -o ${TGT} ${SRC}")
    bld(source=json, target=html, rule="${JOY} -c ${JOYCFG} render -o ${TGT} topic ${SRC}")

    bld.install_files(instdir, org)
    bld.install_files(instdir, pdf)
    bld.install_files(instdir, html)
    
def build(bld):

    bld.env.JOYCFG = bld.path.find_resource('joy.cfg').abspath()

    topic_index_jsons = list()
    for index in bld.path.ant_glob("topics/*/index.org"):
        topic = index.parent

        topic_index_jsons.append(index.change_ext('.json'))

        # process all orgs in topic directory
        for org in topic.ant_glob("*.org"):
            process_org(bld, org)

        bld.install_files('${PREFIX}/'+topic.relpath(),
                          topic.ant_glob('*.svg') +
                          topic.ant_glob('*.png') +
                          topic.ant_glob('*.jpg'))

    feed = bld.path.find_or_declare("feed.xml")
    bld(source = topic_index_jsons, target=feed,
        rule = "${JOY} -c ${JOYCFG} render -o ${TGT} feed ${SRC}")
    bld.install_files('${PREFIX}/'+feed.parent.relpath(), feed)
    return

    
