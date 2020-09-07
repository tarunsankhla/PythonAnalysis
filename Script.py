import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

//Modules are imported.//

corona_dataset_csa = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csa.head(-20)


corona_dataset_csa = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csa.head(10)	

corona_dataset_csa.shape

corona_dataset_csa.drop(["Lat","Long"],axis=1,inplace=True)
corona_dataset_csa.head(10)

corona_dataset_aggregated =corona_dataset_csa.groupby("Country/Region").sum()
corona_dataset_aggregated.head()

corona_dataset_aggregated.shape

corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
corona_dataset_aggregated.loc["Canada"].plot()
corona_dataset_aggregated.loc["India"].plot()
corona_dataset_aggregated.loc["Brazil"].plot()
plt.legend()

corona_dataset_aggregated.loc['China'][:3].plot()

corona_dataset_aggregated.loc["China"].diff().plot()

// find maxmimum infection rate for China
corona_dataset_aggregated.loc["China"].diff().max()
corona_dataset_aggregated.loc["China"].diff().max()

corona_dataset_aggregated.loc["Italy"].diff().max()

corona_dataset_aggregated.loc["Spain"].diff().max()

countries = list(corona_dataset_aggregated.index)
max_infection_rates =[]
for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_infection_rates"] = max_infection_rates

corona_dataset_aggregated.head()


corona_data  = pd.DataFrame(corona_dataset_aggregated["max_infection_rates"])
corona_data.head()

happiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")
happiness_report_csv.head()

happiness_report_csv.drop(useless_col,axis=1,inplace=True)
happiness_report_csv.head()


happiness_report_csv.set_index("Country or region",inplace=True)
happiness_report_csv.head()

corona_data.head()
corona_data.shape

happiness_report_csv.shape
happiness_report_csv.head()

data =corona_data.join(happiness_report_csv,how="inner")
data.head()

data.corr()

x= data["GDP per capita"]
y=data["max_infection_rates"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

x=data["Social support"]
y=data["max_infection_rates"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))








