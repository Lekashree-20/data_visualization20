#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from bokeh.io import show, output_notebook, curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.resources import INLINE


# In[2]:


output_notebook(resources=INLINE)


# In[3]:


from sklearn.datasets import load_iris


# In[4]:


iris = load_iris()

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df["FlowerType"] = iris.target

iris_df.head()


# In[8]:


scatter = figure(plot_width=500, plot_height=400,
                 title="Sepal Length vs Sepal Width Scatter Plot")

color_mapping = {0:"tomato", 1:"dodgerblue", 2:"lime"}

for cls in [0,1,2]:
    scatter.circle(x=iris_df[iris_df["FlowerType"]==cls]["sepal length (cm)"],
               y=iris_df[iris_df["FlowerType"]==cls]["sepal width (cm)"],
               color=color_mapping[cls],
               size=10,
               alpha=0.8,
               legend_label=iris.target_names[cls])

scatter.xaxis.axis_label= "sepal length (cm)".upper()
scatter.yaxis.axis_label= "sepal width (cm)".upper()

show(scatter)


# In[9]:


iris_avg_by_flower_type = iris_df.groupby(by="FlowerType").mean()

bar_chart = figure(plot_width=500, plot_height=400,
                   title="Average Sepal Length (cm) per Flower Type")

bar_chart.vbar(x = [1,2,3],
         width=0.9,
         top=iris_avg_by_flower_type["sepal length (cm)"],
         fill_color="tomato", line_color="tomato", alpha=0.9)

bar_chart.xaxis.axis_label="FlowerType"
bar_chart.yaxis.axis_label="Sepal Length"

bar_chart.xaxis.ticker = [1, 2, 3]
bar_chart.xaxis.major_label_overrides = {1: 'Setosa', 2: 'Versicolor', 3: 'Virginica'}

show(bar_chart)


# In[18]:


layout = row(scatter, bar_chart)
show(layout)


# In[11]:


from bokeh.models import CheckboxButtonGroup

checkbox_options = ['open','high','low','close']

checkbox_grp = CheckboxButtonGroup(labels=checkbox_options, active=[0], button_type="success")
show(checkbox_grp)


# In[12]:


from bokeh.models import Select

drop_scat1 = Select(title="X-Axis-Dim",
                    options=iris.feature_names,
                    value=iris.feature_names[0],
                    width=200)

drop_scat2 = Select(title="Y-Axis-Dim",
                    options=iris.feature_names,
                    value=iris.feature_names[1],
                    width=200)

show(row(drop_scat1, drop_scat2))


# In[13]:


drop_bar = Select(title="Dimension", options=iris.feature_names, value=iris.feature_names[0])

show(drop_bar)


# In[19]:


layout_with_widgets = column(
                            column(checkbox_grp),
                            row(
                                column(row(drop_scat1, drop_scat2), scatter),
                                column(drop_bar, bar_chart)))


show(layout_with_widgets)


# In[15]:


show(layout_with_widgets.children[1])


# In[16]:





# In[ ]:




