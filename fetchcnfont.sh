#!/bin/bash
#Try to get upstream latest files

LANG="CN"
PREFIX="SourceHanSans$LANG"
VERSION="1.001"
ARCHIVE="$PREFIX-$VERSION"
TMPDIR=$(mktemp -d --tmpdir=/var/tmp fetchcnfont-XXXXXXXXXX)
[ $? != 0 ] && exit 1
umask 022
pushd "$TMPDIR"

URLPREFIX="https://github.com/adobe-fonts/source-han-sans/raw/release/SubsetOTF"
VARIANTS="Bold ExtraLight Heavy Light Medium Normal Regular"

for i in $(echo $VARIANTS | tr " " "\n")
do wget "$URLPREFIX/$LANG/$PREFIX-$i.otf"
done

mkdir "$ARCHIVE"
mv $PREFIX-*.otf "$ARCHIVE"
chmod -x $ARCHIVE/*.otf
zip "$ARCHIVE.zip" $ARCHIVE/*.otf
popd
mv "$TMPDIR/$ARCHIVE.zip" .
rm -fr "$TMPDIR"
