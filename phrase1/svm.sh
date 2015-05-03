#!/bin/bash

#-- config --

libSVMPath='./phrase1/libsvm-3.20'
# numsForIter=" 0 1 2 4 5 6 7 8 9 10 "

# linearOrRBF="0"
linearOrRBF="2"

# UsingGrid="1"
UsingGrid="0"

#--

if [ $# == 0 ]; then
  echo "usage:$0 trainingfilePath testingfilePath outputResultFolderPath [-v number]"
  exit
fi

inputDataFilenamePathTrain=$1
inputDataFilenamePathTest=$2
outputResultFolderPath=$3
outputResultFolderTmpPath=$3'/atmp'


  train=$libSVMPath'/svm-train'
  predict=$libSVMPath'/svm-predict'
  scale=$libSVMPath'/svm-scale'
  grid=$libSVMPath'/tools/grid.py'


cd ${inputDataFilenamePathTrain%/*}
rm -r $outputResultFolderPath
mkdir $outputResultFolderPath
mkdir $outputResultFolderTmpPath



trainingFile=${inputDataFilenamePathTrain##*/}
accuracyFile=${trainingFile%%.*}'.accuracy'
#-- train
sScaleFile=${trainingFile%%.*}'.scale'
rangeFile=${trainingFile%%.*}'.rfile'
$scale -l -1 -u 1 -s $rangeFile $trainingFile > $sScaleFile
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
testingFile=${inputDataFilenamePathTest##*/}
rScaleFile=${testingFile%%.*}'.scale'
         
$scale -r $rangeFile $testingFile > $rScaleFile
resultFile=${testingFile%%.*}'.result'
$predict $rScaleFile $modelFile $resultFile | awk '{print $3}' >>"$accuracyFile"

if [ -d $outputResultFolderPath ] && [ "$outputResultFolderPath" != "$inputDataFilenamePathTrain" ]; then 
  # mv *.scale *.model *.rfile $outputResultFolderTmpPath
  mv *.model *.scale *.rfile $outputResultFolderTmpPath
  mv *.accuracy *.result $outputResultFolderPath
fi




