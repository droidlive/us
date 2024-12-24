import requests
import json

def fetch_and_save_json(url, output_file):
    """
    Verilen URL'den JSON verisini alır ve bir dosyaya kaydeder.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"JSON veri {output_file} dosyasına başarıyla kaydedildi.")
        else:
            print(f"Veri alınamadı. HTTP Durum Kodu: {response.status_code}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    # Sabit URL ve çıktı dosyası
    url = "https://www.cnnturk.com/api/cnnvideo/media?id=62d6814670380e2cdc7c124c&isMobile=false"
    output_file = "veri.json"
    fetch_and_save_json(url, output_file)
