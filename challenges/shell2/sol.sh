#!/bin/sh
# setting the seperators 
awk 'BEGIN {FS=" "; RS="\n" }
    {if (NF > 10 && $7 ~ /pass/ && $11 ~ /[^a-z]/ ) 
        {a[$11][$6]++} }
    END { for (key in a) {
            for (key2 in a[key] ) {
                if (key2 = "Failed") {y = a[key][key2]}
                if (key2 = "Accepted") {x = a[key][key2]}
                }
            if (x > 0 && y > x ) { print key, y, x}
            }
        }
        '
