#!/bin/sh

#-- config --

#--
segResultTrainFile='tmp/segResultTrain.txt'
segResultTestFile='tmp/segResultTest.txt'
kBest='0'
lang='pku'
fileTrain='tmp/noTag.txt'
fileTest='tmp/noTagTest.txt'


python src/noTag.py
python src/noTagTest.py



# echo -n "File: " >&2
# echo $fileTrain >&2
# echo -n "Encoding: " >&2
# echo UTF-8 >&2
# echo "-------------------------------" >&2

# BASEDIR=`dirname $0`
# DATADIR=$BASEDIR/stanford-segmenter/data
# #LEXDIR=$DATADIR/lexicons
# JAVACMD1="java -mx2g -cp $BASEDIR/stanford-segmenter/*: edu.stanford.nlp.ie.crf.CRFClassifier -sighanCorporaDict $DATADIR -textFile $fileTrain -inputEncoding UTF-8 -sighanPostProcessing true $ARGS"
# JAVACMD2="java -mx2g -cp $BASEDIR/stanford-segmenter/*: edu.stanford.nlp.ie.crf.CRFClassifier -sighanCorporaDict $DATADIR -textFile $fileTest -inputEncoding UTF-8 -sighanPostProcessing true $ARGS"
# DICTS=$DATADIR/dict-chris6.ser.gz
# KBESTCMD=""

# if [ $kBest != "0" ]; then
#     KBESTCMD="-kBest $kBest"
# fi

# # if [ $lang = "ctb" ]; then
# #   $JAVACMD -loadClassifier $DATADIR/ctb.gz -serDictionary $DICTS $KBESTCMD | awk '{print $3}' >>"$segResultFile"
# # elif [ $lang = "pku" ]; then
# #   $JAVACMD -loadClassifier $DATADIR/pku.gz -serDictionary $DICTS $KBESTCMD | awk '{print $3}' >>"$segResultFile"
# # fi
# if [ $lang = "ctb" ] || [ $lang = "pku" ]; then
#   $JAVACMD1 -loadClassifier $DATADIR/$lang.gz -serDictionary $DICTS $KBESTCMD > $segResultTrainFile
  
#   $JAVACMD2 -loadClassifier $DATADIR/$lang.gz -serDictionary $DICTS $KBESTCMD > $segResultTestFile
# fi

python src/train.py

