from PIL import Image
from PIL.ExifTags import TAGS

# 디렉토리 순회
# 같은 이미지 추출
# EXIF 같은 날짜, 위치 기록
# 얼굴, 시간, 장소


def proc_image_file(dir, fname):
    imgfile = f'{dir}/{fname}'
    try:
        img = Image.open(imgfile)
        meta_data = img._getexif()
        img.close()

        taglabel = {}

        for tag, value in meta_data.items():
            decoded = TAGS.get(tag, tag)
            taglabel[decoded] = value

        #print(meta_data)
        # 36867은 생성 날짜
        if meta_data is not None :
            date_create = None
            Latitude = None
            Longitude = None
            m_keys =  taglabel.keys()

            if 'DateTimeOriginal' in m_keys:
                date_create =taglabel['DateTimeOriginal']

            try:

                if 'GPSInfo' in m_keys:
                    Latitude = taglabel['GPSInfo'][2]
                if 'GPSInfo' in m_keys:
                    Longitude = taglabel['GPSInfo'][4]
            except KeyError:
                pass
                #print('Key Error')

            print(f'{imgfile} ({date_create}, {Latitude}, {Longitude})')
            return [imgfile, date_create, Latitude, Longitude]
        else:
            return []
    except IOError:
        pass
        #print(f'IOERR {imgfile}')
    except AttributeError :
        pass
        #print(f'AttrERR {imgfile}')



# img0 = Image.open('e:/projects/개인/nas_320190602_203936.jpg')
# meta_data = img._getexif()
# print(meta_data)