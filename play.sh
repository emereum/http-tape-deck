#!/usr/bin/env bash

mitmdump -S "$1.tape" --set server_replay_ignore_content=true --set server_replay_nopop=true --set server_replay_kill_extra=true
