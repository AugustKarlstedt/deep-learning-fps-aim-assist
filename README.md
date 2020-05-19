# deep learning aim assist
idea: use off-the-shelf object detector to draw bounding boxes around enemies in first person shooter games

![1](rendered/fps-1.gif)

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

## examples
here's some examples from the first iteration

![2](rendered/fps-2.gif)
![3](rendered/fps-3.gif)

## todo
well, definitely collect more data. see if it generalizes. make it run LIVE on a real game of CS:GO and see if I get VAC banned? 😛 Though I would imagine this wouldn't result in a VAC ban. FRAPS or OBS or other tools draw over the screen just fine. Hmm
