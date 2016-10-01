#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import math
import binascii


import jpegtags as JT


def findmarker(trg, mark):
    pos = {}
    marklength = len(mark)
    matchcount = 0
    for i in range(len(trg)):
        cmpstr = trg[i:i+marklength]
        #print "cmpstr : " + cmpstr
        #print "mark : " + mark
        #print "i : {0:d}".format(i)
        #if i == 30:
        #    quit()
        if mark == cmpstr:
            #print "find : " + cmpstr
            pos[matchcount] = i
            matchcount += 1
            #print "i : {0:d}".format(i)

    #print "mark : {0}".format(mark)
    #for a in range(len(pos)):
    #    print "pos : {0:d}".format(pos[a])

    return pos

def ifdprocess(trg, startpos, a200code, exifoffset, info, processkind):
    ifddata = info
    #print "trg : {0}".format(trg)
    #print "len(trg) : {0}".format(len(trg))
    #print "a200code : {0}".format(a200code)
    #print "startpos : {0:d}".format(startpos)
    #print "startpos : {0}".format(startpos)

    #print "trg : {0}".format(trg)
    ifdfc = trg[startpos:startpos+4]
    #print "ifdfc : {0}".format(ifdfc)
    ifdfieldcount = convert10(endianprocess(ifdfc, a200code))
    ifd = trg[startpos:startpos+((2+ifdfieldcount*12+4)*2)]
    ifdfields = ifd[4:]
    nextifdoffset = ifd[-8:]
    nextifdoffsetvalue = convert10(endianprocess(nextifdoffset, a200code))
    #print "ifdfc : {0}".format(ifdfc)
    #print "ifdfieldcount : {0:d}".format(ifdfieldcount)
    #print "ifd : {0}".format(ifd)
    #print "ifdfields : {0}".format(ifdfields)
    #print "nextifdoffset : {0}".format(nextifdoffset)
    #print "nextifdoffsetvalue : {0:d}".format(nextifdoffsetvalue)
    #print ": : {0}".format(trg[startpos:startpos+32])

    #
    field = {}
    for i in range(ifdfieldcount):
        start = i * (12 * 2)
        end = (i + 1) * (12 * 2)
        ifdfielddata = ifdfields[start:end]
        #print "start : {0:d}".format(start)
        #print "end : {0:d}".format(end)
        #print ifdfields[start:end]
        #print "ifdfielddata : {0}".format(ifdfielddata)
        field[i] = {
                'data' : ifdfielddata,
                'tag' : ifdfielddata[0:4],
                'type' : ifdfielddata[4:8],
                'count' : ifdfielddata[8:16],
                'offset' : ifdfielddata[16:24]
                }

    for i in range(len(field)):
        print "field[{0:d}].data : {1}".format(i, field[i]['data'])
        print "field[{0:d}].tag : {1}".format(i, field[i]['tag'])
        print "field[{0:d}].type : {1}".format(i, field[i]['type'])
        print "field[{0:d}].count : {1}".format(i, field[i]['count'])
        print "field[{0:d}].offset : {1}".format(i, field[i]['offset'])
        field[i]['tag'] = endianprocess(field[i]['tag'], a200code)
        field[i]['type'] = convert10(endianprocess(field[i]['type'], a200code))
        field[i]['count'] = convert10(endianprocess(field[i]['count'], a200code))
        if processkind == 'exif':
            kind = "exiftags"
        elif processkind == 'gps':
            kind = "gpstags"
        tagkind = ""
        tagdescription = ""
        tagkind = JT.TAG_LIST[kind][field[i]["tag"]]["tag"] or "[Not Found]"
        tagdescription = JT.TAG_LIST[kind][field[i]["tag"]]["description"] or "[Not Found]"
        field[i]["tagkind"] = tagkind
        field[i]["tagdescription"] = tagdescription
        tagtype = field[i]["type"]
        datalength = JT.TYPE_MEAN[str(tagtype)]["length"] * field[i]["count"]
        field[i]["datalength"] = datalength
        tagtype = JT.TYPE_MEAN[str(tagtype)]["name"]
        field[i]["typekind"] = tagtype
        #print "tagkind : {0}".format(tagkind)
        #print "tagdescription : {0}".format(tagdescription)
        #print "tagtype : {0}".format(tagtype)
        #print "datalength : {0:d}".format(datalength)
        if field[i]["datalength"] <= 4:
            #if field[i]["typekind"] == "SHORT" or field[i]["typekind"] == "BYTE":
            field[i]["offset"] = field[i]["offset"][0:4]
            #elif field[i]["typekind"] == "ASCII":

            if field[i]["typekind"] != "ASCII":
                #print "field[i][\"offset\"] : {0}".format(field[i]["offset"])
                #field[i]["offset"] = convert10(endianprocess(field[i]["offset"], a200code))
                field[i]["offset"] = endianprocess(field[i]["offset"], a200code)
            #value = str(field[i]["offset"])
            value = field[i]["offset"]
        else:
            field[i]["offset"] = convert10(endianprocess(field[i]["offset"], a200code))
            offsetpos = field[i]["offset"]
            start = exifoffset + (offsetpos * 2)
            end = exifoffset + (offsetpos * 2) + field[i]["datalength"] * 2
            value = trg[start:end]

        if field[i]["tagkind"] != 'MakerNote':
            #print "value : {0}".format(value)
            #print "typekind : {0}".format(field[i]["typekind"])
            #print "count : {0}".format(field[i]["count"])
            #ifddata[field[i]["tagkind"]] = getresult(value, field[i]["typekind"], field[i]["count"])
            ifddata[field[i]["tagkind"]] = getresult(value, field[i]["typekind"], field[i]["count"])

    return ifddata, nextifdoffsetvalue

def getresult(value, tagtype, count):
    #print "value : {0}".format(value)
    #print "type(value) : {0}".format(type(value))
    #print "tagtype : {0}".format(tagtype)
    #print "count : {0}".format(count)

    result = ""
    if tagtype == "ASCII":
        jiscode = {
                "00" : ".", "84" : ".", "98" : ".", "20" : " ",
                "21" : "!", "22" : '"', "23" : "#", "24" : "$",
                "25" : "%", "26" : "&", "27" : "'", "28" : "(",
                "29" : ")", "2a" : "*", "2b" : "+", "2c" : ",",
                "2d" : "-", "2e" : ".", "2f" : "/", "30" : "0",
                "31" : "1", "32" : "2", "33" : "3", "34" : "4",
                "35" : "5", "36" : "6", "37" : "7", "38" : "8",
                "39" : "9", "3a" : ":", "3b" : ";", "3c" : "<",
                "3d" : "=", "3e" : ">", "3f" : "?", "40" : "@",
                "41" : "A", "42" : "B", "43" : "C", "44" : "D",
                "45" : "E", "46" : "F", "47" : "G", "48" : "H",
                "49" : "I", "4a" : "J", "4b" : "K", "4c" : "L",
                "4d" : "M", "4e" : "N", "4f" : "O", "50" : "P",
                "51" : "Q", "52" : "R", "53" : "S", "54" : "T",
                "55" : "U", "56" : "V", "57" : "W", "58" : "X",
                "59" : "Y", "5a" : "Z", "5b" : "", "5c" : "\\",
                "5d" : "",  "5e" : "^", "5f" : "_", "60" : "`",
                "61" : "a", "62" : "b", "63" : "c", "64" : "d",
                "65" : "e", "66" : "f", "67" : "g", "68" : "h",
                "69" : "i", "6a" : "j", "6b" : "k", "6c" : "l",
                "6d" : "m", "6e" : "n", "6f" : "o", "70" : "p",
                "71" : "q", "72" : "r", "73" : "s", "74" : "t",
                "75" : "u", "76" : "v", "77" : "w", "78" : "x",
                "79" : "y", "7a" : "z", "7b" : "{", "7c" : "|",
                "7d" : "}", "7e" : "~",
                }

        for i in range(0, len(value), 2):
            #print "code : {0}".format(jiscode[value[i:i+2]])
            result = result + jiscode[value[i:i+2]]

    elif tagtype == "UNDEFINED":
        result = value
    else:
        values = {}
        typesize = 0
        for key, p in JT.TYPE_MEAN.items():
            if tagtype == p["name"]:
                typesize = p["length"] * 2
                break

        value_count = 0
        #print "typesize : {0:d}".format(typesize)
        #print "len(value) : {0:d}".format(len(value))
        #split
        for i in range(0, len(value), typesize):
            #print value[i:i+typesize]
            values[value_count] = value[i:i+typesize]
            value_count += 1

        #for i,o in values.items():
        #    print "{0} : {1}".format(i,o)

        tmp = 0
        for counts in range(len(values)):
            #print "values[counts] : {0}".format(values[counts])
            if tagtype == "BYTE":
                tmp = math.fabs(int(values[counts], 16))
            elif tagtype == "SHORT":
                tmp = int(values[counts], 16)
                tmp = math.fabs(tmp)
            elif tagtype == "LONG":
                tmp = math.fabs(math.floor((int(values[counts], 16))))
            elif tagtype == "RATIONAL":
                res1 = int(values[counts][0:8], 16)
                res2 = int(values[counts][8:16], 16)
                tmp = res1 / res2
            elif tagtype == "SBYTE":
                tmp = math.fabs(int(values[counts], 16))
            elif tagtype == "SSHORT":
                tmp = int(values[counts], 16)
            elif tagtype == "SLONG":
                tmp = int(values[counts], 16)
            elif tagtype == "SRATIONAL":
                res1 = int(values[counts][0:8], 16)
                res2 = int(values[counts][8:16], 16)
                tmp = res1 / res2
            elif tagtype == "FLOAT":
                tmp = int(values[counts], 16)
            elif tagtype == "DFLOAT":
                tmp = int(values[counts], 16)
            else:
                tmp = "[Error]"

            if type(tmp) == 'str':
                result += tmp
            else:
                if count == 1 or count == 0:
                    result = tmp
                else:
                    #ここは修正必要
                    result = tmp


    #print "RESULT : {0}".format(result)
    return result


def endianprocess(trg, fixedcode):
    #print "-- function endianprocess --"
    #print "[ before endian process : {0} ]".format(trg)
    #print "len(trg) : {0:d}".format(len(trg))
    value = ""
    if fixedcode == "002a":
        return trg
    elif fixedcode == "2a00":
        count = len(trg)
        for i in range(count, 0, -2):
            #print "[ i : {0:d} ]".format(i)
            #print "[ value : {0} ] ".format(value)
            #print "{0}".format(trg[i-2]+trg[i-1])
            value = value + trg[i-2] + trg[i-1]
    else:
        print("process error : ")

    #print "[ after endian process : {0} ]".format(value)
    return value

def convert10(trg):
    #print "-- function convert10 --"
    #print "trg : {0}".format(trg)
    sumvalue = 0
    sumvalue = int(trg, 16)
    #print "int(trg,16): {0:d}".format(int(trg,16))
    #print "sumlvaue: {0}".format(sumvalue)

    return sumvalue


if len(sys.argv) != 2:
    print "Usage : python Jpeglather.py <jpgfile>"
else:
    info = {}
    trgname = sys.argv[1]
    print "[INPUT FILE NAME ] : %s" % trgname
    try:
        f = open(trgname, "rb")
    except:
        print "Error : "

    else:
        data = f.read()
        f.close()

    n = 0
    hexdata = ""
    while n < len(data):
        hexdata = hexdata + binascii.b2a_hex(data[n])
        n += 1
    #print hexdata

    soimarker = "ffd8"
    eoimarker = "ffd9"
    dqtmarker = "ffdb"
    dhtmarker = "ffd4"
    exifmarker = "ffe1"
    soi = findmarker(hexdata, soimarker)
    eoi = findmarker(hexdata, eoimarker)
    dqt = findmarker(hexdata, dqtmarker)
    dht = findmarker(hexdata, dhtmarker)
    exif = findmarker(hexdata, exifmarker)

    if len(soi) != 0:
        print "SOI : {0}".format(soi)
    else:
        print "SOI NOT FOUND"

    if len(eoi) != 0:
        print "EOI : {0}".format(eoi)
    else:
        print "EOI NOT FOUND"

    if len(dqt) != 0:
        print "DOI : {0}".format(dqt)
    else:
        print "DQT NOT FOUND"

    if len(dht) != 0:
        print "DHT : {0}".format(dht)
    else:
        print "DHT NOT FOUND"

    if len(exif) != 0:
        print "EXIF : {0}".format(exif)
        print "exif n : {0:d}".format(len(exif))
        exifzeropos = 0
        for i in range(len(exif)):
            exifn = exif[i]
            exifcode = hexdata[exifn:exifn+4]
            posofseg = exifn + 4
            segmentlength = hexdata[posofseg:posofseg+4]
            posofsegexifcode = posofseg + 4
            segmentexifcode = hexdata[posofsegexifcode:posofsegexifcode+10]
            posoftiffheader = posofsegexifcode + 12
            byteorder = hexdata[posoftiffheader:posoftiffheader+4]
            if exifzeropos == 0:
                exifzeropos = posoftiffheader
            posoffixedcodeintiffheader = posoftiffheader + 4
            a200code = hexdata[posoffixedcodeintiffheader:posoffixedcodeintiffheader+4]
            posofifdoffset = posoffixedcodeintiffheader + 4
            ifdoffset = hexdata[posofifdoffset:posofifdoffset+8]
            #print "exifcode : {0}".format(exifcode)
            #print "exifn : {0}".format(exifn)
            #print "segmentlength : {0}".format(segmentlength)
            #print "posofseg : {0:d}".format(posofseg)
            #print "posofsegexifcode : {0:d}".format(posofsegexifcode)
            #print "segmentexifcode : {0}".format(segmentexifcode)
            #print "posoftiffheader : {0:d}".format(posoftiffheader)
            #print "exifzeropos : {0:d}".format(exifzeropos)
            #quit()
            #print "posoffixedcodeintiffheader : {0:d}".format(posoffixedcodeintiffheader)
            #print "posofifdoffset : {0:d}".format(posofifdoffset)
            #print "byteorder : {0}".format(byteorder)
            #print "a200code : {0}".format(a200code)
            #print "ifdoffset : {0}".format(ifdoffset)
            app1 = hexdata[exifn:(exifn+3)+4+12+4+4+8]
            print "APP1 : {0}".format(app1)
            bigendian = "4d4d"
            littleendian = "4949"
            if byteorder == bigendian:
                print "endian: bigendian"
            elif byteorder == littleendian:
                print "endian: littleendian"
            else:
                print "NOON"
                continue
            #break

            posofifdoffset = convert10(endianprocess(ifdoffset, a200code)) * 2
            print "[posofifdoffset : {0:d}]".format(posofifdoffset)
            posofifd = posofifdoffset + exifzeropos
            print "[posofifd:{0:d}]".format(posofifd)
            processkind = "exif"
            info, nextifdoffset = ifdprocess(hexdata, posofifd, a200code, exifzeropos, info, processkind)

            if nextifdoffset != 0:
                #print "nextifdoffset : {0:d}".format(nexifdoffset)
                info, nextifdoffset = ifdprocess(hexdata, (nextifdoffset * 2) + exifzeropos, a200code, exifzeropos, info, processkind)

        if info["GPSInfo IFD Pointer"] != 0:
            print "[Found GPSInfo IFD Pointer]"
            pos = int(info["GPSInfo IFD Pointer"])
            processkind = "gps"
            #print "pos : {0}".format(pos)
            #print "[exifzeropos : {0}]".format(exifzeropos)
            info, nextifdoffset = ifdprocess(hexdata, pos * 2 + exifzeropos, a200code, exifzeropos, info, processkind)
            if nextifdoffset != 0:
                #print "nextifdoffset : {0:d}".format(nexifdoffset)
                info, nextifdoffset = ifdprocess(hexdata, (nextifdoffset * 2) + exifzeropos, a200code, exifzeropos, info, processkind)
        else:
            print "[ GPSInfo IFD Pointer Not Found ...]"

        if info["Exif IFD Pointer"] != 0:
            print "[Found Exif IFD Pointer]"
            pos = int(info["Exif IFD Pointer"])
            #print "pos : {0}".format(pos)
            processkind = "exif"
            info, nextifdoffset = ifdprocess(hexdata, pos * 2 + exifzeropos, a200code, exifzeropos, info, processkind)
            if nextifdoffset != 0:
                #print "nextifdoffset : {0:d}".format(nexifdoffset)
                info, nextifdoffset = ifdprocess(hexdata, nextifdoffset * 2 + exifzeropos, a200code, exifzeropos, info, processkind)
        else:
            print "[ Exif IFD Pointer Not Found ...]"

    else:
        print "EXIF NOT FOUND"


    print "------------------------------"
    for key, value in info.items():
        print "{0} : {1}".format(key, value)
        #print info

    print "------------------------------"


    #for i in range(len(exif)):
    #    print "[i : {0:d}]".format(i)
    #finally:
    #    print "finally"
    #    f.close()
