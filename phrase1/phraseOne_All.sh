#!/bin/sh

#-- config --

libSVMPath='libsvm-3.20'
# numsForIter=" 0 1 2 4 5 6 7 8 9 10 "

# linearOrRBF="0"
linearOrRBF="2"

# UsingGrid="1"
UsingGrid="0"

#--
segResultTrainFile='tmp/segResultTrain.txt'
segResultTestFile='tmp/segResultTest.txt'
kBest='0'
lang='pku'
fileTrain='tmp/noTag.txt'
fileTest='tmp/noTagTest.txt'

# usage() {
#   echo "Usage: $0 outputPath" >&2
#   echo >&2
#   echo "Example: $0 " >&2
#   exit
# }

# if [ $# -lt 1 -o $# -gt 2 ]; then
# 	usage
# fi

# ARGS="-keepAllWhitespaces false"
# if [ $# -eq 2 -a "$1"=="-k" ]; then
# 		ARGS="-keepAllWhitespaces true"
#     outputFile=$2
# else 
# 	if [ $# -eq 1 ]; then		
#     outputFile=$1
# 	else
# 		usage	
# 	fi
# fi

python src/noTag.py
python src/noTagTest.py



echo -n "File: " >&2
echo $fileTrain >&2
echo -n "Encoding: " >&2
echo UTF-8 >&2
echo "-------------------------------" >&2

BASEDIR=`dirname $0`
DATADIR=$BASEDIR/stanford-segmenter/data
#LEXDIR=$DATADIR/lexicons
JAVACMD1="java -mx2g -cp $BASEDIR/stanford-segmenter/*: edu.stanford.nlp.ie.crf.CRFClassifier -sighanCorporaDict $DATADIR -textFile $fileTrain -inputEncoding UTF-8 -sighanPostProcessing true $ARGS"
JAVACMD2="java -mx2g -cp $BASEDIR/stanford-segmenter/*: edu.stanford.nlp.ie.crf.CRFClassifier -sighanCorporaDict $DATADIR -textFile $fileTest -inputEncoding UTF-8 -sighanPostProcessing true $ARGS"
DICTS=$DATADIR/dict-chris6.ser.gz
KBESTCMD=""

if [ $kBest != "0" ]; then
    KBESTCMD="-kBest $kBest"
fi

# if [ $lang = "ctb" ]; then
#   $JAVACMD -loadClassifier $DATADIR/ctb.gz -serDictionary $DICTS $KBESTCMD | awk '{print $3}' >>"$segResultFile"
# elif [ $lang = "pku" ]; then
#   $JAVACMD -loadClassifier $DATADIR/pku.gz -serDictionary $DICTS $KBESTCMD | awk '{print $3}' >>"$segResultFile"
# fi
if [ $lang = "ctb" ] || [ $lang = "pku" ]; then
  $JAVACMD1 -loadClassifier $DATADIR/$lang.gz -serDictionary $DICTS $KBESTCMD > $segResultTrainFile
  
  $JAVACMD2 -loadClassifier $DATADIR/$lang.gz -serDictionary $DICTS $KBESTCMD > $segResultTestFile
fi

python src/rightWrongParsed.py

python src/parsedNgram.py

python src/stanford_ngram_train.py

python src/stanford_ngram_test.py




# if [ $# == 0 ]; then
#   echo "usage:$0 trainingfilePath testingfilePath outputResultFolderPath [-v number]"
#   exit
# fi

inputDataFilenamePathTrain='tmp/train_prob.txt'
inputDataFilenamePathTest='tmp/test_prob.txt'
# outputResultFolderPath=$outputFile
# outputResultFolderTmpPath=$outputFile'/atmp'


  train=$libSVMPath'/svm-train'
  predict=$libSVMPath'/svm-predict'
  scale=$libSVMPath'/svm-scale'
  grid=$libSVMPath'/tools/grid.py'


# cd ${inputDataFilenamePathTrain%/*}
# rm -r $outputResultFolderPath
# mkdir $outputResultFolderPath
# mkdir $outputResultFolderTmpPath



trainingFile='tmp/'${inputDataFilenamePathTrain##*/}

#-- train
sScaleFile=${trainingFile%%.*}'.scale'
rangeFile=${trainingFile%%.*}'.rfile'
$scale -s $rangeFile $trainingFile > $sScaleFile
modelFile=${trainingFile%%.*}'.model'

   if [ $UsingGrid == "1" ]; then
      # gridResult=`python $grid -out "null" $sScaleFile`
      gridResult=`python $grid -gnuplot "null" -out "null" $sScaleFile`
      paraC=`echo $gridResult | cut -d' ' -f1`
      paraG=`echo $gridResult | cut -d' ' -f2`
      echo $paraC $paraG
      $train -q -t $linearOrRBF -c $paraC -g $paraG $sScaleFile $modelFile
    else
      # $train -q -t $linearOrRBF $sScaleFile $modelFile
      # log--
      $train -q -t $linearOrRBF -c 2048.0 -g 0.0001220703125 $sScaleFile $modelFile
    fi

#--then test
# testingFile='ngram_test_prob.txt'
testingFile='tmp/'${inputDataFilenamePathTest##*/}
accuracyFile=${testingFile%%.*}'.accuracy'
rScaleFile=${testingFile%%.*}'.scale'
         
$scale -r $rangeFile $testingFile > $rScaleFile
resultFile=${testingFile%%.*}'.result'
$predict $rScaleFile $modelFile $resultFile | awk '{print $3}' >>"$accuracyFile"

# cd tmp

# if [ -d $outputResultFolderPath ] && [ "$outputResultFolderPath" != "$inputDataFilenamePathTrain" ]; then 
#   # mv *.scale *.model *.rfile $outputResultFolderTmpPath
#   mv *.model *.scale *.rfile $outputResultFolderTmpPath
#   mv *.accuracy *.result $outputResultFolderPath
# fi

# cd ..

python src/outputFile.py
