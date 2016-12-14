# -*- coding: utf-8 -*-

'''
Created on Dec 2, 2016

@author: Bin Liang
'''
import datetime
import numpy as np


def get_age_for_football_players(birthday_str):
    """
            获取球员年龄
    """
    date  =  birthday_str.split(" ")[0]
    today = datetime.datetime.strptime("2016-12-10", "%Y-%m-%d").date()
    born = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))  


def get_overall_rating(cur, player_api_id):
    """
            获取球员平均评分
    """
    all_rating = cur.execute("SELECT overall_rating FROM Player_Attributes WHERE player_api_id = '%d' " % player_api_id).fetchall()
    all_rating = np.array(all_rating,dtype=np.float)[:,0]
    mean_rating = np.nanmean(all_rating)
    return mean_rating


def get_current_team_and_country(cur, player_api_id):
    """
            获取当前球队及国家
    """
    all_rating = cur.execute("SELECT overall_rating FROM Player_Attributes WHERE player_api_id = '%d' " %player_api_id).fetchall()
    all_rating = np.array(all_rating,dtype=np.float)[:,0]
    rating = np.nanmean(all_rating)
    if (rating>1): 
        all_football_nums = reversed(range(1,12))
        for num in all_football_nums:
            all_team_id = cur.execute("SELECT home_team_api_id, country_id FROM Match WHERE home_player_%d = '%d'" % (num,player_api_id)).fetchall()
            if len(all_team_id) > 0:
                number_unique_teams = len(np.unique(np.array(all_team_id)[:,0]))
                last_team_id = all_team_id[-1]['home_team_api_id']
                last_country_id = all_team_id[-1]['country_id']
                last_country = cur.execute("SELECT name FROM Country WHERE id = '%d'" % (last_country_id)).fetchall()[0][0]
                last_team = cur.execute("SELECT team_long_name FROM Team WHERE team_api_id = '%d'" % (last_team_id)).fetchall()[0][0]
                return last_team, last_country, number_unique_teams
    return None, None, 0


def get_position(cur, x):
    """
            获取球员位置
    """
    all_rating = cur.execute("""SELECT overall_rating FROM Player_Attributes WHERE player_api_id = '%d' """ % (x)).fetchall()
    all_rating = np.array(all_rating,dtype=np.float)[:,0]
    rating = np.nanmean(all_rating)
    if (rating>1): 
        all_football_nums = reversed(range(1,12))
        for num in all_football_nums:
            all_y_coord = cur.execute("""SELECT home_player_Y%d FROM Match WHERE home_player_%d = '%d'""" % (num,num,x)).fetchall()
            if len(all_y_coord) > 0:
                Y = np.array(all_y_coord,dtype=np.float)
                mean_y = np.nanmean(Y)
                if (mean_y >= 10.0):
                    return "for"
                elif (mean_y > 5):
                    return "mid"
                elif (mean_y > 1):
                    return "def"
                elif (mean_y == 1.0):
                    return "gk"
    return None