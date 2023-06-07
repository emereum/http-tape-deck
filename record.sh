#!/usr/bin/env bash

mitmdump -w "$1.tape" --anticache --set scripts=deterministic.py