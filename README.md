# 🚢 Titanic Survival Analysis — Exploratory Data Analysis (EDA)
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"/>
  <img src="https://img.shields.io/badge/Seaborn-41B4BD?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn"/>
</p>


This project explores the **Titanic dataset** to uncover insights about passenger survival. Using Python libraries like **Pandas**, **Seaborn**, and **Matplotlib**, I performed data cleaning, transformation, and visualization to answer key questions such as:

- Who had higher chances of survival?
- How did age, sex, class, and fare influence survival?
- What patterns emerge through correlation and feature distribution?

---

## 📊 Key Visual Insights

| Plot | Description |
|------|-------------|
| `Survival Count` | Overall number of survivors vs non-survivors |
| `Survival by Sex` | Shows higher female survival rate |
| `Survival by Class` | Passengers in higher classes had better survival |
| `Age Distribution` | Provides an overview of passenger age spread |
| `Age vs Survival (Boxplot)` | Highlights survival tendencies based on age |
| `Pairplot` | Multivariate visualization of relationships between features |
| `Correlation Heatmap` | Correlation between key numerical features |

> 📁 All output images are saved as `.png` in the project directory.

---

## ⚙️ Technologies Used

| Tool        | Purpose                            |
|-------------|------------------------------------|
| `Python 3.9`| Scripting and logic implementation |
| `Pandas`    | Data wrangling and analysis        |
| `Matplotlib`| Visualization and plots            |
| `Seaborn`   | Enhanced statistical graphics      |
| `NumPy`     | Efficient numerical computation    |

---

## 🧹 Data Preprocessing

- Handled missing values in **Age** and **Embarked**
- Dropped **Cabin** due to excessive nulls
- Encoded **Sex** and **Embarked** for analysis
- Created cleaner feature set for visualization

---

## 📁 Project Structure

.
├─ train.csv # Input dataset
├─ Task5.py # Main analysis script
├── .gitignore # Git ignore rules
├── Output Graphs: # Saved visualizations
│ ├── output_1_survival_count.png
│ ├── output_2_survival_by_sex.png
│ ├── output_3_survival_by_class.png

│ ├── output_4_age_distribution.png
│ ├── output_5_age_vs_survival_boxplot.png
│ ├── output_6_pairplot.png
│ └── output_7_correlation_heatmap.png

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/yuvraj0412s/Exploratory_Data_Analysis.git
cd Exploratory_Data_Analysis

# Make sure you have the dependencies installed
pip install pandas numpy matplotlib seaborn

# Run the script
python Task5.py

