# Top5_Candidates.py
A simple Flask web application to score, rank, and display job candidates based on their skills, experience, and education. Uses ngrok to make the app accessible over the internet (perfect for demos from Colab or local machine).
Sure! Here’s a **clean, professional, and clear** `README.md` you can put in your project root.
It explains what the project does, how to set it up (both locally and in Colab), and what each route does.

Feel free to copy-paste this directly:

---

## 📄 **README.md**

# 🧑‍💻 Hiring App — Candidate Scoring and Shortlisting

A simple Flask web application to score, rank, and display job candidates based on their skills, experience, and education.
Uses ngrok to make the app accessible over the internet (perfect for demos from Colab or local machine).

---

## 🚀 **Features**

✅ Automatically scores each candidate:

* +3 points per year of experience
* +5 points per matching skill (`Python`, `Java`, `AI`, `ML`)
* +5 points if education is `Masters` or `PhD`

✅ Shows:

* Home page with navigation
* List of all candidates sorted by score
* Top 5 candidates with score & reason

✅ Uses **Bootstrap** for styling

---

## 🛠 **Tech Stack**

* Python
* Flask
* pyngrok
* HTML + Bootstrap (for templates)

---

## 📦 **Folder Structure**

```
.
├── app.py
├── form-submissions.json
└── templates/
    ├── home.html
    ├── candidates.html
    └── top5.html
```

---

## ⚙️ **Setup & Run (Local)**

1️⃣ Install dependencies:

```bash
pip install flask pyngrok
```

2️⃣ Create your ngrok account at [ngrok.com](https://ngrok.com/) → get your **authtoken**.

3️⃣ Add your authtoken to `app.py`:

```python
ngrok.set_auth_token("YOUR_AUTHTOKEN_HERE")
```

4️⃣ Run the app:

```bash
python app.py
```

5️⃣ Copy the ngrok public URL printed in terminal → open in browser.

---

## 📔 **Run in Google Colab**

1️⃣ Install:

```python
!pip install flask pyngrok
```

2️⃣ Create required HTML templates and JSON file (use `os.makedirs` and `open()` as shown in notebook).

3️⃣ Use same `app.py` code, run cell → copy the ngrok link.

**Tip:** See `app.py` and `templates` folder in this repo for ready files.

---

## 🌐 **Routes**

| Route         | Description                                     |
| ------------- | ----------------------------------------------- |
| `/`           | Home page with navigation                       |
| `/candidates` | Shows all candidates sorted by calculated score |
| `/top5`       | Shows top 5 candidates + reason                 |

---

## ✏️ **Customization**

* Edit `form-submissions.json` to add more candidates.
* Change scoring logic inside `score_candidate()` in `app.py`.
* Edit HTML templates inside `templates/` to change styling.

---

## 🏆 **Author**

Made for demo / learning purpose.

---
