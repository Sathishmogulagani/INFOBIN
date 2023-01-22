from tkinter import messagebox as mb
try:
    import pywhatkit as wt
    import mysql.connector as mc
    from datetime import datetime as dt
    import random as ran
    import tkinter as tk
    r=tk.Tk()
    r.title('INFOBIN')
    r.geometry('350x550')
    r.minsize(350,550)
    r.maxsize(350,550)
    r['background']='#856ff8'
    r.config(bg='blue')
    ###INSERT START
    app_var=tk.StringVar()
    psw_var=tk.StringVar()

    def stored():
        #x=""
        app_name=app_var.get()
        orgnl=psw_var.get()
        l=[]
        k=0
        l2=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',1,2,3,4,5,6,7,8,9,0,'@','!','$','%','^','&','*','(',')','~','`',':']
        for i in range(len(orgnl)*2-1):
            if i%2==0:
                l.append(orgnl[k])
                k+=1
            else:
                l.append(str(ran.choice(l2)))
        psw_name=""
        for i in range(len(l)):    
            psw_name+=l[i]
        psw_name=psw_name[::-1]
        #print(psw_name)



        #print(app_name)
        if(app_name and psw_name and len(psw_name)>7):
            try:
                con=mc.connect(host="localhost",user="root",passwd='tozo608',database='INFOBIN')#CHANGE YOUR ROOT NAME ,PASSWORD , DATABASE NAME IN ALL THESE LINE
                cur=con.cursor()
                Q="insert into store(application,password) values(%s,%s)"
                val=(app_name,psw_name)
                cur.execute(Q,val)
                con.commit()
                cur.close()
                con.close()
                mb.showinfo('SECURED','Your Password is Saved!!')
                app_var.set("")
                psw_var.set("")
            except Exception as e:
                mb.showerror('FALSE',e)  
        elif(app_name==""):
            mb.showerror('ERROR','Enter Applicatioin')
        elif(psw_name==""):
            mb.showerror('ERROR','Enter Password')
        elif(len(psw_name)<8):
            mb.showerror('ERROR','Enter Strong Passowd')
            psw_var.set("")
        else:
            pass
    def resetin():
        app_var.set("")
        psw_var.set("")
        
    app=tk.Entry(r,width=20,bd=1,textvariable=app_var)
    psw=tk.Entry(r,width=20,bd=1,textvariable=psw_var,show='°')

    applabel=tk.Label(r,text="APPLICATION :",font='sans 8 bold',bg='blue',fg='white')#,relief=RAISED
    pswdlabel=tk.Label(r,text="PASSWORD :",font='sans 8 bold',bg='blue',fg='white')

    in_b=tk.Button(r,text='STORE',bd=1,font='sans 8 bold',command=stored)
    reset_bin=tk.Button(r,text="RESET",font='sans 8 bold',bd=1,command=resetin)

    #app.pack(side='top',padx=100,pady=10)
    applabel.place(x=20,y=10)
    app.place(x=125,y=10)

    pswdlabel.place(x=33,y=33)
    psw.place(x=125,y=35)

    reset_bin.place(x=125,y=60)
    in_b.place(x=205,y=60)
    #####INSERT OVER ########

    #####UPDATE START #######

    cur_pw=tk.StringVar()
    new_pw=tk.StringVar()


    cur_psw=tk.Entry(r,width=20,bd=1,textvariable=cur_pw)
    new_psw=tk.Entry(r,width=20,bd=1,textvariable=new_pw)

    curlabel=tk.Label(r,text="CURRENT :",font='sans 8 bold',bg='blue',fg='white')
    newlabel=tk.Label(r,text="NEW :",font='sans 8 bold',bg='blue',fg='white')
    def update():
        
        shfl=cur_pw.get()       
        orgnl=new_pw.get()
        l=[]
        k=0
        l2=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',1,2,3,4,5,6,7,8,9,0,'@','!','$','%','^','&','*','(',')','~','`',':']
        for i in range(len(orgnl)*2-1):
            if i%2==0:
                l.append(orgnl[k])
                k+=1
            else:
                l.append(str(ran.choice(l2)))
        new_val=""
        for i in range(len(l)):    
            new_val+=l[i]
        new_val=new_val[::-1]
        

        
        con=mc.connect(host="localhost",user="root",passwd='tozo608',database='INFOBIN')
        cur=con.cursor()
        Q="select password from store"
        cur.execute(Q)
        x=list(cur)
        y=[]
        for i in x:
            y.append(list(i))

        
        if cur_val in y:
            x=cur_val
            cur_val=""
            for i in x:
                cur_val+=i
            cur.close()
            con.close()       
            if cur_val!=new_val:
                try:
                    if(cur_val and new_val and len(new_val)>7):
                        con=mc.connect(host="localhost",user="root",passwd='tozo608',database='INFOBIN')
                        cur=con.cursor()
                        Q="update store set password='"+new_val+"' where password='"+cur_val+"'"
                        cur.execute(Q)
                        con.commit()
                        cur.close()
                        con.close()
                        mb.showinfo('UPDATED','YOUR PASSWORD UPDATED!!')
                        cur_pw.set("")
                        new_pw.set("")
                    elif(cur_val==""):
                        mb.showerror('FALSE','ENTER CURRENT PASSWORD')
                    elif(new_val==""):
                        mb.showerror('FALSE','ENTER NEW PASSWORD')
                    elif(len(new_val)<8):
                        mb.showerror('FALSE','ENTER STRONG PASSWORD')
                    else:
                        pass
                except Exception as e:
                    mb.showerror('FALSE',e)
            else:
                mb.showinfo('FALSE','TRY NEW PASSWORD')
                cur_pw.set("")
                new_pw.set("")
        else:
            mb.showerror('FALSE','INVALID PASSWORD')
            cur_pw.set("")
            new_pw.set("")
    def resetup():
            cur_pw.set("")
            new_pw.set("")
            
    up_b=tk.Button(r,text="UPDATE",bd=1,font='sans 8 bold',command=update)
    reset_bup=tk.Button(r,text="RESET",font='sans 8 bold',bd=1,command=resetup)

    curlabel.place(x=43,y=140)
    cur_psw.place(x=125,y=140)

    newlabel.place(x=68,y=165)
    new_psw.place(x=125,y=165)



    up_b.place(x=195,y=190)
    reset_bup.place(x=125,y=190)


    ####UPDATE OVER####

    ####DELETE START####
    d_app=tk.StringVar()
    d_psw=tk.StringVar()

    dapp=tk.Entry(r,width=20,bd=1,textvariable=d_app)
    dpsw=tk.Entry(r,width=20,bd=1,textvariable=d_psw)
    dapp_label=tk.Label(r,text="APPLICATION :",font='sans 8 bold',bg='blue',fg='white')
    dpsw_label=tk.Label(r,text="PASSWORD :",font='sans 8 bold',bg='blue',fg='white')
    def delete():
        del_app=d_app.get()
        if(del_app):
            a=[del_app]
            con=mc.connect(host="localhost",user="root",passwd='tozo608',database='INFOBIN')
            cur=con.cursor()
            Q="select application from store"
            cur.execute(Q)
            x=[]
            for i in cur:
                x.append(list(i))
            #print(x)
            #print(a)
            if a in x:       
                shfl=d_psw.get()
                es=""
                os=""
                for i in range(len(shfl)):
                    if i%2==0:
                        es+=shfl[i]
                    else:
                        os+=shfl[i]
                del_psw=es+os           
                if(del_psw):
                    a=[del_psw]
                    con=mc.connect(host="localhost",user="root",passwd='tozo608',database='INFOBIN')
                    cur=con.cursor()
                    Q="select password from store"
                    cur.execute(Q)
                    x=[]
                    for i in cur:
                        x.append(list(i))
                    
                    if(a in x):            
                        try:
                            if(del_app and del_psw):     
                                con=mc.connect(host="localhost",user="root",passwd='tozo608',database='INFOBIN')
                                cur=con.cursor()
                                Q="delete from store where application='"+del_app+"' and password='"+del_psw+"'"
                                cur.execute(Q)
                                con.commit()
                                cur.close()
                                con.close()
                                mb.showinfo('DELETED','YOUR DATA ERASED!!')
                                d_app.set("")
                                d_psw.set("")
                            elif(del_app==""):
                                mb.showerror('FALSE','ENTER APPLICATION')
                            elif(del_psw==""):
                                mb.showerror('FALSE','ENTER PASSWORD')
                            elif(len(del_psw)<8):
                                mb.showerror('FALSE','ENTER ACTUAL PASSWORD')
                            else:
                                mb.showerror("FALSE","UNABLE TO DELETE") 
                        except Exception as e:
                            mb.showerror('FALSE',e)
                    else:
                        mb.showerror("FALSE","INVALID PASSWORD")
                else:
                    mb.showerror("FALSE","ENTER PASSWORD")
            else:
                mb.showerror('FALSE','NO MATCHED DATA')
                
    def resetdel():
        d_app.set("")
        d_psw.set("")
        
    dbtn=tk.Button(r,bd=1,text="DELETE",font='sans 8 bold',command=delete)
    reset_bdel=tk.Button(r,bd=1,text="RESET",font='sans 8 bold',command=resetdel)
    dapp_label.place(x=20,y=260)
    dapp.place(x=125,y=260)

    dpsw_label.place(x=33,y=285)
    dpsw.place(x=125,y=285)
    reset_bdel.place(x=125,y=310)
    dbtn.place(x=202,y=310)
    ####DELETE OVER#####


    ####RETRIVE START####
    app_show=tk.StringVar()
    mob_show=tk.StringVar()
    def get():
        appval=app_show.get()
        if(appval):
            a=[appval]
            #print(a)
            con=mc.connect(host="localhost",user="root",passwd='tozo608',database='INFOBIN')
            cur=con.cursor()
            Q="select application from store"
            cur.execute(Q)
            x=[]
            for i in cur:
                x.append(list(i))
            if a in x:
                s=""
                for i in a:
                    s+=i
                Q="select password from store where application='"+s+"'"
                cur.execute(Q)
                x=[]
                for i in cur:
                    x.append(list(i))
                s=""
                for i in x[0]:
                    s+=i
                shfl=s
                os1=""
                print(shfl)
                k=len(shfl)//2
                for i in range(len(shfl)-k):
                    os1+=shfl[i]
                    os1+=shfl[i+k]
                #print(os1)
                mb.showinfo('HERE',os1)
            else:
                mb.showerror("FALSE","NO DATA MATCHED")
        else:
            mb.showerror("FALSE","ENTER APPLICATION")
        app_show.set("")
    def resetshow():
        app_show.set("")
        mob_show.set("")
    def whatme():
        cell=mob_show.get()
        appval=app_show.get()
        if(cell and appval and len(cell)==10):
            now=dt.now()
            h= now.strftime("%H")
            m=now.strftime("%M")
            s=now.strftime('%S')
            h=int(h)
            m=int(m)+2
            #print(h,m,s)
            s=int(s)+2

            a=[appval]
            #print(a)
            con=mc.connect(host="localhost",user="root",passwd='tozo608',database='INFOBIN')
            cur=con.cursor()
            Q="select application from store"
            cur.execute(Q)
            x=[]
            for i in cur:
                x.append(list(i))
            if a in x:
                st=""
                for i in a:
                    st+=i
                Q="select password from store where application='"+st+"'"
                cur.execute(Q)
                x=[]
                for i in cur:
                    x.append(list(i))
                stt=""
                for i in x[0]:
                    stt+=i



                shfl=stt
                os1=""
                k=len(shfl)//2
                for i in range(len(shfl)-k):
                    os1+=shfl[i]
                    os1+=shfl[i+k]

                
                try:
                    #print(type(cell))
                    cell="+91"+cell
                    #print(cell)
                    wt.sendwhatmsg(cell,os1,h,m,s)
                except Exception as e:
                    print(e)
            else:
                mb.showerror('FALSE','NO MATCHED DATA')
        elif(appval==""):
            mb.showerror("FALSE","ENTER APPLICATION")
        elif(cell==""):
            mb.showerror("FALSE","ENTER MOBILE NUMBER")
        elif(len(cell)<10):
            mb.showerror("FALSE","ENTER PROPER MOBILE NUMBER")
            mob_show.set("")
        else:
            mb.showerror("FALSE","UNABLE TO SEND")
            mob_show.set("")
            app_show.set("")
    apps=tk.Entry(r,width=20,bd=1,textvariable=app_show)
    apps_label=tk.Label(r,text="APPLICATION :",font='sans 8 bold',bg='blue',fg='white')
    mob=tk.Entry(r,width=20,bd=1,textvariable=mob_show)
    mob_label=tk.Label(r,text="MOBILE NO :",font='sans 8 bold',bg='blue',fg='white')

    get_b=tk.Button(r,text="SHOW ME",font='sans 8 bold',bd=1,command=get)
    reset_bget=tk.Button(r,text="RESET",font='sans 8 bold',bd=1,command=resetshow)
    whats_bget=tk.Button(r,text="WHATSAPP",font='sans 8 bold',bd=1,command=whatme)

    apps_label.place(x=20,y=410)
    apps.place(x=125,y=410)

    mob_label.place(x=33,y=435)
    mob.place(x=125,y=435)

    get_b.place(x=185,y=460)
    reset_bget.place(x=125,y=460)
    whats_bget.place(x=265,y=432)

    def des():
        r.destroy()
    dis=tk.Button(r,text="CLOSE",bd=1,font='sans 8 bold',command=des,bg="cyan")
    dis.place(x=130,y=520)

    ####RETRIVE OVER####
    r.mainloop()
except Exception as e:
    mb.showerror('NETWORK',e)
