#!/usr/bin/env bash
set -o errexit

echo "Current directory:"
pwd
ls -la

export DJANGO_SETTINGS_MODULE=vartalap.settings
export PYTHONPATH=/opt/render/project/src

pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --noinput
