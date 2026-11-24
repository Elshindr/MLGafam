#!/bin/bash

docker run -d --name rncp-fastapi  -v model_vol:/models/ rncp-fastapi