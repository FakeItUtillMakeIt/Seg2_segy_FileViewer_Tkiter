import segyio
import os



def get_alldata(filehand):
    print(filehand._filename[:-4])

    for num in range(filehand.header.length):
        print(num)
        trace_head=filehand.header[num]

        txtpath = filehand._filename[:-4]+r"\trace"+str(num+1)+".txt"
        if os.path.exists(txtpath):
            pass
        fileh = open(txtpath, mode='a')

        fileh.write('道头参数')
        head_list=trace_head.keys()
        for item in range(len(head_list)):
            fileh.write('\n')
            print(item)
            fileh.write(str(head_list[item])+':'+str(trace_head[head_list[item]]))

        trace_data=filehand.trace[num]
        fileh.write('\n')
        fileh.write('道数据')

        for item in range(trace_data.shape[0]):
            fileh.write('\n')
            print(item)
            fileh.write('采样点{}:{}'.format(item + 1, trace_data[item]))

        fileh.close()
    print('finish')


filename=['D:\\桌面\\智能地球物理\\柴老师\\数据\\数据\\41dp.sgy','D:\\桌面\\智能地球物理\\柴老师\\数据\\数据\\284dp.sgy','D:\\桌面\\智能地球物理\\柴老师\\数据\\数据\\452dp.sgy']



for file in filename:
    filehand = segyio.open(filename=file, mode='rb', strict=False)
    get_alldata(filehand)