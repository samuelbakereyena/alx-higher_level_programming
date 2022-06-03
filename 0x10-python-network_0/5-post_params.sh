#!/bin/bash
# sends post request with 2 variables
curl -sd 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
