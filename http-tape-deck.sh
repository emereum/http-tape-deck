#!/usr/bin/env bash

THIS_DIR=$(cd -P "$(dirname "$(readlink -f "${BASH_SOURCE[0]}" || echo "${BASH_SOURCE[0]}")")" && pwd)

if [[ $# != 2 ]] || [[ $1 != "play" && $1 != "record" ]]; then
    echo "Usage: http-tape-deck (play|record) tape-name"
    exit 1
fi

if [[ $1 == "record" ]]; then
    mitmdump -w "$2.tape" --anticache --set scripts="$THIS_DIR/deterministic.py" "${@:3}"
    exit 0
fi

if [[ $1 == "play" ]]; then
    mitmdump -S "$2.tape" --set server_replay_ignore_content=true --set server_replay_nopop=true --set server_replay_kill_extra=true "${@:3}"
    exit 0
fi
