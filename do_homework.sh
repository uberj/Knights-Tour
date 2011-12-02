#!/bin/bash

do_problem2 () {
    solutions=0
    for ((i=0; i<$2; i++))
    do
        for ((j=0; j<$3; j++))
        do
            echo "Knights tour with initial move ($i, $j)"
            python knights_tour.py $1  $i $j
            if [ $? -eq 0 ]
            then
                solutions=$((solutions+1))
            fi
            echo
        done
    done
    echo "There were $solutions successful tours out of $1 attempts."
    echo
}

echo "Jacques Uber"
echo "Knights Tour"
echo "Homework 9"
echo "CS325"
echo "12/1/2011"
echo
echo
echo "===================================================="
echo "===================================================="
echo "Problem 2 and 3 . Test your program by using as starting square each of the 25 squares on a 5 by 5 gameboard. How many tours did it find?"
echo "===================================================="
do_problem2 5 5 5

echo "===================================================="
echo "===================================================="
echo "Problem 4. Run your program from 4 different initial squares on a 6 by 6 gameboard. Does your program always find a tour? Are the tours you found open or closed? How many different tours does your program?"
echo "===================================================="
do_problem2 6 2 2

echo "===================================================="
echo "===================================================="
echo "Problem 4. Run your program from 4 different initial squares on a 8 by 8 gameboard. Does your program always find a tour? Are the tours you found open or closed? How many different tours does your program?"
echo "===================================================="
do_problem2 8 2 2
