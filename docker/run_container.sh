#!/bin/bash

docker run -d --name rncp-prepare-dataframe -v data_vol:/data/  rncp-prepare-dataframe
docker run -d --name rncp-build_model -v data_vol:/data/ -v model_vol:/models/ rncp-build_model