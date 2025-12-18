#!/bin/sh

file="$1"

case "$(file --mime-type -Lb "$file")" in
    text/*)
        bat --style=plain --color=always "$file"
        ;;
    application/pdf)
        pdftotext "$file" - | sed -n '1,200p'
        ;;
    *)
        file "$file"
        ;;
esac
