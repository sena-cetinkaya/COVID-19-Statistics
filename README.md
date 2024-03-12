# COVID-19-Statistics
This repo contains COVID-19 data and data visualization operations. The dataset used in this repo was taken from Kaggle.
[Link to the dataset](https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset).

To review my work on this dataset on Kaggle; [https://www.kaggle.com/code/senacetinkaya/covid-19-statistics#DATA-VISUALIZATION](https://www.kaggle.com/code/senacetinkaya/covid-19-statistics#DATA-VISUALIZATION)

--------------------------------------------
# DATA VISUALIZATION
Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.

In this repo, the "Total Cases" data included in the COVID-19 data are shown with a bar plot. "Total Deaths" data is shown with a pie chart. Also It designed to visualize COVID-19 global statistics on a world map.

-----------------------------------------
### Libraries Used in the Project
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point
```

---------------------------------
### Visuals obtained from the data.

A horizontal bar chart was created using the Seaborn library to visualize the total number of COVID-19 cases for each of the top 10 countries.

![](https://github.com/sena-cetinkaya/COVID-19-Statistics/blob/main/Figure_1.png)

A pie chart was created using the matplotlib library to visualize the distribution of COVID-19 deaths among the top 10 countries.

![](https://github.com/sena-cetinkaya/COVID-19-Statistics/blob/main/Figure_2.png)

COVID-19 global statistics visualized on a world map.

![](https://github.com/sena-cetinkaya/COVID-19-Statistics/blob/main/Figure_3.png)
