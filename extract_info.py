import subprocess as sb
import logging,re,sys,os

logger=logging.getLogger('extract_info.py')
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s :%(name)s :%{message}s')
file_handler=logging.FileHandler('log.txt')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



def latest_file():
    data=sb.Popen(["ls -lrt"],stdout=sb.PIPE,shell=True)
    file=data.communicate()[0].decode('utf-8').split("\n")[-2]
    req_file=file.split(" ")[-1]
    return "Required file : {0}".format(req_file)


def  cat_cmd(file_path):
    print(file_path)
    data=sb.Popen(["cat {0}".format(file_path)],stdout=sb.PIPE,shell=True)
    return data.communicate()[0].decode('utf-8')


def full_path(file_name):
    path_wo_file_name=sb.Popen(["pwd"],stdout=sb.PIPE,shell=True).communicate()[0].decode('utf-8')
    print(path_wo_file_name)
    return f'{path_wo_file_name[:-2]}/{file_name}'


def get_mac():
    bin_data=sb.Popen(["ifconfig"],stdout=sb.PIPE,shell=True)
    data=bin_data.communicate()[0].decode('utf-8')
    result=re.findall(r'HWaddr \S+',data,re.I)
    logger.debug(f"result is :{result}")
    result[-1]=result[-1].replace("HWaddr ","")
    return result[-1]


def max_file(folder_name):
    data=sb.Popen([f"cd;cd {folder_name};ls -S"],stdout=sb.PIPE,shell=True)
    req=data.communicate()[0].decode('utf-8').split()
    if len(req) == 0:
        print("sorry no files found")
        sys.exit()
        #logger.exception("please try again")
    else:
        return req[0]


print(max_file('Documents'))
