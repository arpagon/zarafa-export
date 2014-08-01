#!/bin/bash

#We need this to avoid issues with spaces
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

for e in $(ls -d */);do
    echo "USUARIO $e"
    echo ""
    cd $e
    mkdir -p $e Maildir
    #Delete this line if you prefer not to mark all mail as read
    mv .Inbox/new/* ./Inbox/cur/
    #OpenChange uses Sent rather than Sent Items
    mv ".Sent Items" .Sent
    for i in $(ls -A );do
        if [ $i != "cur" ] && [ $i != "new" ] && [ $i != "tmp" ] ; then
            if [ $i == ".Inbox" ]; then
                mv .Inbox/* Maildir/
            elif [ $i != "Maildir" ]; then
                    mv $i Maildir
            fi;
        fi;
     done
     cd ..
done
