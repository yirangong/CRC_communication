# 🗺️ Working with Game Maps

This notebook analyzes and filters game map data used in a Unity-based road construction game. Each map is evaluated under two strategic modes: **greedy** (locally optimal at each step) and **optimal** (globally best outcome). The goal is to select maps that produce meaningful gameplay differences between these strategies.

---

## 🔍 Objective

- Identify maps where strategic choices matter — i.e., where **greedy ≠ optimal**.
- Quantify differences using metrics like path length, city coverage, and player contribution.
- Export selected maps for further use in visualization, game development, and training pipelines.

---

# 🧭 MapSelectionNotebook Structure
This notebook is intended to:
- Evaluate strategic depth of maps
- Identify training vs. testing map sets
- Serve as a filtering stage before game integration
- Provide visual and tabular summaries of map features

### 1. ✅ Selecting Desired Maps
- Filter maps by:
  - **Starting Position Distance** (Euclidean): 30–200 units
  - **Optimal Contribution Gap**: 25%–75%
- Purpose: Avoid trivial or highly skewed maps.

### 2. 🔍 Inspecting Basic Features
- Visualize city coordinates.
- Analyze spatial/geometric structure of maps.

### 3. 📉 Exploratory Correlations
- Investigate:
  - Relationship between **number of optimal solutions** and **map depth**
  - Territory separation and suboptimality in player behavior

### 4. 🧪 Map-Level Deep Dives
- For selected maps, inspect path sequences, budget usage, and turn-by-turn strategy differences.

---

## 📁 File Structure

- `basic_map_1`: Raw map data (coordinates, metadata).
- `basic_summary_1`: Precomputed metrics and gameplay stats for maps.
- `map_blocks.xlsx`: Exported map sets for testing or training.

---

## 🧠 Variable Glossary (from `basic_summary_1`)

### Strategy Comparison
- `diff_num_opt_greed`:  
  Difference in cities collected between optimal and greedy strategies.

- `optimal_list`, `greedy_list_p1`, `greedy_list_p2`:  
  City visit sequences for each strategy.

- `optimal_move_num`, `greedy_move_num_p1`, `greedy_move_num_p2`:  
  Number of turns taken (excluding start).

### Player Behavior
- `optimalTurn_list`:  
  Indicates which player made the optimal move at each step.

- `remain_budget_len_opt`, `remain_budget_len_greed`:  
  Remaining budget per player per round under each strategy.

### Tree & Path Structure
- `depth_opt`:  
  Number of cities visited (tree depth).

- `treeWidth`:  
  Number of possible gameplay paths (tree leaves).

- `nOfOpt`:  
  Number of distinct optimal solutions.

- `OptPathAll`, `OptTurnsAll`:  
  Collections of all optimal paths and turn sequences.

### Contribution Metrics
- `delta_contribution`:  
  Player contribution difference across optimal paths.

- `contribution_p1`, `contribution_p2`:  
  Average player contributions in optimal plays.

---
## MapConversion Notebook Structure
- Export selected maps to Excel (`map_blocks.xlsx`) with city coordinates and starting positions per block.

## MapVisualization Notebook Structure


