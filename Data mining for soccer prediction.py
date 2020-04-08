from selenium import webdriver
import time
import csv
import pandas as pd

driver = webdriver.Firefox()
Summery = """
https://www.flashscore.com/match/tnOlHb9f/#match-statistics;0
"""
results = """
https://www.flashscore.com/football/england/premier-league/results/
"""
driver.get(results)


driver.find_element_by_link_text("Show more matches").click()
time.sleep(3)
# statistics = driver.find_elements_by_xpath("//div[@class='statRow']")
# list = []
# for i in range(len(statistics)):
#     list.append(statistics[i].text.split('\n'))
#
# print(list)
link_list = []
big_list = []

df = pd.read_csv('/home/jordan/Documents/Projects/Python Android/Neural_Network/Neural_Network/Premier_all.csv')

events = driver.find_elements_by_xpath('//div[@title="Click for match detail!"]')

for i in range(len(events)):
    id = events[i].get_attribute('id')
    id = id[4:]
    link = "https://www.flashscore.com/match/" + id + "/#match-statistics;0"
    link_list.append(link)

for j in range(len(link_list)):
    c = j*2
    driver.get(link_list[j])
    time.sleep(3)
    teams = driver.find_elements_by_xpath("//div[@class='tname__text']")
    statistics = driver.find_elements_by_xpath("//div[@class='statRow']")
    df['T_name'][c] = teams[0].text
    df['T_name'][c+1] = teams[1].text
    for k in range(len(statistics)):
        if statistics[k].text == "":
            break
        else:
            elements = statistics[k].text.split('\n')
            try:
                df[elements[1]][c] = elements[0].strip('%')
                df[elements[1]][c+1] = elements[2].strip('%')
            except Exception as e:
                pass

print(j)

# with open('{}.csv'.format(x), 'w') as f:
#     f.write("Home,Away,H_ball_position,A_ball_position,H_Goal_Attempts,A_Goal_Attempts\n")
#     for i in range(size):
#         list = events[i].text.split("\n")
#         # home = list[1]
#         # away = list[5]
#         # home_score = list[2]
#         # away_score = list[4]
#         over = 0
#         bts = 0
#         sum = int(list[2]) + int(list[4])
#         if sum > 2.5:
#             over = 1
#         if int(list[2]) > 0 and int(list[4]) > 0:
#             bts = 1
#         f.write(list[1] + "," + list[5] + "," + list[2] + "," + list[4] + "," + str(sum) + "," + str(bts) + "," + str(over) + "\n")


# url = driver.current_url
# new_url = url[:-14] + "#match-statistics;0"
# driver.get(new_url)
# statistics = driver.find_elements_by_xpath("//div[@class='statRow']")
# list = []
# for j in range(len(statistics)):
#     list.append(statistics[i].text.split('\n'))
# biglist.append(list)
# print(biglist)



# League_1_results = """
# https://www.flashscore.com/football/france/ligue-1/results/
# """
# Laliga_results = """
# https://www.flashscore.com/football/spain/laliga/results/
# """
# Seria_A_results = """
# https://www.flashscore.com/football/italy/serie-a/results/
# """
# BundesLiga_results = """
# https://www.flashscore.com/football/germany/bundesliga/results/
# """
# Eredivisie_results = """
# https://www.flashscore.com/football/netherlands/eredivisie/results/
# """
# Premier_results = """
# https://www.flashscore.com/football/england/premier-league/results/
# """
# Turkey_results = """
# https://www.flashscore.com/football/turkey/super-lig/results/
# """
#
#
# def get_results(league, x):
#     driver.get(league)
#     driver.find_element_by_link_text("Show more matches").click()
#     time.sleep(3)
#     events = driver.find_elements_by_xpath("//div[@title='Click for match detail!']")
#     size = len(events)
#
#     with open('{}.csv'.format(x), 'w') as f:
#         f.write("Home,Away,H_Score,A_Score,Sum,BTS,Over\n")
#         for i in range(size):
#             list = events[i].text.split("\n")
#             # home = list[1]
#             # away = list[5]
#             # home_score = list[2]
#             # away_score = list[4]
#             over = 0
#             bts = 0
#             sum = int(list[2]) + int(list[4])
#             if sum > 2.5:
#                 over = 1
#             if int(list[2]) > 0 and int(list[4]) > 0:
#                 bts = 1
#             f.write(list[1] + "," + list[5] + "," + list[2] + "," + list[4] + "," + str(sum) + "," + str(bts) + "," + str(over) + "\n")
#
#     for i in range(size):
#         list = events[i].text.split("\n")
#         # home = list[1]
#         # away = list[5]
#         # home_score = list[2]
#         # away_score = list[4]
#         print(list[1] + "," + list[5] + "," + list[2] + "," + list[4])
#     print(i)
#
# get_results(League_1_results,'League_1_results')
# get_results(Laliga_results,'Laliga_results')
# get_results(Seria_A_results,'Seria_A_results')
# get_results(BundesLiga_results,'BundesLiga_results')
# get_results(Eredivisie_results,'Eredivisie_results')
# get_results(Premier_results,'Premier_results')
# get_results(Turkey_results,'Turkey_results')


print(df.tail())
df.to_csv('/home/jordan/Documents/Projects/Python Android/Neural_Network/Neural_Network/Test.csv')

driver.close()
