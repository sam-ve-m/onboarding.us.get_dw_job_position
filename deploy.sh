fission spec init
fission env create --spec --name onb-us-enum-jb-pos-env --image nexus.sigame.com.br/fission-onboarding-us-enum-job-position:0.1.0 --poolsize 0 --version 3 --imagepullsecret "nexus-v3" --spec
fission fn create --spec --name onb-us-enum-jb-pos-fn --env onb-us-enum-jb-pos-env --code fission.py --targetcpu 80 --executortype newdeploy --maxscale 3 --requestsperpod 10000 --spec
fission route create --spec --name onb-us-enum-jb-pos-rt --method GET --url /enum/get_employ_positions --function onb-us-enum-jb-pos-fn
