# -*- coding: utf-8 -*-
import zlib, os, logging

dirs = [
    ur"D:\魔法小神童加旋"
    ]

append_format = "[{0}]"

def crc32(filename):
    prev = 0
    for line in open(filename,"rb"):
	    prev = zlib.crc32(line, prev)
    return ("%X"%(prev & 0xFFFFFFFF)).zfill(8)

def CRC():
    for dir in dirs:
        for file in os.listdir(dir):            
            fullpath = os.path.join(dir, file)
            logging.debug("fullpath = " + fullpath)
            if (os.path.isfile(fullpath)):
                base, ext = os.path.splitext(fullpath)
                crc = crc32(os.path.join(dir, file))
                logging.debug("crc32 = " + crc)
                newFullpath = (base + append_format + ext).format(crc)
                logging.debug("newFullpath = " + newFullpath)
                os.rename(fullpath, newFullpath)

logging.basicConfig(level = logging.DEBUG,
		    format = "%(asctime)s %(name)s %(levelname)s\t - %(message)s")


def RemoveStrFromFilename(dir, s):
    for file in os.listdir(dir):
        if s in file:
                old = os.path.join(dir,file)
                new = os.path.join(dir, file.replace(s, ""))
                os.rename(old, new)

if __name__ == "__main__":
    RemoveStrFromFilename(ur"D:\鋼の錬金術師\钢炼Ⅰ", "(DVD.640x480.WMV9)")
