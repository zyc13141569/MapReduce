#!/bin/bash

WCDIR=/home/tfidf
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar

printf "\nTF MapReduce\n\n"
bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/tfMap.py,$WCDIR/tfReduce.py 	\
    -mapper  $WCDIR/tfMap.py                      	\
    -reducer $WCDIR/tfReduce.py                   	\
    -input   Gutenberg/'*'                          \
    -output  Gutenberg-out

printf "\nrIDF MapReduce\n\n"
bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/idfMap.py,$WCDIR/idfReduce.py   \
    -mapper  $WCDIR/idfMap.py                       \
    -reducer $WCDIR/idfReduce.py                    \
    -input   Gutenberg-out/'*'                      \
    -output  Result
