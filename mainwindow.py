from tkinter import *
from tkinter.filedialog import *
import threading
import segyio
import filestructwindow as fsw
from obspy.io.seg2 import seg2


root=Tk()
root.title('SegY/Seg2/DAT文件读取工具 V2.0')

frame1=Frame(master=root,padx=5,pady=5)
frame1.grid(row=0,columnspan=8,column=0)

label_file=Label(master=frame1,text='请选择SegY/Seg2/DAT文件:',
                 anchor=W,borderwidth=5,font='华康少女字体,30',fg='green',
                relief=GROOVE)
label_file.grid(row=0,column=0)

filename=StringVar()

entry_file=Entry(master=frame1,textvariable=filename,bd=5,relief=GROOVE,width=50)
entry_file.grid(row=0,column=1,columnspan=8)

def get_alldata(filehand):
    print(filehand._filename[:-4])

    #此处应加上文件判断
    for num in range(filehand.header.length):
        print(num)
        trace_head=filehand.header[num]

        txtpath = filehand._filename[:-4]+r"\trace"+str(num+1)+".txt"
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
    print('finish')




#选择文件
def select_file(filename):
    try:
        
        filehandle=askopenfile()
        file_name=filehandle.name
        filename.set(file_name)
        
        return file_name
    except AttributeError:
        pass

button_file=Button(master=frame1,text='选择文件',bd=5,
                   height=1,relief=GROOVE,font='华康少女字体,30',fg='green',
                   command=lambda:select_file(filename))
button_file.grid(row=0,column=9,sticky=W)

#界面排版
frame2=Frame(master=root,padx=5,pady=5)
frame2.grid(row=1,columnspan=8,column=0,sticky=W+E)

text_info='''
本程序可以对多种SegY/Seg2/DAT文件进行分析\n

可分析文件种类：\n
 1、有卷头的工作站格式SegY/Seg2/DAT文件\n
 2、无卷头的工作站格式SegY/Seg2/DAT文件\n
 3、有卷头的微机格式SegY/Seg2/DAT文件\n
 4、无卷头的微机格式SegY/Seg2/DAT文件\n


'''
def explain_info():
    listbox.delete(0,END)
    #filepath=r'./explain_text.txt'
    #filehandle=open(filepath,'r')
    data=''
    for line in text_info:
        if line != '\n':
            data+=line
        else:
            listbox.insert(END,data)
    
            data=''
        

button_guide=Button(master=frame2,text='说明信息',bd=5,padx=6,
                   height=1,relief=GROOVE,width=20,anchor=W,
                    font='华康少女字体,30',fg='green',
                    command=explain_info)

#文件信息
def file_info(file):
    listbox.delete(0,END)
    filename=file.get()
    try:
        if filename[-3:]=='sgy' or filename[-3:]=='SGY':
            with segyio.open(filename,'rb',strict=False) as filehand:
                listbox.insert(END,'文件类型:SegY')
                listbox.insert(END, '相关信息:')
                listbox.insert(END,'存放格式:'+str(filehand.endian))
                filehand.close()
        elif filename[-3:]=='sg2' or filename[-3:]=='SG2':
            S=seg2.SEG2()
            data=S.read_file(filename)
            head=data.traces[0].verify()
            listbox.insert(END,'文件类型:Seg2')
            listbox.insert(END,'相关信息:'+str(head))
        elif filename[-3:]=='dat' or filename[-3:]=='DAT':
            S=seg2.SEG2()
            data=S.read_file(filename)
            head=data.traces[0].verify()
            listbox.insert(END,'文件类型:Dat')
            listbox.insert(END,'相关信息:'+str(head))
        else:
            pass

    except OSError:
        listbox.insert(END,'请先选择SegY/Seg2/DAT文件')

button_fileinfo=Button(master=frame2,text='文件信息',bd=5,padx=6,
                   height=1,relief=GROOVE,width=20,anchor=W,
                    font='华康少女字体,30',fg='green',
                       command=lambda:file_info(filename))

def fileStruct_window(filename):
    filepath=filename.get()
    try:
        if filepath[-3:]=='sgy' or filepath[-3:]=='SGY':
            file_format='sgy'
            filehand=segyio.open(filepath,'rb',strict=False)

        elif filepath[-3:]=='sg2' or filepath[-3:]=='SG2':
            file_format='sg2'
            S=seg2.SEG2()
            filehand =S.read_file(filepath)

        elif filepath[-3:]=='dat' or filepath[-3:]=='DAT':
            file_format='dat'
            S = seg2.SEG2()
            filehand = S.read_file(filepath)
        else:
            pass
        fsw.show_filestruct(filehand,file_format)
        #get_alldata(filehand)

        
    except OSError:
        listbox.delete(0,END)
        listbox.insert(END,'请先选择SegY/Seg2/Dat文件')
    #root.iconify()

button_explain=Button(master=frame2,text='文件结构',bd=5,padx=6,
                   height=1,relief=GROOVE,width=20,anchor=W,
                    font='华康少女字体,30',fg='green',
                      command=lambda:fileStruct_window(filename))
'''
button_headerdata=Button(master=frame2,text='数据道道头',bd=5,
                   height=1,relief=GROOVE)

button_readdata=Button(master=frame2,text='采样数据',bd=5,
                   height=1,relief=GROOVE)
button_traceheader=Button(master=frame2,text='文件信息',bd=5,
                   height=1,relief=GROOVE)
button_tracedata=Button(master=frame2,text='各道数据',bd=5,
                   height=1,relief=GROOVE)
button_datascan=Button(master=frame2,text='数据扫描',bd=5,
                   height=1,relief=GROOVE)
'''

#界面布局
button_guide.grid(row=0,column=0,columnspan=3)
button_fileinfo.grid(row=0,column=3,columnspan=3)
button_explain.grid(row=0,column=6,columnspan=3)
'''
button_headerdata.grid(row=0,column=3)
button_traceheader.grid(row=0,column=4)
button_tracedata.grid(row=0,column=5)
button_datascan.grid(row=0,column=6)
button_readdata.grid(row=0,column=7)
'''

scrollbar=Scrollbar(master=frame2,relief=GROOVE,bd=5)
scrollbar.grid(row=1,column=9,sticky=N+S)

listbox=Listbox(master=frame2,yscrollcommand=scrollbar.set,
                relief=GROOVE,bd=5)
listbox.grid(row=1,columnspan=9,sticky=W+E+S)

scrollbar.config(command=listbox.yview)

mainloop()
