#!/bin/bash

FUNCTION_NAME=store-remo-to-dynamodb

rm -f lambda.zip

pushd src
    zip -rq ../lambda.zip .
popd

aws lambda update-function-code --function-name $FUNCTION_NAME --zip-file fileb://lambda.zip