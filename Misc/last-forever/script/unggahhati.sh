#!/bin/bash

for i in {1..64}; do
    cut -c$i < hatigw.txt > myheart.txt
    aws --profile awscli s3 cp ./myheart.txt s3://forever.lychnobyte.my.id
done

cp myheartasli.txt myheart.txt
aws --profile awscli s3 cp ./myheart.txt s3://forever.lychnobyte.my.id