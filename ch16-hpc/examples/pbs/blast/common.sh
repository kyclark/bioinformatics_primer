# --------------------------------------------------
function lc() {
    wc -l $1 | cut -d ' ' -f 1
}

# --------------------------------------------------
function get_lines() {
 FILE=$1
 OUT_FILE=$2
 START=${3:-1}
 STEP=${4:-1}

 if [ -z $FILE ]; then
   echo No input file
   exit 1
 fi

 if [ -z $OUT_FILE ]; then
   echo No output file
   exit 1
 fi

 if [[ ! -e $FILE ]]; then
   echo Bad file \"$FILE\"
   exit 1
 fi

 awk "NR==$START,NR==$(($START + $STEP - 1))" $FILE > $OUT_FILE
}

# --------------------------------------------------
function init_dir {
    for dir in $*; do
        if [ -d "$dir" ]; then
            rm -rf $dir/*
        else
            mkdir -p "$dir"
        fi
    done
}
