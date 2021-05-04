#!/bin/sh
if [ $# -eq 0 ]
  then
    echo "Usage:
            ./build.sh build : Builds the project
            ./build.sh run   : Runs the project
            ./build.sh test  : Test the project
    "
fi
if [ "$1" = "build" ]
  then
    npm install && npx webpack
    scss hive/scss/main.scss hive/static/css/main.css
    docker-compose build
fi

if [ "$1" = "run" ]
  then
    docker-compose up
fi

if [ "$1" = "test" ]
  then
    nosetests -w test

fi

