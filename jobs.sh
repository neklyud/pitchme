#!/usr/bin/env bash

platform="$(uname -s)"
if [[ "$platform" == "Linux"* ]]; then
  n_jobs=$(awk '/^processor/{n+=1}END{print n}' /proc/cpuinfo)
elif [[ "$platform" == "Darwin"* ]]; then
  n_jobs=$(sysctl -n hw.ncpu)
else
  n_jobs=1
fi

echo ${n_jobs}
