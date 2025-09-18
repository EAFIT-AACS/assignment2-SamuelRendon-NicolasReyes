---

# ✨ Activity 2 – PDA Formal Languages

## ✨ Samuel Rendon Pabon

## ✨ Nicolas Reyes Cano

This project contains three **Python** implementations related to the topic of **Formal Languages and Pushdown Automata (PDA)**.  

The original file was divided into **three independent programs**, one for each algorithm, in order to run and analyze them separately.  

---

## 📦 Detailed instructions for running your implementation

**Open the terminal in macOS and put the next line**
```bash
python3 actividad2_algoritmo1.py
```
```bash
python3 actividad2_algoritmo2.py
```
```bash
python3 actividad2_algoritmo3.py
```
🚀 **These 3 lines will run each of the algorithms u want to use**

🚀 **After the program runs, you will see that the strings for each algorithm work and give results**

🚀 **For Windows you can insert the code in VScode and run it from there, you will also see that the strings for each algorithm work and will give results**

---

## 📂 Files  

### 1. `actividad2_algoritmo1.py`  
📘**Description:**  
Implements an automaton that recognizes strings under certain rules of a formal language (depending on the definition given in the original statement).  

⚙️**Functionality:**  
- 📖 Defines the grammar or the pushdown automaton.  
- 🔍 Processes input strings to determine whether they belong to the language or not.  
- ✅ When executed, the program displays examples of acceptance or rejection.  

📚**Theoretical explanation:**  
This algorithm works with the idea of a **Deterministic Pushdown Automaton (DPDA)** for balanced strings or similar structures. The stack is used as auxiliary memory to validate the structure of the string.  

---

### 2. `actividad2_algoritmo2.py`  
📘**Description:**  
Second algorithm that validates strings of another formal language defined in the activity.  

⚙️**Functionality:**  
- 🛠️ Initializes a set of transition rules for the pushdown automaton.  
- 🔄 The program iterates through the strings and simulates the PDA’s behavior.  
- ✅/❌ Displays accepted and rejected strings according to the rules.  

📚**Theoretical explanation:**  
This example reflects the use of PDA for a more complex language that cannot be recognized by a simple finite automaton. A common case is **non-regular languages** such as `{ a^n b^n | n ≥ 0 }`.  

---

### 3. `actividad2_algoritmo3.py`  
📘**Description:**  
Third algorithm based on another specific grammar or PDA.  

⚙️**Functionality:**  
- 🧩 Simulates an automaton that processes more structured strings.  
- 🔍 Verifies whether the input meets the conditions of the defined grammar.  
- ✅/❌ Returns results of acceptance or rejection.  

📚**Theoretical explanation:**  
The third algorithm illustrates another classical case of **Context-Free Languages (CFLs)** recognizable by PDA, reinforcing how pushdown automata can handle **nested structures** that go beyond finite automata.  

---

## 📚 Conclusion  
This project helps understand how **Pushdown Automata (PDA)** are applied to the validation of **Context-Free Languages (CFLs)**.  
Splitting the code into three files makes it easier to clearly see the independent functionality of each algorithm and reinforces theory with practical examples.  

---
