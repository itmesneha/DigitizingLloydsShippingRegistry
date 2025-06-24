# 📦 Lloyd's Shipping Registry OCR Pipeline

This repository contains scripts and notebooks to extract tabular data from historical shipping registers (PDF scans) using column-wise OCR.

---

## 🔄 Workflow Overview

### 1. 📥 Download the Registry
Download the full shipping registry PDF from the Internet Archive:

[https://ia802809.us.archive.org/5/items/HECROS1860/ROS1860.pdf](https://ia802809.us.archive.org/5/items/HECROS1860/ROS1860.pdf)

---

### 2. 🧾 Extract a Single Page

Run the script `extract_single_page.py`:

```bash
python extract_single_page.py
```

- It will prompt for a **page number** (e.g., enter `155`).
- Outputs:
  - A single-page **PDF** file
  - A corresponding **PNG** image of that page

---

### 3. 📏 Define Column Coordinates

Run the OpenCV script `get_coordinates.py` to record the X positions of each column.

- Click on each column to record its X-coordinate.
- Separate coordinates are needed for **odd** and **even** page layouts.

#### 📄 Odd Page Numbers (e.g., page 155)

**Clicked Points:**
```
(75, 1417), (306, 1406), (477, 1403), (547, 1540),
(668, 1524), (759, 1538), (929, 1549), (1068, 1549),
(1269, 1538), (1334, 1543), (1408, 1543), (1485, 1544)
```

**COLUMN_BOUNDARIES:**
```python
COLUMN_BOUNDARIES = [
    (0, 75),
    (75, 306),
    (306, 477),
    (477, 547),
    (547, 668),
    (668, 759),
    (759, 929),
    (929, 1068),
    (1068, 1269),
    (1269, 1334),
    (1334, 1408),
    (1408, 1485)
]
```

---

#### 📄 Even Page Numbers (e.g., page 156)

**Clicked Points:**
```
(121, 1693), (361, 1704), (530, 1703), (607, 1702),
(726, 1700), (815, 1699), (986, 1698), (1121, 1711),
(1325, 1725), (1389, 1728), (1465, 1734), (1514, 2034)
```

**COLUMN_BOUNDARIES:**
```python
COLUMN_BOUNDARIES = [
    (0, 121),
    (121, 361),
    (361, 530),
    (530, 607),
    (607, 726),
    (726, 815),
    (815, 986),
    (986, 1121),
    (1121, 1325),
    (1325, 1389),
    (1389, 1465),
    (1465, 1514)
]
```

---

### 4. 🚀 Run the Full OCR Pipeline

Run the following Google Colab notebook to:

- Split image by columns
- Send each column to Google Document AI
- Collect and structure text into Excel

🔗 [Run Notebook on Google Colab](https://colab.research.google.com/drive/1r-F4aXKY5GWt8smoCE1rQVPyS_ySwb-n#scrollTo=jZcq7MmUgTLt)

---

### 📄 Notebook Overview – Google Document AI PoC

This notebook implements a column-wise OCR processing pipeline for structured documents like scanned registers. The goal is to extract text **column by column** from scanned `.png` pages and populate them into an Excel sheet.

---

#### ✅ Step-by-Step Summary:

 1. **Authentication & Setup**
- Authenticates with Google Cloud.
- Initializes project environment variables.
- Prepares access to the Document AI API.

 2. **Defining Column Boundaries**
- Based on pre-clicked X-coordinates from representative odd and even pages (e.g., pages 155 and 156).
- Each page is assumed to follow similar structure; columns are defined as `(start_x, end_x)` pixel boundaries.

 3. **Image Splitting**
- Loads a scanned page (e.g., `page_155.png`).
- Splits the page into individual column images using the X-boundaries defined earlier.
- Saves each column image into a separate file (e.g., `columns_exact/column_1.png`, `column_2.png`, ...).

 4. **OCR Processing with Google Document AI**
- Each column image is sent individually to Google Document AI for OCR.
- Text results are parsed and extracted column by column.

 5. **Exporting to Excel**
- The OCR text from each column is saved into a Pandas DataFrame.
- Each column of the DataFrame corresponds to one column from the original document.
- The DataFrame is exported to an `.xlsx` file for downstream use.

 6. **End-to-End Workflow Execution**
- The notebook combines all above steps into a pipeline that processes a full page in one go:  
   **Split → OCR → Tabular Output**

---
