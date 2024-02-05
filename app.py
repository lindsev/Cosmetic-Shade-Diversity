import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Data Viewer')
shades = pd.read_csv('notebooks/shades.csv')
st.dataframe(shades)

# Shade Distribution Across Price Categories
fig3 = px.histogram(
    shades,
    x="lightness",
    nbins=25,
    color="hex",
    color_discrete_map={hex_val: hex_val for hex_val in shades['hex'].unique()},
    title='Range of Lightness in Price Categories'
)
fig3.update_layout(xaxis_title='Lightness Value', yaxis_title='Count of Shades', hovermode=False, showlegend=False)
product_types = shades['price_category'].unique()
dropdown_menu = [{'label': product_type, 'method': 'update', 'args': [{'visible': shades['price_category'] == product_type}]} for
                 product_type in product_types]
dropdown_menu.insert(0, {'label': 'Show All', 'method': 'update', 'args': [{'visible': True}]})

fig3.update_layout(
    updatemenus=[
        {'buttons': dropdown_menu,
         'direction': 'down',
         'showactive': True,
         'x': 0.1,
         'xanchor': 'left',
         'y': 1.1,
         'yanchor': 'top'}
    ]
)

# Create a scatter plot using Plotly Express
fig4 = px.scatter(
    shades,
    x='lightness',  # Use lightness as the x-axis
    y='price_category',  # Use price category as the y-axis
    color='hex',  # Color each point based on its hex value
    color_discrete_map={hex_val: hex_val for hex_val in shades['hex'].unique()},  # Use actual hex values for colors
    hover_data={'brand': True,
                'hex': False,
                'product': True,
                'name': True,
                'specific': True}
)

# Hide the legend (since colors directly represent hex values)
fig4.update_layout(showlegend=False, xaxis_title='Shade Lightness Value', yaxis_title='Price Category')

# Add a descriptive title to the plot
fig4.update_layout(title='Relationship Between Shade Lightness and Price Category')

# Add checkboxes to toggle visibility
show_histogram = st.checkbox("Show Histogram", False)
# Display the charts based on checkbox values
if show_histogram:
    st.plotly_chart(fig3, use_container_width=True)

show_scatter_plot = st.checkbox("Show Scatter Plot", False)
# Display the charts based on checkbox values
if show_scatter_plot:
    st.plotly_chart(fig4, use_container_width=True)

show_all_plots = st.checkbox("Show Scatter Plot", True)
# Display the charts based on checkbox values
if show_all_plots:
    st.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig3, use_container_width=True)
