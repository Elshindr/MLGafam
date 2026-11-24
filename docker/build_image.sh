#!/bin/bash

docker build -t rncp-prepare-dataframe -f ./build_model/Dockerfile   .
docker build -t rncp-build_model -f ./prepare_dataframe/Dockerfile   .
