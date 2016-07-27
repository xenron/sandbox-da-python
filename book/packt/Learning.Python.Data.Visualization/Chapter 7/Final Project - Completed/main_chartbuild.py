#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import LoadRssFeed, chart_build

#Call our 'LoadRssFeed' function.
chart_build.generate_chart(LoadRssFeed.get_all_rss_dates())