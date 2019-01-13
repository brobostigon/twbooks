#!/bin/bash
psql -S -h 85.119.83.147 -p 5432 --username=ptaylor -d pfdplaytest -v HISTFILE=psql_history
