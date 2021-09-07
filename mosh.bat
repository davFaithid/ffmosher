cd "%~dp0"
mkdir frames 2>NUL
mkdir moshed 2>NUL
ffmpeg -i "%~1" frames/"%%04d".bmp
for /f %%Q in ('dir /b frames') DO py -3 mosh.py -i frames/%%Q -f volume=volume=3,bass=g=3:f=110:w=0.6,aformat=channel_layouts=mono,chorus=0.5:0.5:1:0.1:1:2 -o moshed/%%Q 
ffmpeg -i moshed/"%%04d.bmp" -c:a h264 -crf 30 -r 24 "moshed.mp4"
pause