import requests
import json

def fetch_cnn_data():
    url = "https://www.cnnturk.com/api/cnnvideo/media?id=62d6814670380e2cdc7c124c&isMobile=false"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Veri alırken hata oluştu: {response.status_code}")
        return None

def save_data_to_file(data, filename="veri.json"):
    if data:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Veri başarıyla {filename} dosyasına kaydedildi.")
    else:
        print("Veri kaydedilemedi.")

if __name__ == "__main__":
    data = fetch_cnn_data()
    save_data_to_file(data)
