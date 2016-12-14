# -*- coding: utf-8 -*-

'''
Created on Dec 2, 2016

@author: Bin Liang
'''

import sqlite3

def connect_sqlite(sqlite_file):
    """ 
            连接数据库，返回连接和游标 
    """
    with sqlite3.connect(sqlite_file) as conn:
        conn.row_factory = sqlite3.Row # 返回的每行是sqlite3.Row类型，可通过列名直接访问数据
        cur = conn.cursor()
    return conn, cur


def close_sqlite(conn):
    """ 
            关闭连接
    """
    if conn:
        conn.close()


def total_rows(cursor, table_name, print_out=False):
    """ 
                返回表中的所有行
    """
    # for py3
    #cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))
    
    # for py2    
    cursor.execute('SELECT COUNT(*) FROM %s' %table_name)
    count = cursor.fetchall()
    
    if print_out:
        # for py3
        #print('\nTotal rows: {}'.format(count[0][0]))
        
        # for py2
        print'\nTotal rows: %i' %count[0][0]
        
    return count[0][0]


def table_col_info(cursor, table_name, print_out=False):
    """ 
                返回表信息
        (id, name, type, notnull, default_value, primary_key)
    """
    # for py3
    #cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    
    # for py2
    cursor.execute('PRAGMA TABLE_INFO(%s)' %table_name)
    
    info = cursor.fetchall()

    if print_out:
        print "\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey"
        for col in info:
            print(col)
    return info
