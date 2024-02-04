#!/bin/bash

# This script will update the entire system.
# It will update the system, upgrade the system, and then clean the system.
# It will also remove any orphaned packages.

# Update the system using pacman
sudo pacman -Syyu --noconfirm

# Get the current time and date in the format of 01-Jan-2024 12:00:00
current_time=$(date +"%d-%b-%Y %T")

# Log the time and date of the update
echo "System updated on: $current_time" >> logs/sysupdate.log

