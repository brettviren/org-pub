#!/bin/bash

mydir=$(dirname $BASH_SOURCE)
cd $mydir

for what in $@
do
    emacs --batch -Q -l pub.el --eval "(org-publish-project \"$what\")"
done
