FROM python:3.11 AS builder

WORKDIR /app

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
ENV PYTHONPATH="/app/src:$PYTHONPATH"

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


# FROM python:3.7 AS test_runner
# WORKDIR /tmp
# COPY --from=builder /venv /venv
# COPY --from=builder /usr/src/app/tests tests
# ENV PATH=/venv/bin:$PATH

# install test dependencies
# RUN pip install pytest

# run tests
# RUN pytest tests


# FROM python:3.7 AS service
# WORKDIR /root/app/site-packages
# COPY --from=test_runner /venv /venv
# ENV PATH=/venv/bin:$PATH
