import os
from image_mgr import proc_image_file

dir_start ='e:\\'



def get_img_list(name_dir):
    list_meta =[]

    for (path, d_anem, f_name) in os.walk(name_dir):
        list_img =[]
        for f_item in f_name:
            if '.jpeg' in f_item or '.png' in f_item or '.jpg' in f_item :
                list_img.append(f_item)
                meta=proc_image_file(path, f_item)

                if meta is not None and len(meta)>0:
                    list_meta.append(meta)

        # if len(list_img) > 0:
        #     print(f'{path}/{list_img}')

    print(len(list_meta))


get_img_list(dir_start)