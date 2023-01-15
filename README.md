# ffmosher
 Datamoshing with FFmpeg

Drag and drop video onto `mosh.bat` to create a datamoshed video.

To datamosh an image, please ensure the file is in a `bitmap (.bmp)` format.

Then simply run 

```
py -3 mosh.py -i input.bmp -f filter -o output.bmp
```

## Filters

For filters, you must use [FFmpeg's filters](https://ffmpeg.org/ffmpeg-filters.html) using the `-f` or `--filter` command.

For example:

```
py -3 mosh.py -i input.bmp -f volume=volume=3,bass=g=3:f=110:w=0.6 -o output.bmp
```

[Here is a list of some good filters with examples.](FILTERS.md)

## Note

Currently this is just a proof of concept. In future I will allow for customizable filters.

At the moment any outputted video is mute.

The idea for this project came from [here](https://www.reddit.com/r/datamoshing/comments/9s0los/datamoshd_a_screenshot_with_audacity_came_out/?utm_source=share&utm_medium=web2x&context=3)

## How does this work?

As was demonstrated in the Reddit post, you can use audio filters to distort images. I thought about automating that process using FFmpeg instead of Audacity however.

Currently if you want to change the default filter, you will have to manually edit the `mosh.py`. I will be adding customizable filters sometime in the future.

## Demonstration

10 second clip of [Big Buck Bunny](https://peach.blender.org/) (Note: Gif compression reduces some of the detail.)

| [Original](https://imgur.com/cFIGbZU) | [Datamoshed](https://imgur.com/MM1nzGl) |
| :------: | :--------: |
|![Original](https://i.imgur.com/cFIGbZU.gif)|![Datamosh](https://i.imgur.com/MM1nzGl.gif)|

If the above images aren't displaying, please visit [here](https://imgur.com/a/zc87MqN).
