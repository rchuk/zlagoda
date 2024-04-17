#!/bin/bash

/usr/local/bin/docker-entrypoint.sh generate \
    -i /in/api/_index.yaml \
    -g typescript-fetch \
    -o /out/web_src/generated

/usr/local/bin/docker-entrypoint.sh generate \
    -i /in/api/_index.yaml \
    -g python-flask \
    -o /out/src/generated

cp /out/src/generated/openapi_server/util.py /out/src
cp /out/src/generated/openapi_server/encoder.py /out/src
cp /out/src/generated/openapi_server/typing_utils.py /out/src
cp -r /out/src/generated/openapi_server/openapi/* /out/src/openapi
cp -r /out/src/generated/openapi_server/models/* /out/src/models
