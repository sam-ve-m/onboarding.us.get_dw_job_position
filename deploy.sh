#!/bin/bash

fission spec init
fission env create --spec --name get-employ-positions-env --image nexus.sigame.com.br/fission-env-cx-async:0.0.1 --builder nexus.sigame.com.br/fission-builder-3.8:0.0.1
fission fn create --spec --name get-employ-positions-fn --env get-employ-positions-env --src "./func/*" --entrypoint main.get_employ_positions --executortype newdeploy --maxscale 1
fission route create --spec --name get-employ-positions-rt --method GET --url /enum/get_employ_positions --function get-employ-positions-fn