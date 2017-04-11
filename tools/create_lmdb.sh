#!/bin/sh
if [ ! -d lmdb ]; then
    mkdir lmdb
fi

for subset in train test; do
    $CAFFEROOT/build/tools/convert_annoset.bin \
        --anno_type=detection --label_type=xml \
        --check_label=true --encoded --encode_type=jpg \
        --resize_height=512 \
        --label_map_file="helper/labelmap.prototxt" \
        data/ splits/${subset}.txt lmdb/${subset}_lmdb
done
