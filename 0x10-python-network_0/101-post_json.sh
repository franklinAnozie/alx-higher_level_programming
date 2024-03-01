#!/bin/bash
# JSON file
curl -sH "Content-Type: application/json" -d "@$2" "$1"
