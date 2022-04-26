
import csv, math
import pandas as pd
import numpy as np
from datetime import timedelta
import time
import matplotlib.pyplot as plt
import statsmodels.api as sm
import plotly.express as px


pf = pd.read_html('https://www.nbastuffer.com/2020-2021-nba-player-stats/', index_col=0, header=0, 
                    skiprows=[21])[0]

pf.head()


pf.reset_index()



pf.reset_index()



import matplotlib.ticker as ticker
#fig1 = pf.plot.scatter(x = 'MIN%Minutes PercentagePercentage of team minutes used by a player while he was on the floor',y ='PPGPointsPoints per game.')
x = pf['MIN%Minutes PercentagePercentage of team minutes used by a player while he was on the floor']
y = pf['PPGPointsPoints per game.']
plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.xlabel('Percenatage of Team Minutes %') 
plt.ylabel('Points Per Game') 
plt.title("Amount of Time Spent Playing and Points Earned")
plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter())
plt.show()


pf_team = pf.groupby('TEAM').sum()
pf_team = pf_team.reset_index()
pf_team.head(16)
pf_team = pf_team.reindex([9, 12, 0, 5, 14, 11, 4, 2, 7, 15, 3, 10, 13, 8, 1, 6])


fig2 = pf_team.plot.bar(x= 'TEAM', y='PPGPointsPoints per game.',                        color=['darkgreen', 'darkorange', 'black', 'mediumblue', 'gold', 'red', 'midnightblue', 'black',                             'mediumblue', 'red', 'silver', 'orange', 'red', 'hotpink', 'green', 'purple'],                         title='Total Points Per Team' )
fig2.set_ylabel('Number of Points')
fig2.set_xlabel('Team')
fig2.get_legend().remove()


pf_team2 = pf.groupby('TEAM').mean()
pf_team2 = pf_team2.reset_index()
list(pf.columns)
pf_team2.head(12)

list(pf_team2.columns)


pf_team2 = pf_team2[['TEAM', 'FT%', '2P%', '3P%', 'eFG%Effective Shooting PercentageWith eFG%, three-point shots made are worth 50% more than two-point shots made. eFG% Formula=(FGM+ (0.5 x 3PM))/FGA', 'TRB%Total Rebound PercentageTotal rebound percentage is estimated percentage of available rebounds grabbed by the player while the player is on the court.','TO%Turnover RateA metric that estimates the number of turnovers a player commits per 100 possessions']]
pf_team22 = pf_team2.loc[(pf_team2['TEAM'] == 'Mil') | (pf_team2['TEAM'] == 'Pho')]



pf_team22.head()



def turn_to_percent(df, colname):
    df[colname] = df[colname] * 100
    return df

pf_team22 = turn_to_percent(pf_team22, 'FT%')
pf_team22 = turn_to_percent(pf_team22, '2P%') 
pf_team22 = turn_to_percent(pf_team22, '3P%')
pf_team22 = turn_to_percent(pf_team22, 'eFG%Effective Shooting PercentageWith eFG%, three-point shots made are worth 50% more than two-point shots made. eFG% Formula=(FGM+ (0.5 x 3PM))/FGA')


listOfDFRows = pf_team22.to_numpy().tolist()
mil_means1 = listOfDFRows[0]
mil_means1.pop(0)
pho_means1 = listOfDFRows[1]
pho_means1.pop(0)

print(mil_means1, pho_means1)



import matplotlib.ticker as mtick
labels = ['FT%', '2P%', '3P%', 'eFG%', 'TRB%', 'TO%']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mil_means1, width, label='Milwaukee Bucks', color = 'green')
rects2 = ax.bar(x + width/2, pho_means1, width, label='Phoenix Suns', color = 'darkorange')

ax.set_ylabel('Stats Percentage %')
ax.set_xlabel('Stats')
ax.set_title('Scores by Team and Stat')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.legend()
fig.tight_layout()

plt.show()



pf_player_short = pf[['FULL NAME', 'FT%', '2P%', '3P%', 'eFG%Effective Shooting PercentageWith eFG%, three-point shots made are worth 50% more than two-point shots made. eFG% Formula=(FGM+ (0.5 x 3PM))/FGA', 'MIN%Minutes PercentagePercentage of team minutes used by a player while he was on the floor']]
dev_giannis = pf_player_short.loc[(pf_player_short['FULL NAME'] == 'Devin Booker') | (pf_player_short['FULL NAME'] == 'Giannis Antetokounmpo')]


dev_giannis = turn_to_percent(dev_giannis, 'FT%')
dev_giannis = turn_to_percent(dev_giannis, '2P%') 
dev_giannis = turn_to_percent(dev_giannis, '3P%')
dev_giannis = turn_to_percent(dev_giannis, 'eFG%Effective Shooting PercentageWith eFG%, three-point shots made are worth 50% more than two-point shots made. eFG% Formula=(FGM+ (0.5 x 3PM))/FGA')



dev_giannis.head()


listOfDFRows = dev_giannis.to_numpy().tolist()
dev = listOfDFRows[0]
dev.pop(0)
giannis = listOfDFRows[1]
giannis.pop(0)

print(dev, giannis)



import matplotlib.ticker as mtick
labels = ['FT%', '2P%', '3P%', 'eFG%', 'Min Playing%']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, giannis, width, label='Giannis Antetokounmpo', color = 'green')
rects2 = ax.bar(x + width/2, dev, width, label='Devin Booker', color = 'darkorange')

ax.set_ylabel('Stats Percentage %')
ax.set_xlabel('Stats')
ax.set_title('Scores by Player and Stat')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.legend()
fig.tight_layout()

plt.show()




