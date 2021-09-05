ffmpeg -i "%~1" frames/"%%04d".bmp
for /f %%Q in ('dir /b frames') DO py -3 mosh.py frames/%%Q moshed/%%Q 
ffmpeg -i moshed/"%%04d.bmp" -c:a h264 -crf 30 -r 24 "moshed.mp4"