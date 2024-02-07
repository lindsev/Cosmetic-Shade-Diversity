import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.header('Data Viewer')
shades = pd.read_csv('notebooks/shades.csv')
st.dataframe(shades)

# Shade Distribution Across Price Categories
histogram = px.histogram(
    shades,
    x="lightness",
    color="hex",
    color_discrete_map={hex_val: hex_val for hex_val in shades['hex'].unique()}, # Descrete color mapping for each count's corresponding  hex value
    title='Range of Lightness in Various Price Points',
    nbins=50,
    labels={'lightness': 'Lightness Value', 'count': 'Count of Shades'},  # Setting axis labels
)
histogram.update_layout(showlegend=False, )

# Updatin layout and dropdown menu
product_types = ['High-End', 'Mid-Range', 'Drugstore']
dropdown_menu = [{'label': product_type, 'method': 'update',
                  'args': [{'visible': shades['price_category'] == product_type,
                            'xbins':{'start':40,'size':5},
                            'xaxis': {'tickvals': np.arange(39, 251, 10)},
                            }]} for product_type in product_types]
dropdown_menu.insert(0, {'label': 'Show All', 'method': 'update', 'args': [{'visible': True}]})

#Adding Dropdown Menu
histogram.update_layout(
    updatemenus=[
        {'buttons': dropdown_menu,
         'direction': 'down',
         'showactive': True,
         'x': 0.0,
         'xanchor': 'left',
         'y': 1.1,
         'yanchor': 'top'}
    ]
)


#### Scatter Plot of Lightness Values

# Creating a scatter plot using Plotly Express
scatter = px.scatter(
    shades,
    x='lightness',  # Using lightness as the x-axis
    y='price_category',  # Using price category as the y-axis
    color='hex',  # Color each point based on its hex value
    color_discrete_map={hex_val: hex_val for hex_val in shades['hex'].unique()},  # Use actual hex values for colors
    hover_data={'brand': True,
                'hex': False,
                'product': True,
                'name': True,
                'specific': True}
)

# Hide the legend (since colors directly represent hex values)
scatter.update_layout(showlegend=False, xaxis_title='Shade Lightness Value', yaxis_title='Price Category')

# Add a descriptive title to the plot
scatter.update_layout(title='Relationship Between Shade Lightness and Price Category')

# Add checkboxes to toggle visibility
show_histogram = st.checkbox("Show Histogram", False)
# Displaying the charts based on checkbox values
if show_histogram:
    st.plotly_chart(histogram, use_container_width=True)

show_scatter_plot = st.checkbox("Show Scatter Plot", False)
# Displaying the charts based on checkbox values
if show_scatter_plot:
    st.plotly_chart(scatter, use_container_width=True)

show_all_plots = st.checkbox("Show All Plots", True)
# Displaying the charts based on checkbox values
if show_all_plots:
    st.plotly_chart(scatter, use_container_width=True)
    st.plotly_chart(histogram, use_container_width=True)
