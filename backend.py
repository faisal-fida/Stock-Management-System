from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import csv
from datetime import datetime
import numpy as np

from connect import *

def read():
    cursor.connection.ping()
    sql=f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks ORDER BY `id` DESC"
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def find():
    itemId = str(itemIdEntry.get())
    name = str(nameEntry.get())
    price = str(priceEntry.get())
    qnt = str(qntEntry.get())
    cat = str(categoryCombo.get())
    cursor.connection.ping()
    if(itemId and itemId.strip()):
        sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `item_id` LIKE '%{itemId}%' "
    elif(name and name.strip()):
        sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `name` LIKE '%{name}%' "
    elif(price and price.strip()):
        sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `price` LIKE '%{price}%' "
    elif(qnt and qnt.strip()):
        sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `quantity` LIKE '%{qnt}%' "
    elif(cat and cat.strip()):
        sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `category` LIKE '%{cat}%' "
    else:
        messagebox.showwarning("","Please fill up one of the entries")
        return
    cursor.execute(sql)
    try:
        result = cursor.fetchall();
        for num in range(0,5):
            setph(result[0][num],(num))
        conn.commit()
        conn.close()
    except:
        messagebox.showwarning("","No data found")

def clear():
    for num in range(0,5):
        setph('',(num))

def exportExcel():
    cursor.connection.ping()
    sql=f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks ORDER BY `id` DESC"
    cursor.execute(sql)
    dataraw=cursor.fetchall()
    date = str(datetime.now())
    date = date.replace(' ', '_')
    date = date.replace(':', '-')
    dateFinal = date[0:16]
    with open("stocks_"+dateFinal+".csv",'a',newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in dataraw:
            w.writerow(record)
    print("saved: stocks_"+dateFinal+".csv")
    conn.commit()
    conn.close()
    messagebox.showinfo("","Excel file downloaded")