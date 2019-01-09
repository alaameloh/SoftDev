#!/bin/bash
i=0
while read line ; do
    if [ $line != "." ]; then 
        folders[$i]=$line
        ((i++))
    fi
done < <(find . -type d | sort -r) 
i=0
while read line ; do
    if ! [[ $line =~ ^.$ ]]; then
    recent_folders[$i]=$line
    ((i++))
    fi
done < <(find . -atime -31 -type f -exec dirname {} + | sort | uniq )
len_folders=${#folders[@]}
len_recent_folders=${#recent_folders[@]}

target=("${folders[@]}") 

for ((i=0; i<$len_recent_folders; i++)); do
    for ((j=0; j<$len_folders; j++)) do
       if [[ ${recent_folders[$i]} == *${folders[$j]}* ]] ; then target[$j]="pass";fi
    done
done

for elem in ${target[@]}; do
    if ! [[ $elem == "pass" ]] ; then tar -cf $elem.tgz $elem --remove-files;fi
done

rm sol.bash
