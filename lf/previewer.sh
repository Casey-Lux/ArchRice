#!/bin/sh

file="$1"
w="$2"
h="$3"
x="$4"
y="$5"

case "$(file --mime-type -Lb "$file")" in
    image/*)
        ueberzug layer --parser bash <<EOF
{
  "action": "add",
  "identifier": "preview",
  "path": "$file",
  "x": $x,
  "y": $y,
  "width": $w,
  "height": $h
}
EOF
        ;;
    text/*)
        bat --style=numbers --color=always "$file"
        ;;
    *)
        file "$file"
        ;;
esac
