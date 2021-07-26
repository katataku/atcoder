#!/bin/sh
rm output/*

dirpath="./input"
files=`ls $dirpath`

printf "\n"
for file in $files;
do
    printf "=====${file}=======\n"

    input="${file}"
    output="${file}"
    answer="${file}"

    python main.py <input/${input} | tee output/${output}

    if [ -e answer/${answer} ]; then
        diff -u output/${output} answer/${answer} >tmp
        if [ $? -eq 0 ]; then
            printf "\nCOLLECT ANSWER!!\n"
        elif [ $? -eq 1 ]; then
            printf "\n--- diff output answer --------------------\n"
            cat tmp
            printf "\nWRONG ANSWER...\n"
        fi
        rm tmp
    fi
done


