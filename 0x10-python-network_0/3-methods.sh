#!/bin/bash
# list the methods
curl -Is "$1" | grep "Allow" | cut -d ' ' -f 2-
