# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
df = pd.read_csv("./survey_results_public.csv")
df.columns=[x.lower() for x in df.columns]


# %%
schema = pd.read_csv("./survey_results_schema.csv")
schema


# %%
country = ['India',"Afghanistan"]
filt = (df['hobbyist']=='Yes') & (df['country'].isin(country))
# filt=df['LanguageWorkedWith'].str.contains("Python",na=False)


# %%

 df.loc[filt & df['languageworkedwith'].str.contains("Python",na=False),['country']]


# %%
def lowerHobbylist(hobby):
    return hobby.lower()
    
df['hobbyist'].apply(lowerHobbylist)
df['hobbyist'].replace({'Yes':True,"No":False   })


# %%
# schema.drop(index=range(85,91))
df.info()


# %%
# df[['age','convertedcomp']].sort_values(by=["convertedcomp",'age'],ascending=[False,False],inplace=True)
df.nlargest(10,'convertedcomp')


# %%
countryGroup = df.groupby(['country'])
countryGroup['convertedcomp'].value_counts().loc['India']


# %%
countryGroup['convertedcomp'].median().loc['India']


# %%
countryGroup['convertedcomp'].agg(['median','mean','max','min'])

# %%
countryUsePython= countryGroup['languageworkedwith'].apply(lambda x: x.str.contains("Python").sum())
countryUsePython


# %%
pythonDf = pd.concat([countryUsePython,df['country'].value_counts()],axis='columns')
pythonDf.dtypes


# %%
pd.to_datetime.dataframes




# %%
