#! /usr/bin/bash env

cd ../
python build_rawframes.py ../data/hmdb51/videos/ ../data/hmdb51/rawframes/ --level 2  --ext avi
echo "Raw frames (RGB only) generated for train set"


cd hmdb51/
