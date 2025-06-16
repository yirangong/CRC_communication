# Map Selection Analysis

This notebook analyzes map statistics from a pool of game scenarios used in a Unity road construction game. The maps are evaluated based on strategic behavior in two modes: **greedy** and **optimal**.

## 🔍 Objective
To evaluate and select maps based on the differences between greedy and optimal strategies, looking at path efficiency, player contributions, and budget consumption.

---

## 📁 File Structure

- `basic_map_1`: Contains raw map data for one game.
- `basic_summary_1`: Contains precomputed metrics for that map (see below for structure).

---

## 🧠 Variables Explained (from `basic_summary_1`)

### Map-Level Comparison
- `diff_num_opt_greed`:  
  Difference in number of cities collected between **optimal** and **greedy** strategies.

### Strategy Paths
- `optimal_list`:  
  City locations of both players over time using optimal strategy.
  
- `greedy_list_p1`, `greedy_list_p2`:  
  City locations of each player using greedy strategy.

- `optimal_move_num`, `greedy_move_num_p1`, `greedy_move_num_p2`:  
  Number of moves taken by each strategy (minus start).

### Turn Analysis
- `optimalTurn_list`:  
  Which player took the optimal move at each turn.

### Budget Tracking
- `remain_budget_len_opt`, `remain_budget_len_greed`:  
  Remaining budget per player per turn under each strategy.

### Tree Metrics
- `depth_opt`:  
  Depth (number of cities visited) by both players in optimal strategy.
  
- `treeWidth`:  
  Number of possible game plays (leaves in the decision tree).

- `nOfOpt`:  
  Number of distinct optimal paths evaluated.

### Path Collections
- `OptPathAll`:  
  All optimal move sequences for the map.

- `OptTurnsAll`:  
  All optimal turn sequences for the map.

### Player Contributions
- `delta_contribution`:  
  Difference in contribution between players.

- `contribution_p1`, `contribution_p2`:  
  Average move contribution across optimal paths.

---

## Future Notes
> This structure may expand if new variables are introduced.

---

## 🛠 Usage
This notebook can be used to:
- Compare strategies on a per-map basis.
- Filter out low-interest maps (e.g., where greedy ≈ optimal).
- Visualize budget usage and player decision dynamics.
