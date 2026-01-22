import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class SistemAnalisisPangan:
    def __init__(self, file_path):
        self.file_path = file_path
        self.raw_df = pd.read_csv(file_path)
        # Membersihkan nama kolom (menghapus spasi pada tanggal)
        self.raw_df.columns = [c.replace(' ', '') if '/' in c else c for c in self.raw_df.columns]
        self.hasil_prediksi = []

    def _cleaning_data(self, row_index):
        """Metode internal untuk membersihkan data per baris"""
        nama = self.raw_df.iloc[row_index, 1]
        data_harga = self.raw_df.iloc[row_index, 2:]
        
        df_temp = pd.DataFrame({
            'Tanggal': pd.to_datetime(data_harga.index, format='%d/%m/%Y'),
            'Harga': data_harga.values.astype(str)
        })
        
        # Hilangkan koma ribuan dan ubah ke numerik
        df_temp['Harga'] = df_temp['Harga'].str.replace(',', '').astype(float)
        df_temp['Bulan_Ke'] = np.arange(len(df_temp))
        return nama, df_temp

    def analisis_dan_export(self, list_index, jumlah_bulan):
        plt.figure(figsize=(12, 6))
        writer = pd.ExcelWriter('Laporan_Prediksi_Beras.xlsx', engine='xlsxwriter')
        
        for idx in list_index:
            nama, df_kategori = self._cleaning_data(idx)
            
            # 1. Training Model (Linear Regression)
            model = LinearRegression()
            X = df_kategori[['Bulan_Ke']]
            y = df_kategori['Harga']
            model.fit(X, y)
            
            # 2. Prediksi Masa Depan
            last_idx = df_kategori['Bulan_Ke'].max()
            X_future = np.array([[i] for i in range(last_idx + 1, last_idx + 1 + jumlah_bulan)])
            y_pred = model.predict(X_future)
            
            # 3. Membuat Rentang Tanggal Masa Depan
            last_date = df_kategori['Tanggal'].iloc[-1]
            future_dates = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=jumlah_bulan, freq='MS')
            
            # 4. Simpan Hasil ke List untuk Excel
            df_hasil = pd.DataFrame({
                'Bulan': future_dates.strftime('%B %Y'),
                'Estimasi_Harga': y_pred.round(0)
            })
            df_hasil.to_excel(writer, sheet_name=nama[:30], index=False)
            
            # 5. Plot Grafik
            plt.plot(df_kategori['Tanggal'], df_kategori['Harga'], label=f"{nama} (Data)")
            plt.plot(future_dates, y_pred, '--', label=f"{nama} (Prediksi)")

        # Simpan Excel
        writer.close()
        
        # Finalisasi Grafik
        plt.title('Proyeksi Kenaikan Harga Beras 2026-2027')
        plt.xlabel('Tahun')
        plt.ylabel('Harga (Rp)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('grafik_prediksi.png') # Simpan grafik sebagai gambar
        plt.show()
        
        print("✅ Analisis Selesai!")
        print("- File Excel 'Laporan_Prediksi_Beras.xlsx' telah dibuat.")
        print("- Gambar grafik 'grafik_prediksi.png' telah disimpan.")

# --- Jalankan Program ---
path = 'Tabel_Harga Berdasarkan_Daerah.csv'
proyek = SistemAnalisisPangan(path)
proyek.analisis_dan_export(list_index=[1, 2, 3], jumlah_bulan=12)

#AI Ethic : 
# Dalam pengembangan sistem ini, kami memastikan bahwa data yang digunakan bersifat transparan dan dapat dipertanggungjawabkan.
# Kami tidak menggunakan data sensitif atau pribadi tanpa izin. Seluruh proses prediksi dilakukan secara objektif dan berdasarkan data historis yang tersedia.

#liner regression merupakan metode statistik yang umum digunakan untuk analisis tren dan prediksi.
#Namun, perlu diingat bahwa prediksi masa depan selalu mengandung ketidakpastian,
#terutama dalam konteks pasar komoditas yang dipengaruhi oleh banyak faktor eksternal.
#Oleh karena itu, hasil prediksi harus digunakan sebagai salah satu referensi dalam pengambilan keputusan, bukan sebagai kepastian mutlak.

#library yang digunakan dalam kode ini adalah library open-source yang tersedia untuk umum,
#seperti pandas, numpy, scikit-learn, dan matplotlib.

#pandas digunakan untuk manipulasi data,
#numpy untuk operasi numerik,
#scikit-learn untuk model machine learning (linear regression),

#dan matplotlib untuk visualisasi data.
