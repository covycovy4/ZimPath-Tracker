# ZimPath-Tracker 🧬

**A Low-Bandwidth Web Tool for Real-Time Pathogen Surveillance in Zimbabwe**

## 🧠 Why I Built This

Zimbabwe experiences outbreaks of cholera, typhoid, TB, and drug-resistant infections, but:

- 🏥 Pathogen data is siloed in hospitals and research labs
- 🧬 Local bioinformatics tools are scarce
- 📶 Many rural clinics have poor internet

I wanted to create a tool that could **run even offline**, analyze local genomic data, and help frontline health workers.

---

## 🔧 Project Summary
ZimPath-Tracker is a lightweight web tool to:

✅ Upload and analyze pathogen sequences  
✅ Detect mutations and resistance genes  
✅ Visualize outbreaks using maps  
✅ Store results offline and sync when online

---

## 📅 Timeline

### ✅ **Day 1: Flask Web App + Upload**
- Set up `Flask` app with a file upload form
- Users can submit `.fastq` files
- Files are saved to `/data`

### ✅ **Day 2: FASTQ Alignment with Minimap2**
- Installed `minimap2` via conda
- Downloaded *Salmonella Typhi* genome from NCBI
- Used Python to run `minimap2` on uploads
- Output: `.paf` file showing alignments

---

## 🔬 Next Steps

- Add Biopython to extract resistance markers
- Store results in SQLite
- Add outbreak maps using Leaflet.js
- Generate reports as PDFs

---

## 💻 Technologies Used

| Component     | Tools                              |
|---------------|------------------------------------|
| Backend       | Python (Flask)                     |
| Alignment     | `minimap2`, Biopython              |
| Frontend      | HTML, CSS, JavaScript              |
| Offline       | SQLite + Service Workers (planned) |
| Mapping       | Leaflet.js or Plotly (planned)     |

---

## 🇿🇼 For Zimbabwe, By Zimbabwe

This project shows how open tools and local talent can help shape public health solutions in Africa.

I hope to grow this into a powerful tool that supports health research in Zimbabwe and other resource-limited settings.

> _Built by Tsidzonaishe Covenant Chiwasa_  
> Final-year Biotechnology & Bioinformatics student  
> Passionate about open science and genomic surveillance  
