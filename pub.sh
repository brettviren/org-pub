#!/bin/bash

set -e

mydir=$(dirname $(readlink -f $BASH_SOURCE))
cd $mydir

emacsdir=$mydir/emacs.d
if [ ! -d "$emacsdir" ] ; then
    mkdir -p $emacsdir
fi

rm -rf $emacsdir
mkdir -p $emacsdir
for pkg in org htmlize ; do
    pkgel=$(ls ~/.emacs.d/elpa/${pkg}-*/${pkg}.el | tail -1)
    pkgdir=$(dirname $pkgel)
    ln -s $pkgdir $emacsdir/$pkg
done

topub="$@"
if [ -z "$topub" ] ; then
    topub="pub-all"
fi

for what in "$topub"
do
    echo "Building $what"
    pwd
    emacs --batch -Q -l pub.el --eval "(org-publish-project \"$what\")"
done
