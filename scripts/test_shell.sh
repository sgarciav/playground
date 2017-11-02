#!/bin/bash

GLOBAL_VAR=1

# update variables if there are user inputs
while getopts n: flag; do
    case $flag in
	n)
	    GLOBAL_VAR=$OPTARG
	    ;;
	?)
	echo "this is a test";
	exit;
	;;
    esac
done


function rmfile()
{
    echo "function input: $1"
    echo ""
    if [ -f $1 ]; then
	echo "add me" >> $1
    fi
}

function test_fun()
{
    echo "global: $GLOBAL_VAR"
    echo "temp: $temp_var"
    echo "input: $1"

    # rosrun turtlesim turtlesim_node
    if [ $# -eq 2 ]; then
	echo "helloooo"
    fi
}

function test_cd()
{
    echo "testing cd:"
    echo "-------------------"
    mkdir sergio_dir1
    cd $1
    mkdir $2
}

temp_var=10
echo "file input: $1"
echo ""
rmfile "deleteme.txt"
rmfile "$1"
echo "file input: $1"
echo ""
test_fun "sergios" "sure"
