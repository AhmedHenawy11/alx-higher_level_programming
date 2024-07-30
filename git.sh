#!/bin/bash

# Get a random description word
if [ $# -ge 1 ];
then
        commit_word="$@"
else
        commit_word="upload"
fi;

# Get currnet git branch
current_branch=$(git rev-parse --abbrev-ref HEAD)
# Add all the files in the current directory to the Git staging area
git add .

# Create a new commit with the random description word
git commit -m "$commit_word"

# Push the changes to the remote repository
git push origin $current_branch