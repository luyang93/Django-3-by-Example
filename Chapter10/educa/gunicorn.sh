#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=educa.settings.pro
gunicorn -w 3 -b "127.0.0.1:8000" educa.wsgi
