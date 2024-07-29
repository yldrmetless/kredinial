# Python 3.12.4 tabanlı bir imaj kullan
FROM python:3.12.4

# Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# Gereksinimlerinizi içeren dosyayı kopyala
COPY requirements.txt .

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamanın kodlarını kopyala
COPY . .

# Portu aç
EXPOSE 8000

# Django'nun yönetim komutunu çalıştır
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kredinial.wsgi:application"]
