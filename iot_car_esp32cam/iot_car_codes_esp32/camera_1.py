import camera

camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)

camera.flip(1)
# left / right
camera.mirror(1)

# framesize
camera.framesize(camera.FRAME_QVGA)
#camera.framesize(camera.FRAME_240X240)
# The options are the following:
# FRAME_240X240
# FRAME_96X96 FRAME_QQVGA FRAME_QCIF FRAME_HQVGA FRAME_240X240
# FRAME_QVGA FRAME_CIF FRAME_HVGA FRAME_VGA FRAME_SVGA
# FRAME_XGA FRAME_HD FRAME_SXGA FRAME_UXGA FRAME_FHD
# FRAME_P_HD FRAME_P_3MP FRAME_QXGA FRAME_QHD FRAME_WQXGA
# FRAME_P_FHD FRAME_QSXGA
# Check this link for more information: https://bit.ly/2YOzizz

# special effects
camera.speffect(camera.EFFECT_NONE)
# The options are the following:
# EFFECT_NONE (default) EFFECT_NEG EFFECT_BW EFFECT_RED EFFECT_GREEN EFFECT_BLUE EFFECT_RETRO

# white balance
camera.whitebalance(camera.WB_SUNNY)
# The options are the following:
# WB_NONE (default) WB_SUNNY WB_CLOUDY WB_OFFICE WB_HOME

# saturation
camera.saturation(0)
# -2,2 (default 0). -2 grayscale 

# brightness
camera.brightness(0)
# -2,2 (default 0). 2 brightness

# contrast
camera.contrast(0)
#-2,2 (default 0). 2 highcontrast

# quality

# 10-63 lower number means higher quality
def take_photo(qualityy):
    camera.quality(qualityy) #between 10-63 lower number means higher quality
    buf = camera.capture()
    #print(len(buf))
    return buf

def camera_deinit():
    camera.deinit()
