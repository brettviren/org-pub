#!/usr/bin/env waf

import os
import sys
import os.path as osp


def configure(cfg):

    cfg.find_program('joy',var='JOY')

    # some topics need ROOT
    cfg.find_program('root-config',var='ROOT-CONFIG')


from waflib.Task import Task
from waflib import TaskGen


def process_org(bld, org):

    json = org.change_ext('.json')
    html = json.change_ext('.html')
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

    topic_templ = bld.path.find_resource('templates/topic.html')

    # topic index.html's
    topic_index_jsons = list()
    for index in bld.path.ant_glob("topics/*/index.org"):
        topic = index.parent

        index_json = index.change_ext('.json')
        topic_index_jsons.append(index_json)

        bld.add_manual_dependency(index.change_ext('.html'), topic_templ)

        # process all orgs in topic directory
        for org in topic.ant_glob("*.org"):
            process_org(bld, org)

        bld.install_files('${PREFIX}/'+topic.relpath(),
                          topic.ant_glob('*.svg') +
                          topic.ant_glob('*.png') +
                          topic.ant_glob('*.jpg'))

    def single(fname):
        what,ext = os.path.splitext(fname)
        node = bld.path.find_or_declare(fname)
        bld(source = topic_index_jsons, target=node,
            rule = "${JOY} -c ${JOYCFG} render -o ${TGT} %s ${SRC}"%what)
        bld.install_files('${PREFIX}/'+node.parent.relpath(), node)
    single('topics.html')
    single('feed.xml')

    # index of indices
    # topics = bld.path.find_or_declare("topics.html")
    # bld(source = topic_index_jsons, target=topics,
    #     rule = "${JOY} -c ${JOYCFG} render -o ${TGT} topics ${SRC}")
    # bld.install_files('${PREFIX}/'+topics.parent.relpath(), topics)

    # feed = bld.path.find_or_declare("feed.xml")
    # bld(source = topic_index_jsons, target=feed,
    #     rule = "${JOY} -c ${JOYCFG} render -o ${TGT} feed ${SRC}")
    # bld.install_files('${PREFIX}/'+feed.parent.relpath(), feed)
    return

    
