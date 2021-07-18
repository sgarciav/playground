#!/bin/bash

find . -name "*pyc" -o \
     -name "*pycache*" -o \
     -name "#*" -o \
     -name ".#*" | xargs rm -rf
