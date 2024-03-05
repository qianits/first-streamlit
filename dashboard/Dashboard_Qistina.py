# Proyek Analisis Data: Bike Sharing Dataset
# - **Nama:** Qistina Muharrifa
# - **Email:** qmqistina@gmail.com
# - **ID Dicoding:** qistina

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

day_df = pd.read_csv("data/day.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

## Sidebar 
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df["dteday"] >= str(start_date)) & 
                (day_df["dteday"] <= str(end_date))]

st.header('Proyek Analisis Data: Bike Sharing Dataset :sparkles:')
st.subheader('by Qistina Muharrifa')


# Interactive 1
daily_cnt_df = main_df.groupby('dteday')['cnt'].sum().reset_index()
st.text('Jumlah Total Penyewa Sepeda per Hari')
plt.figure(figsize=(10, 6))
plt.plot(daily_cnt_df['dteday'], daily_cnt_df['cnt'], marker='o', linestyle='-')
plt.title('Jumlah Total Penyewa Sepeda per Hari')
plt.xlabel('Tanggal')
plt.ylabel('Total Penyewa')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

# Nomor 1
st.subheader("Notebook")
st.text("Bagaimana tren total penyewa sepeda (baik casual maupun registered) setiap bulannya pada tahun 2012 pada dataset day.csv")
day_df_2012 = day_df[day_df['dteday'].dt.year == 2012]
monthly_trend_2012 = day_df_2012.groupby(day_df_2012['dteday'].dt.month)['cnt'].sum()

plt.figure(figsize=(10, 6))
plt.plot(monthly_trend_2012.index, monthly_trend_2012.values, marker='o', linestyle='-')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewa Total')
plt.title('Tren Penyewa Total per Bulan (2012)')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(plt)

# Nomor 2
st.text("Hubungan antara total penyewa sepeda dengan suhu temperatur lingkungan pada dataset day.csv")
plt.figure(figsize=(10, 6))
plt.scatter(day_df['temp'], day_df['cnt'], color='skyblue', alpha=0.6)
plt.title('Scatter Plot Total Penyewa vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('Jumlah Penyewa')
plt.grid(True, linestyle='--', alpha=0.5)
st.pyplot(plt)

# Nomor 3
st.text("Musim apa yang paling banyak memiliki penyewa sepeda pada dataset day.csv")
day_df1 = day_df.copy()
day_df1['season'] = day_df1['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
season_counts = day_df1.groupby('season')[['casual', 'registered']].sum()
plt.figure(figsize=(10, 6))
season_counts.plot(kind='bar', stacked=True)
plt.title('Jumlah Penyewa Casual dan Registered untuk Setiap Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(title='Atribut')
plt.ticklabel_format(style='plain', axis='y')
st.pyplot(plt)

# Nomor 4
st.text("Pada hari apakah masyarakat kebanyakan menyewa sepeda pada dataset day.csv")
day_df2 = day_df.copy()
day_df2['weekday'] = day_df2['weekday'].replace({0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4:'Thu', 5:'Fri', 6:'Sat'})
counts = day_df2.groupby('weekday')[['casual', 'registered']].sum()
plt.figure(figsize=(10, 6))
counts.plot(kind='bar', stacked=True)
plt.title('Jumlah Penyewa Casual dan Registered untuk Setiap Hari')
plt.xlabel('Hari')
plt.ylabel('Jumlah')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(title='Atribut')
st.pyplot(plt)