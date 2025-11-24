#!/bin/bash

USER=Serhii

echo "Current date: $(date)"

echo "Hello $USER!"

echo "Рабочая директория: $PWD"

bioset_count=$(ps aux | grep 'bioset' | grep -v grep | wc -l)
echo "количество процессов bioset равно: $bioset_count"

permissions=$(ls -l /etc/passwd | awk '{print $1}')
echo "$permissions"
