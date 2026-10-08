#!/bin/sh
#SBATCH --job-name=corpus-greeting
#SBATCH --nodes=1
#SBATCH --ntasks=1
printf "Hello, World!\n"
