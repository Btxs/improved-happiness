import tkinter as tk
import tkinter.messagebox
import pymysql
import sys
import pickle

#def __init__(self, master, root, cnf = {}, extra = ()):

main_window = tk.Tk()

def center_window(w, h):
    ws = main_window.winfo_screenwidth()
    hs = main_window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    return '%dx%d+%d+%d' %(w, h, x, y)

size = center_window(500, 400)
main_window.geometry(size)
center_window(500, 400)
main_window.title('登录')
tk.Label(main_window, text = '用户名').place(x = 100, y = 150)
tk.Label(main_window, text = '密码').place(x = 100, y = 190)
#用户名与密码输入
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(main_window, textvariable = var_usr_name)
entry_usr_name.place(x = 160, y = 150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(main_window, show = '*', textvariable = var_usr_pwd)
entry_usr_pwd.place(x = 160, y = 190)

sql_table = 'user.new_table'

server = 'localhost'
sql_user = 'root'
sql_pwd = '980324'
try:
    sql_connect = pymysql.connect(server, sql_user, sql_pwd)
except:
    tk.messagebox.showerror(message = 'Connect wrong!')
sql_connect.autocommit(1)
cursor = sql_connect.cursor()

def user_log_in():
    username = var_usr_name.get()
    password = var_usr_pwd.get()
    cursor.execute('SELECT * FROM user.new_table where username = %s', username)  #返回整形
    row = cursor.fetchone()
    try:
        if password == row[2]:
            log_success(username)
            import flowers
            main_window.destroy()
        else:
            log_failed()
    except:
        log_failed()

def log_up_destory():
        sign_up_window.destroy()
        
def user_log_up_con():
    global sign_up_window
    global var_new_name
    global var_new_pwd
    global var_new_repwd
    sign_up_window = tk.Toplevel(main_window)
    sign_up_window.title('注册')
    sign_up_window.geometry(center_window(400, 400))
    tk.Label(sign_up_window, text = '新用户名').place(x = 100, y = 150)
    tk.Label(sign_up_window, text = '密码').place(x = 100, y = 190)
    tk.Label(sign_up_window, text = '确认密码').place(x = 100, y = 230)
    var_new_name = tk.StringVar()
    entry_new_name = tk.Entry(sign_up_window, textvariable = var_new_name)
    entry_new_name.place(x = 160, y = 150)
    var_new_pwd = tk.StringVar()
    entry_new_pwd = tk.Entry(sign_up_window, show = '*', textvariable = var_new_pwd)
    entry_new_pwd.place(x = 160, y = 190)
    var_new_repwd = tk.StringVar()
    entry_new_repwd = tk.Entry(sign_up_window, show = '*', textvariable = var_new_repwd)
    entry_new_repwd.place(x = 160, y = 230)
    def user_log_up_acc(var_new_name, var_new_pwd):
        new_username = var_new_name.get()
        new_password = var_new_pwd.get()
        reCount = cursor.execute('INSERT INTO `user`.`new_table` (`username`, `password`) VALUES (%s, %s);' ,(new_username, new_password))
        #print(reCount)
        if reCount != 0:
            log_up_success()
            sign_up_window.destroy()
        else:
            log_up_failed()
            sign_up_window.destroy()
    def log_up_destory():
        global sign_up_window
        sign_up_window.destroy()
    bt_log_up_acc = tk.Button(sign_up_window, text = '确认注册', command = user_log_up)
    bt_log_up_acc.place(x = 140, y = 270)
    bt_log_return = tk.Button(sign_up_window, text = '返回登录', command = log_up_destory)
    bt_log_return.place(x = 210, y = 270)
    #sign_up_window.mainloop()
    
def user_log_up():
    new_username = var_new_name.get()
    new_password = var_new_pwd.get()
    new_repassword = var_new_repwd.get()
    if new_password == new_repassword:
        cursor.execute('INSERT INTO `user`.`new_table` (`username`, `password`) VALUES (%s, %s);' ,(new_username, new_password))
        log_up_success()
        sign_up_window.destroy()
    else:
        log_up_failed()
        sign_up_window.destroy()
    
def user_log_exit():
    main_window.destroy()
    
def log_success(username):
    tk.messagebox.showinfo(title = 'Welcome', message = 'Welcome ' + username)

def log_up_success():
    tk.messagebox.showinfo(title = 'Welcome', message = 'Welcome')
    
def log_failed():
    tk.messagebox.showerror(message = 'Password wrong!')

def log_up_failed():
    tk.messagebox.showerror(message = 'Log up failed!')
#def connect_mysql():
    #tk.messagebox.showerror(message = 'Password wrong!')

#按钮
bt_log_in = tk.Button(main_window, text = '登录', command = user_log_in)
bt_log_in.place(x = 140, y = 230)
bt_log_up = tk.Button(main_window, text = '注册', command = user_log_up_con)
bt_log_up.place(x = 210, y = 230)
bt_log_exit = tk.Button(main_window, text = '退出', command = user_log_exit)
bt_log_exit.place(x = 280, y = 230)

main_window.mainloop()

#if __name__ == '__main__':
    #username, password = user_log_in()


