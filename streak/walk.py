import os




def walk(dir):



    a = os.listdir(dir)

    # print(a)

    dir_name = []
    file_name = []

    # for i in a:

    #     if os.path.isdir(i):
    #         dir_name.append(i)


    # for i in a:
    #     print(i[:10],os.path.isdir(os.path.join(dir,i)))

        # else:
        #     file_name.append(i)



    dir_name = [os.path.join(dir,i) for i in a if os.path.isdir(os.path.join(dir,i))]
    file_name = [os.path.join(dir,i) for i in a if os.path.isfile(os.path.join(dir,i))]


    res = [os.path.abspath(os.curdir),dir_name,file_name]

    # print(dir_name)

    if not file_name and not dir_name:
        print('->'.join(os.path.abspath(os.path.join(dir,os.curdir)).split(os.path.abspath(root))[1].split('/')))
        # # os.path.abspath(os.path.curdir).split(root)[1].split()
        # print(os.path.abspath(os.path.curdir))
        # print(file_name, dir_name, os.path.abspath(os.path.join(dir,os.curdir)))

    for f in file_name:
        f_path = os.path.abspath(f)
        # print(f_path)
        print('->'.join(f_path.split(os.path.abspath(root))[1].split('/')))



    for d in dir_name:
        walk(os.path.join(dir,d))





root = '/home/pybot/Desktop/streak'

walk(root)
