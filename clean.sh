#!/bin/bash

find . -name "*pyc" -o \
     -name "*pycache*" | xargs rm -rf
