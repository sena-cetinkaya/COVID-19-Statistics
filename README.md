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

![](https://www.kaggleusercontent.com/kf/166185463/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..9Yyb-0Da4pg9DQEFDKljhQ.6MyztwGv-yK9q_IuJdpghoLhyuBFwYRdBoTtp2EV4qhMDF5CxH45gMh3BLocEYN2QvJ1Zg1x00EMElFawZ371t5kdV46mQz2Q0neFpgORJOypJuyfexWlxHuccFc6BbM2ZE365mvxzXAr1JDspY3NcyQXkITlxd8No6s-DCkG8tzKV4lLzGAqKM_qlvoQ6Ft-VVQKdanZjTFjJB4gjuxmXBg2LlNtG2Q0t5obopEGQMvLSTcZ_7H-8AH5h5kYYskBQbfdT4TTp6_OJPA5vWzxzSbNGlUxG9EFZ65XdB5SOVb9jJRHYe9etuGKh6iDmk1bFq-xVeK2fK7BwXqjZraL5n5RHrtIW2mbduBPodrc-NavhQQNF-CviKVg2n7Q46qGAG5eGDjpK8kuxUjQCVRckUzIOy57-zAPK5GEkY9F_8Elz7i7BQWxwBxrXiD9VOAIxGpfeImUcnHrjhhUI644AwbW3TnEJO4PhsgVl9pa4SlOYYe1cGiRr3zIlv58XHBjpj7k-PuYUGMrj0tV4iYP3_SDof2MM1XgMliivqIXT-UleeWHAv9jpVhtAzF91HQItYuNzCzezSeC1bbGv7dUFguD-gmxHW4r697VWkd5sHD5Iu8AlIr7CSeIHPgb5SSQ6GGjckd2MwHTWLjzZsGqpEfrAhE3fpvH_cgkv8rhS0.L5Rz8oq1xduAVtAjqSJUnw/__results___files/__results___17_1.png)

A pie chart was created using the matplotlib library to visualize the distribution of COVID-19 deaths among the top 10 countries.

![](https://www.kaggleusercontent.com/kf/166185463/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..9Yyb-0Da4pg9DQEFDKljhQ.6MyztwGv-yK9q_IuJdpghoLhyuBFwYRdBoTtp2EV4qhMDF5CxH45gMh3BLocEYN2QvJ1Zg1x00EMElFawZ371t5kdV46mQz2Q0neFpgORJOypJuyfexWlxHuccFc6BbM2ZE365mvxzXAr1JDspY3NcyQXkITlxd8No6s-DCkG8tzKV4lLzGAqKM_qlvoQ6Ft-VVQKdanZjTFjJB4gjuxmXBg2LlNtG2Q0t5obopEGQMvLSTcZ_7H-8AH5h5kYYskBQbfdT4TTp6_OJPA5vWzxzSbNGlUxG9EFZ65XdB5SOVb9jJRHYe9etuGKh6iDmk1bFq-xVeK2fK7BwXqjZraL5n5RHrtIW2mbduBPodrc-NavhQQNF-CviKVg2n7Q46qGAG5eGDjpK8kuxUjQCVRckUzIOy57-zAPK5GEkY9F_8Elz7i7BQWxwBxrXiD9VOAIxGpfeImUcnHrjhhUI644AwbW3TnEJO4PhsgVl9pa4SlOYYe1cGiRr3zIlv58XHBjpj7k-PuYUGMrj0tV4iYP3_SDof2MM1XgMliivqIXT-UleeWHAv9jpVhtAzF91HQItYuNzCzezSeC1bbGv7dUFguD-gmxHW4r697VWkd5sHD5Iu8AlIr7CSeIHPgb5SSQ6GGjckd2MwHTWLjzZsGqpEfrAhE3fpvH_cgkv8rhS0.L5Rz8oq1xduAVtAjqSJUnw/__results___files/__results___19_0.png)

COVID-19 global statistics visualized on a world map.

![](https://www.kaggleusercontent.com/kf/166185463/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..9Yyb-0Da4pg9DQEFDKljhQ.6MyztwGv-yK9q_IuJdpghoLhyuBFwYRdBoTtp2EV4qhMDF5CxH45gMh3BLocEYN2QvJ1Zg1x00EMElFawZ371t5kdV46mQz2Q0neFpgORJOypJuyfexWlxHuccFc6BbM2ZE365mvxzXAr1JDspY3NcyQXkITlxd8No6s-DCkG8tzKV4lLzGAqKM_qlvoQ6Ft-VVQKdanZjTFjJB4gjuxmXBg2LlNtG2Q0t5obopEGQMvLSTcZ_7H-8AH5h5kYYskBQbfdT4TTp6_OJPA5vWzxzSbNGlUxG9EFZ65XdB5SOVb9jJRHYe9etuGKh6iDmk1bFq-xVeK2fK7BwXqjZraL5n5RHrtIW2mbduBPodrc-NavhQQNF-CviKVg2n7Q46qGAG5eGDjpK8kuxUjQCVRckUzIOy57-zAPK5GEkY9F_8Elz7i7BQWxwBxrXiD9VOAIxGpfeImUcnHrjhhUI644AwbW3TnEJO4PhsgVl9pa4SlOYYe1cGiRr3zIlv58XHBjpj7k-PuYUGMrj0tV4iYP3_SDof2MM1XgMliivqIXT-UleeWHAv9jpVhtAzF91HQItYuNzCzezSeC1bbGv7dUFguD-gmxHW4r697VWkd5sHD5Iu8AlIr7CSeIHPgb5SSQ6GGjckd2MwHTWLjzZsGqpEfrAhE3fpvH_cgkv8rhS0.L5Rz8oq1xduAVtAjqSJUnw/__results___files/__results___21_1.png)
