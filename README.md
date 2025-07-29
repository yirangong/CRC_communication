# Modeling Communication Dynamics in Complex Strategic Planning: A Unity-Based Behavioral Experiment

A behavioral experiment exploring how communication influences strategic planning in complex, asymmetric decision environments. Developed in Unity, this project simulates decision trees with varying structure and captures multimodal behavioral data to investigate when and how verbal communication supports collaboration.

Done by Yiran and Nastaran (Ma Lab at NYU).

---

## 🚀 Motivation & Hypotheses

Communication supports collaboration—but at a cost. This project examines the **cognitive trade-offs of verbal communication** during joint planning tasks. We ask:

- **When is communication used?**
- **How does it impact performance?**
- **What biases emerge in collaborative vs. solo planning?**

### 🔍 Core Hypotheses

#### 🗣️ Selective Communication
We hypothesize that speech is **strategically deployed** during moments of uncertainty. Participants are more likely to communicate when:
- The **decision tree** has a **high branching factor** (many possible actions)
- The **state space** is ambiguous or unpredictable
- The move has **long-term or irreversible consequences**

#### 🤝 Communication Benefits
Collaborative planning will **outperform solo planning** in environments requiring **mutual belief alignment**, with communication serving to:
- Signal uncertainty (e.g., verbal hesitations)
- Clarify intent (e.g., verbal previews or gestural cues)
- Repair mispredictions (e.g., corrections after mismatched actions)

#### ⚠️ Communication Biases
We expect collaborative teams may also show:
- **Over-coordination**: Unnecessary talking in low-stakes or predictable states
- **Contribution disparity**: Unequal effort when task complexity is unevenly distributed (e.g., one player faces deeper subtrees)

---

## 📁 Data Pool

- `basic_map_1`: Raw map data (coordinates, metadata)
- `basic_summary_1`: Precomputed metrics and gameplay stats

---

## 🗺️ Game Map Analysis

- Uses the data pool to analyze map structure and complexity
- See `Game_Map_Analysis/README.md` for implementation details

---

## 📊 `map_blocks.xlsx`

- Contains exported map sets for gameplay testing or model training
