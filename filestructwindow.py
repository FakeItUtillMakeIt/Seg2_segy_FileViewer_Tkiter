#文件结构窗口

from tkinter import *
import segyio
import struct
import datastructwindow as dsw


def vloume_show(listbox,filehand,file_format):
    #filepath=filepath
    listbox.delete(0,END)
    if file_format=='sgy':
        vloume_header=filehand.text[0].decode()
        s=0
        e=1
        for item in range(1,41):
            listbox.insert(END,vloume_header[s*80:e*80])
            s+=1
            e+=1
    elif file_format=='sg2' or file_format=='dat':
        listbox.insert(END,'未读到卷头')
    else:
        pass

def binary_show(listbox,filehand,file_format):
    #filepath=filepath
    listbox.delete(0,END)
    if file_format=='sgy':
        bin_header=filehand.bin
        count=len(bin_header)
        bin_list=bin_header.keys()
        for item in range(count):
            listbox.insert(END,str(bin_list[item])+':'+str(bin_header.get(bin_list[item])))
    elif file_format=='sg2' or file_format=='dat':
        listbox.insert(END,'未读到二进制文件头')
    else:
        pass


def trace_show(listbox,filehand,file_format):
    #filepath=filepath
    listbox.delete(0,END)
    if file_format=='sgy':
        trace_header=filehand.header
        total_trace=trace_header.length#总道数
        trace_sample=filehand.trace.shape#每道采样点
        #子窗口
        struct_win=Toplevel()
        dsw.show_traceheader(struct_win,filehand,file_format)
    elif file_format=='sg2' or file_format=='dat':
        trace_header=filehand.stats
        total_trace=filehand.count()
        trace_sample=filehand[0].data.shape[0]
        # 子窗口
        struct_win = Toplevel()
        dsw.show_traceheader(struct_win, filehand,file_format)

def data_show(listbox,filehand,file_format):
    #filepath=filepath
    listbox.delete(0,END)
    #trace_data=filehand.trace[trace_num]
    #listbox.insert(END,'第{}道数据采样点:'.format(trace_num))
    data_win=Toplevel()
    dsw.show_tracedata(data_win,filehand,file_format)
    
def show_filestruct(filehand,file_format):
    struct_window=Toplevel()
    if file_format=='sgy':
        struct_window.title('SegY文件信息查看')
    elif file_format=='sg2':
        struct_window.title('Seg2文件信息查看')
    elif file_format=='dat':
        struct_window.title('Dat文件信息查看')
    else:
        pass

    frame_option=Frame(master=struct_window)
    frame_option.grid(row=0,columnspan=4,column=0)

    #filepath=r'E:/Users/LiJin/Desktop/fw/fw.sgy'
    #filehand=segyio.open(filepath,'rb',strict=False)

    vloume_header=Button(master=frame_option,text='卷头',bd=5,
                       height=1,relief=GROOVE,font='华康少女字体,30',
                         fg='green',width=20,
                         command=lambda:vloume_show(listbox,filehand,file_format))
    binary_header=Button(master=frame_option,text='二进制文件头',bd=5,
                       height=1,relief=GROOVE,font='华康少女字体,30',
                         fg='green',width=20,
                         command=lambda:binary_show(listbox,filehand,file_format))
    trace_header=Button(master=frame_option,text='道头',bd=5,
                       height=1,relief=GROOVE,font='华康少女字体,30',
                         fg='green',width=20,
                        command=lambda:trace_show(listbox,filehand,file_format))
    data_info=Button(master=frame_option,text='数据',bd=5,
                       height=1,relief=GROOVE,font='华康少女字体,30',
                         fg='green',width=20,
                         command=lambda:data_show(listbox,filehand,file_format))

    vloume_header.grid(row=0,column=0)
    binary_header.grid(row=0,column=1)

    trace_header.grid(row=0,column=2)
    data_info.grid(row=0,column=3)

    scrollbar=Scrollbar(master=frame_option,relief=GROOVE,
                        bd=5)
    scrollbar.grid(row=1,rowspan=5,column=4,sticky=N+S)
    listbox=Listbox(master=frame_option,bd=5,yscrollcommand=scrollbar.set,
                       height=20,relief=GROOVE,font='华康少女字体,30',
                         fg='green',width=88)
    listbox.grid(row=1,rowspan=5,column=0,columnspan=4)

    scrollbar.config(command=listbox.yview)

    

    

