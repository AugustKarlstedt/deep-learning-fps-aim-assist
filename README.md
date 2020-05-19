# deep learning aim assist
idea: use off-the-shelf object detector to draw bounding boxes around enemies in first person shooter games

## plan
1. caputre screen from game (doesn't have to be 60 frames per second, could really just be like 5 FPS)
2. use object detector on image
3. draw boxes over screen

## data
- capture gameplay or use twitch video
- annotate a bunch of images

## notes
ok, found a good candidate video: https://www.twitch.tv/niko/clip/DeliciousRelentlessAxePMSTwin

downloaded video

now to split it up into frames using `ffmpeg`

`ffmpeg.exe -i '.\AT-cm 670698522.mp4' 'frames/$filename%04d.jpg'`

using LabelImg to annotate frames: https://github.com/tzutalin/labelImg

