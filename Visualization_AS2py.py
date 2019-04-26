#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vega_datasets import data
import pandas as pd
import altair as alt
source=pd.read_csv('C://Users/Yoga 910/Desktop/Life Expectancy_Group7.csv')

alt.renderers.enable('notebook')


# In[2]:



source.head()


# In[3]:


#df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]
Source_UAC=source.loc[(source['Country'] == "United States of America") | (source['Country'] == "Australia") |
                      (source['Country'] == "Canada") |  (source['Country'] == "Germany")]
Source_UAC


# In[4]:


source = Source_UAC

alt.Chart(Source_UAC).transform_filter(
    alt.datum.symbol != 'GOOG'
).mark_area().encode(
    x='Year:O',
    y='Hepatitis B:Q',
    color='Country:N',
    row=alt.Row('Country:N')
).properties(height=50, width=400).interactive()


# In[5]:



alt.Chart(Source_UAC).mark_circle().encode(
    alt.X(alt.repeat("column"), type='ordinal'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color='Country:N'
).properties(
    width=150,
    height=150
).repeat(
    row=['percentage expenditure', 'Population'],
    column=['Year']
).interactive()


# In[6]:


alt.Chart(Source_UAC).mark_circle().encode(
    x='Year:O',
    y='GDP:Q',
    color='Country'
).interactive()


# In[7]:


alt.Chart(Source_UAC).mark_circle().encode(
    x='Year:O',
    y='Adult Mortality:Q',
    size='average(Adult Mortality):Q',
    color='Country:N'
).interactive()


# In[8]:


source_2015=source.loc[source.Year==2015]
source_2014=source.loc[source.Year==2014]
source_2013=source.loc[source.Year==2013]
source_2015


# In[9]:


base = alt.Chart(source_2015)

bar = base.mark_bar().encode(
    x=alt.X('Population:Q', bin=True, axis=None),
    y='count()',
     color='Country:N'
)

rule = base.mark_rule(color='red').encode(
    x='mean(Population):Q',
    size=alt.value(5)
).interactive()

bar + rule


# In[10]:



brush = alt.selection(type='interval', resolve='global')

base = alt.Chart(source).mark_point().encode(
    y='Adult Mortality',
    color=alt.condition(brush, 'Year', alt.ColorValue('gray'))
).add_selection(
    brush
).properties(
    width=250,
    height=250
)

base.encode(x='Hepatitis B') | base.encode(x='Diphtheria')


# In[11]:


source.head()

