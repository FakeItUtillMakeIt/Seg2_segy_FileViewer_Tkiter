#数据结构窗口
from tkinter import *
import os

#道头函数
def show_traceheader(root,filehand,file_format):
    frame1=Frame(master=root,width=80,height=20)
    frame1.grid(row=2,columnspan=5,column=0)

    label1=Label(master=root,text='滑动以选择道数:')
    label1.grid(row=0,sticky=W)

    if file_format=='sgy':
        tracelen=filehand.header.length
    elif file_format=='sg2' or file_format=='dat':
        tracelen=filehand.count()
    else:
        pass

    s1=Scale(master=root,from_=0,to=tracelen-1,orient=HORIZONTAL,
             length=200,tickinterval=tracelen-1)
    s1.grid(row=1,columnspan=4,sticky=W+E)

    def get_trace(filehand,file_format):
        listbox1.delete(0,END)
        #道名称
        trace_num=s1.get()
        print('trace number:{}'.format(trace_num))
        #道参数数据
        if file_format=='sgy':
            trace_head=filehand.header[trace_num]
            #道参数
            head_list=trace_head.keys()
            #道参数个数
            count=len(head_list)
            txtpath = r"D:\桌面\智能地球物理\柴老师\数据\txt\41dp\trace1.txt"
            fileh = open(txtpath, mode='a')
            fileh.write('道头参数')
            for item in range(count):
                listbox1.insert(END,str(head_list[item])+':'+str(trace_head[head_list[item]]))
                fileh.write('\n')
                fileh.write(str(head_list[item])+':'+str(trace_head[head_list[item]]))
            fileh.write('\n')
            fileh.close()
        elif file_format=='sg2' or file_format=='dat':
            for item in (filehand.traces[trace_num].stats):
                item1=filehand.traces[trace_num].stats.get(item)
                listbox1.insert(END,str(item)+':'+str(item1))
        else:
            pass

    button1=Button(master=root,text='选择',command=lambda:get_trace(filehand,file_format))
    button1.grid(row=1,column=4)

    scrollbar=Scrollbar(master=frame1,relief=GROOVE,
                        bd=5)
    scrollbar.grid(row=0,rowspan=5,column=4,sticky=N+S)

    listbox1=Listbox(master=frame1,width=80,bd=5,yscrollcommand=scrollbar.set,
                       height=20,relief=GROOVE,font='华康少女字体,30',
                         fg='green')
    listbox1.grid(row=0)
    scrollbar.config(command=listbox1.yview)


#道数据
def show_tracedata(root,filehand,file_format):
    frame1=Frame(master=root,width=80,height=20)
    frame1.grid(row=2,columnspan=5,column=0)

    label1=Label(master=root,text='滑动以选择道数:')
    label1.grid(row=0,sticky=W)

    if file_format=='sgy':
        tracelen = filehand.header.length
    elif file_format=='sg2' or file_format=='dat':
        tracelen = filehand.count()
    else:
        pass
    #samplelen=filehand.trace.shape

    s1=Scale(master=root,from_=0,to=tracelen-1,orient=HORIZONTAL,
             length=200,tickinterval=tracelen-1)
    s1.grid(row=1,columnspan=4,sticky=W+E)

    def get_trace(filehand,file_format):
        listbox1.delete(0,END)
        trace_num=s1.get()
        print('trace number:{}'.format(trace_num))
        listbox1.insert(END,'第{}道数据采样点:'.format(trace_num+1))
        if file_format=='sgy':
            trace_data=filehand.trace[trace_num]

            txtpath = r"D:\桌面\智能地球物理\柴老师\数据\txt\41dp\trace1.txt"
            fileh = open(txtpath, mode='a')
            fileh.write('道数据')
            for item in range(0,filehand.trace.shape):
                listbox1.insert(END,'采样点{}:{}'.format(item+1,trace_data[item]))
                fileh.write('\n')
                fileh.write('采样点{}:{}'.format(item+1,trace_data[item]))
        elif file_format=='sg2' or file_format=='dat':
            trace_data=filehand.traces[trace_num].data
            count=0
            for item in trace_data:
                count+=1
                listbox1.insert(END,'采样点{}:{}'.format(count,item))


    button1=Button(master=root,text='选择',command=lambda:get_trace(filehand,file_format))
    button1.grid(row=1,column=4)

    scrollbar=Scrollbar(master=frame1,relief=GROOVE,
                        bd=5)
    scrollbar.grid(row=0,rowspan=5,column=4,sticky=N+S)

    listbox1=Listbox(master=frame1,width=80,bd=5,yscrollcommand=scrollbar.set,
                       height=20,relief=GROOVE,font='华康少女字体,30',
                         fg='green')
    listbox1.grid(row=0)
    scrollbar.config(command=listbox1.yview)


def get_alldata(filehand):
    for num in range(filehand.header.length):
        trace_head=filehand.header[num]
        txtpath = r"D:\桌面\智能地球物理\柴老师\数据\txt\41dp\trace"+str(num+1)+".txt"
        fileh = open(txtpath, mode='a')
        fileh.write('道头参数')
        head_list=trace_head.keys()
        for item in head_list:
            fileh.write('\n')
            fileh.write(str(head_list[item])+':'+str(trace_head[head_list[item]]))


        trace_data=filehand.trace[num]
        fileh.write('\n')
        fileh.write('道数据')
        for item in range(trace_data.shape):
            fileh.write('\n')
            fileh.write('采样点{}:{}'.format(item + 1, trace_data[item]))

        fileh.close()

