# 🚢 Titanic Survival Analysis — Exploratory Data Analysis (EDA)

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

