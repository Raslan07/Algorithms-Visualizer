# 📊 Algorithm Visualizer (Python)

An interactive **Algorithm Visualizer** built with Python and Matplotlib that allows users to explore how different sorting algorithms work step-by-step.

The application provides a graphical interface to visualize sorting algorithms, control animation speed, pause/resume execution, and monitor algorithm statistics such as comparisons and swaps.

---

## 🚀 Features

* 📌 Visualize multiple sorting algorithms
* 🎮 Interactive controls (buttons and sliders)
* ⏸ Pause and resume the animation
* 🔄 Reset and generate a new random array
* ⚡ Adjustable animation speed
* 📊 Real-time statistics:

  * Number of comparisons
  * Number of swaps
  * Time complexity display
* 🧠 Clean project architecture

---

## 🧮 Supported Algorithms

| Algorithm      | Average Complexity |
| -------------- | ------------------ |
| Bubble Sort    | O(n²)              |
| Insertion Sort | O(n²)              |
| Merge Sort     | O(n log n)         |
| Quick Sort     | O(n log n)         |

---

## 🖥 Demo Interface

The application includes interactive UI controls:

* **Bubble / Insertion / Merge / Quick** → select sorting algorithm
* **Pause** → pause animation
* **Resume** → continue sorting
* **Reset** → generate a new random array
* **Speed Slider** → control visualization speed

---

## 📂 Project Structure

```
algorithm_visualizer
│
├── algorithms
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   └── quick_sort.py
│
├── utils
│   └── generator.py
│
├── visualizer
│   └── visualizer.py
│
├── main.py
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/algorithm_visualizer.git
```

Navigate to the project folder:

```
cd algorithm_visualizer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the visualizer with:

```
python main.py
```

The interactive visualization window will open.

---

## 🧠 How It Works

The visualization uses:

* **Python generators (`yield`)** to produce algorithm states
* **Matplotlib animations** to render sorting steps
* **Interactive widgets** for UI controls

Each algorithm yields intermediate states of the array which are then rendered as animated bars.

---

## 🛠 Technologies Used

* Python
* Matplotlib
* NumPy

---

## 📚 Learning Goals

This project demonstrates concepts including:

* Algorithm visualization
* Sorting algorithms
* Python generators
* Event-driven programming
* Matplotlib animations
* Clean project architecture

---

## 🔮 Future Improvements

Potential upgrades for the project:

* 🔴 Comparison highlighting (colored bars)
* 🟢 Swap highlighting
* 🎚 Array size slider
* 🔍 Search algorithm visualization
* 🌙 Dark mode UI
* 💾 Export animation as GIF

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve the project:

1. Fork the repository
2. Create a new branch
3. Submit a pull request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you find this project useful, consider giving it a **star ⭐ on GitHub**.
