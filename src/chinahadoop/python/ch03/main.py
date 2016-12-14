# -*- coding: utf-8 -*-

'''
Created on Dec 2, 2016

@author: Bin Liang
'''
import zipfile
import os
import pandas as pd
import mpl_toolkits.basemap as bm
import matplotlib.pyplot as plt
import numpy as np
from sqlite_tool import connect_sqlite, close_sqlite
from proc_tool import get_age_for_football_players, get_overall_rating,\
    get_current_team_and_country


def unzip(zip_filepath, dest_path):
    """
            解压zip文件
    """
    with zipfile.ZipFile(zip_filepath) as zf:
        zf.extractall(path = dest_path)


def get_dataset_filename(zip_filepath):
    """
            获取数据库文件名
    """
    with zipfile.ZipFile(zip_filepath) as zf:
        return zf.namelist()[0]
    

def run_task1(cur):
    """
            多表查询获取球员基本数据，保存CSV，并返回该数据
    """
    # 分析球员的个数，根据分析时间可自行调整
    max_players_to_analyze = 50
    sql = "SELECT * FROM Player LIMIT %i" %max_players_to_analyze
    players = cur.execute(sql).fetchall()
    
    # 球员姓名列表
    player_name_lst = [player['player_name'] for player in players]
    # 获取生日列表
    player_birthday_lst = [player['birthday'] for player in players]
    # 体重列表
    player_weight_lst = [player['weight'] for player in players]
    # 身高列表
    player_height_lst = [player['height'] for player in players]
    # 获取年龄列表
    player_age_lst = map(get_age_for_football_players, player_birthday_lst)
    # 获取平均评分列表
    player_rating_lst = [get_overall_rating(cur, player['player_api_id']) for player in players]
    
    # 获取所处球队、国家及曾经所在球队的个数
    player_country_info_tup_lst = [get_current_team_and_country(cur, player['player_api_id']) for player in players]
    team_lst, country_lst, n_teams = zip(*player_country_info_tup_lst)
    
    # 构造dataframe保存CSV 
    player_name_se = pd.Series(player_name_lst, name='name') # 球员姓名
    player_age_se = pd.Series(player_age_lst, name='age')    # 球员年龄
    player_weight_se = pd.Series(player_weight_lst, name='weight')  # 体重
    player_height_se = pd.Series(player_height_lst, name='height')  # 身高
    player_ave_rating_se = pd.Series(player_rating_lst, name='rating')  # 平均评分
    player_team_se = pd.Series(team_lst, name='team')  # 球队
    player_country_se = pd.Series(country_lst, name='country')  # 国家
    n_teams_se = pd.Series(n_teams, name='#teams')  # 所在球队个数
    
    player_df = pd.concat([player_name_se, player_age_se, player_weight_se, player_height_se,
                           player_ave_rating_se, player_team_se, player_country_se, n_teams_se],
                          axis = 1)
    player_csv_filepath = './player_data.csv'
    player_df.to_csv(player_csv_filepath, indx = None, encoding='utf-8')
    
    return player_df

def run_task2(player_df):
    """
            可视化国家评分
    """
    countries_rating = player_df.groupby("country")["rating"].mean()
    countries_rating = countries_rating.reset_index()   # 重设索引号
    min_rating = countries_rating["rating"].min()
    
    # 按国家计算整体评分
    countries_coef = map(lambda x: x - min_rating + 5, countries_rating["rating"])
    countries_rating["rating"] = countries_coef
    
    # 构建字典列表
    final_ratings = {item[0]:item[1] for item in countries_rating.values}
    
    # 初始化地图信息
    countries = {}
    # [横坐标, 纵坐标, 点大小]
    countries["England"] = [-0.12, 51.5, 20.0]
    countries["Belgium"] = [4.34, 50.85, 20.0]
    countries["France"] = [2.34, 48.86, 20.0]
    countries["Germany"] = [13.4, 52.52, 20.0]
    countries["Italy"] = [12.49, 41.89, 20.0]
    countries["Netherlands"] =[4.89, 52.37, 20.0]
    countries["Poland"] = [21.01, 52.23, 20.0]
    countries["Portugal"] = [-9.14, 38.73, 20.0]
    countries["Scotland"] = [-4.25, 55.86, 20.0]
    countries["Spain"] = [-3.70, 40.41, 20.0]
    countries["Switzerland"] = [6.14, 46.2, 20.0]
    
    # 根据评分更新点的大小
    for i in final_ratings.keys():
        countries[i][2] = 3*final_ratings[i]
    plt.figure(figsize=(12,12))
    
    m = bm.Basemap(projection='cyl',    # 地图投影方式 
                   llcrnrlat=35, urcrnrlat=58, llcrnrlon=-10, urcrnrlon=22, # 经纬度范围
                   resolution='f')
    
    m.drawcountries(linewidth=0.2)
    m.fillcontinents(color='lavender', lake_color='#907099')
    m.drawmapboundary(linewidth=0.2, fill_color='#000040')
    m.drawparallels(np.arange(-90,90,30),labels=[0,0,0,0], color='white', linewidth=0.5)
    m.drawmeridians(np.arange(0,360,30),labels=[0,0,0,0], color='white', linewidth=0.5)
    
    # 绘制国家
    for i in countries.keys():
        m.plot(countries[i][0], countries[i][1], 'bo', markersize = countries[i][2], color='r')
    
    # 添加国家名称
    for label, xpt, ypt in zip(list(countries.keys()), np.array(list(countries.values()))[:,0],\
                               np.array(list(countries.values()))[:,1]):
        plt.text(xpt - 0.85, ypt, label, fontsize = 20, color="black")
    plt.show()
    
    # 保存数据的可视化
    plt.savefig('./country_rank.png')

    
def run_main():
    """
            主函数
    """
    # 声明变量
    database_path = './database'    # 数据库路径
    zip_filename = 'soccer.zip'     # zip文件名
    zip_filepath = os.path.join(database_path, zip_filename)    # zip文件路径
    database_filename = get_dataset_filename(zip_filepath)      # 数据库文件名（在zip中）
    database_filepath = os.path.join(database_path, database_filename)  # 数据库文件路径
    
    print "解压zip...",
    unzip(zip_filepath, database_path)
    print "完成."
    
    # 连接数据库
    conn, cur = connect_sqlite(database_filepath)
    
    # 运行task1
    player_df = run_task1(cur)
    
    # 运行task2
    run_task2(player_df)
    
    # 分析结束，关闭数据库
    close_sqlite(conn)
    
    # 删除解压数据，清理空间
    if os.path.exists(database_filepath):
        os.remove(database_filepath)

    
if __name__ == '__main__':
    run_main()

