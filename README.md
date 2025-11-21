# 🔍 Mirror Equation Challenge – Python Solution

## 🧠 Deskripsi
Diberikan string persamaan dengan format `"a + b = c"` di mana **salah satu angka dibalik urutan digitnya (reversed)**. Tugasnya adalah menentukan:
- angka mana yang terbalik (prioritas: a → b → c)
- dan berapa nilai sebenarnya

Contoh:
`"12 + 34 = 64"`  
➡ `12 + 34 = 46` jadi salah di `c`, nilai benar `46`

---

## 📌 Aturan
- Hanya **satu angka** yang terbalik
- Dilarang menggunakan:
  - `regex`
  - `eval()`
  - `split()`
  - `reverse()` / `[::-1]`
- Parsing dan reverse harus manual (loop)

---

## 🎯 Output Format
| Kondisi | Output |
|---------|---------|
| Persamaan benar | `correct` |
| a salah | `a,nilai_benar` |
| b salah | `b,nilai_benar` |
| c salah | `c,nilai_benar` |
| Tidak ada solusi valid | `no solution` |

---

## 🚀 Cara Menjalankan
```
python challenge.py
