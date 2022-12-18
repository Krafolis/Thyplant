# Thyplant - Aplikasi Web Deteksi Kesehatan Tanaman

[![Thyplant Logo.jpg](https://i.postimg.cc/bwhsTzJJ/thyplant-logo.jpg)](https://postimg.cc/7fKHPrS8)

Kesehatan tanaman seringkali memiliki permasalahan yang diakibatkan oleh beberapa faktor yang menyebabkan kerusakan pada kualitas tanaman. Diantaranya pada tanaman seringkali terserang penyakit oleh hama, bakteri, dan lainnya. Dari permasalahan yang sudah dijabarkan dibuatlah sebuah sistem aplikasi berbasis web yang dapat membantu mengatasi permasalahan pada sektor pertanian. Sistem aplikasi ini dibuat untuk membantu masyarakat agar lebih mudah dalam mendeteksi kesehatan tanaman.  

# Resource 

## Tools
- Visual Studio Code
- Google Colab

## Programming dan Markup language
- HTML
- CSS
- JavaScript
- Python

## Library dan Framework
- TensorFlow
- Keras
- matplotlib
- pathlib
- Scikit-Learn
- numpy
- shutill
- Opendatasets
- bootstrap
- Flask
- Gunicorn 

## Algoritma
- **CNN (Convolutional Neural Network)**, dengan hasil accuracy 96% dan validation accuracy 94%

## Model Deteksi
- [Model Plant Health](https://github.com/capstone-team-c22-057/Machine_Learning/blob/main/Plant_Health_Detection.ipynb)

## Dataset
- [Tanaman](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)

# Documentation
1. Clone this repository
```
git clone https://github.com/Krafolis/Thyplant.git
```

2. Download file [plant_model.h5](https://drive.google.com/file/d/1-5ex690e86hgJR31KCO6CTvo-07O4pJt/view?usp=share_link)

3. Create folder static

4. Move this folder and file to folder static:
- node_modules
- script
- src
- index.html
- package.json
- package-lock.json

5. Go to folder Web
```
cd (web directory)
```

6. Run with Flask Environment
```
python -m venv venv
pip install virtualenv

virtualenv —-system-site-packages -p python ./venv
.\venv\Scripts\activate

pip install flask
pip install numpy
pip install pillow
pip install tensorflow-cpu

set FLASK_ENV=development
flask run
```
7. Open in browser: http://127.0.0.1:5000/static/index.html

# Developer
Dafa Arif Nurkholis - Indramayu, Jawa Barat

- [Instagram](https://www.instagram.com/dafarifn20/)
- [LinkedIn](https://www.linkedin.com/in/dafa-arif-nurkholis)
