# RISC-V Çok Çekirdekli Pipeline Simülatörü ve Görüntü Tabanlı Hareket Algılama

Bu proje, bilgisayar organizasyonu dersi kapsamında geliştirilen bir sistemdir. RISC-V mimarisi üzerine kurulu çok çekirdekli bir pipeline simülatörü, görüntü işleme temelli hareket algılama sistemiyle entegre edilmiştir. Kullanıcılar, komutların boru hattındaki adım adım işlenişini görselleştirilmiş bir web arayüzü üzerinden takip edebilir.

---

## 🔧 Proje Özellikleri

- ✅ **RISC-V pipeline simülasyonu (IF, ID, EX, MEM, WB aşamaları)**
- ✅ **Çok çekirdekli işlem desteği**
- ✅ **Görselleştirme: Adım adım komut ilerleyişi**
- ✅ **OpenCV ile gerçek zamanlı hareket algılama**
- ✅ **Flask tabanlı web arayüzü**
- ✅ **Performans metrikleri: CPI, IPC, stall sayısı, forwarding sayısı**
- ✅ **Kod analiz modülü: Syntax Tree oluşturma (beta)**

---

## 🖼️ Ekran Görüntüleri

> Web arayüzü, pipeline görselleştirme, grafik analizler ve örnek video işlem çıktılarının yer aldığı ekran görüntüleri `screenshots/` klasöründe bulunmaktadır.

---

## 🚀 Kurulum ve Çalıştırma

1. Depoyu klonlayın:
```bash
git clone https://github.com/jesusamaisa/riscv_pipeline_simulator.git
cd riscv_pipeline_simulator
