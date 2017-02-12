#!/bin/bash
. /appenv/bin/activate
cd /app
exec hug -f server.py
