#!/usr/bin/bash
fission spec init
fission env create --spec --name env-get-bmf-client --image nexus.sigame.com.br/fission-cx-env-3.8:0.0.3 --builder nexus.sigame.com.br/fission-cx-builder-3.8:0.0.3
fission fn create --spec --name fn-get-bmf-client --env env-get-bmf-client --src "./func/*" --entrypoint main.get_enums --executortype newdeploy
fission route create --spec --name rt-get-bmf-client --method GET --url /enum/bmf_client --function fn-get-bmf-client
