# 🌾 Sundrop Farm

A text-based farming simulation game where you manage a small farm in Albatross Town. Plant seeds, harvest crops, and pay off your debt before time runs out!

**Author:** Xander Yeo Kai Kiat   
**Course:** CSF03 - PRG1 Assignment

---

## 📖 Game Overview

You've taken out a loan to buy a small farm in Albatross Town. Your goal is to **pay off your debt of $100 within 20 days** while managing your energy, money, and resources wisely. Can you turn a profit and become a successful farmer?

---

## ✨ Features

### Core Gameplay
- **Farm Management**: Navigate a 5x5 grid farm to plant and harvest crops
- **Three Crop Types**: 
  - 🥬 **Lettuce** - Quick growth (2 days), low profit
  - 🥔 **Potato** - Medium growth (3 days), moderate profit
  - 🥦 **Cauliflower** - Slow growth (6 days), high profit
- **Energy System**: Each action costs energy; rest by ending the day
- **Day/Night Cycle**: 20-day time limit to achieve your goal
- **Save/Load System**: Save your progress and continue later

### Additional Features ⭐
1. **Limited Seed Bag Capacity** - Carry up to 10 seeds at a time
2. **High Score Board** - Compete for the highest profit after winning

---

## 🎮 How to Play

### Installation

1. **Requirements**: Python 3.x
2. **Download**: Clone or download this repository
3. **Run**: Execute the game file
   ```bash
   python sundrop_farm.py
   ```

### Main Menu Options

```
1) Start a new game
2) Show high scores
3) Load your saved game
0) Exit Game
```

---

## 🏘️ In Town

When in Albatross Town, you can:

| Option | Action |
|--------|--------|
| **1** | Visit Pierce's Seed Shop |
| **2** | Visit Your Farm |
| **3** | End the Day (restore energy to 10) |
| **9** | Save Game |
| **0** | Exit Game |

---

## 🛒 Seed Shop

### Available Seeds

| Seed | Price | Growth Time | Crop Value | Profit |
|------|-------|-------------|------------|--------|
| Lettuce | $2 | 2 days | $3 | $1 |
| Potato | $3 | 3 days | $6 | $3 |
| Cauliflower | $5 | 6 days | $14 | $9 |

**Note:** Your seed bag can only hold **10 seeds maximum**!

---

## 🚜 On the Farm

### Farm Layout
- **5x5 grid** with your farmhouse at the center (2,2)
- Each plot shows:
  - **Top row**: Crop type (LET/POT/CAU)
  - **Middle row**: Your position (X)
  - **Bottom row**: Days until harvest

### Controls

| Key | Action | Energy Cost |
|-----|--------|-------------|
| **W** | Move Up | 1 |
| **A** | Move Left | 1 |
| **S** | Move Down | 1 |
| **D** | Move Right | 1 |
| **P** | Plant Seed | 1 |
| **H** | Harvest Crop | 1 |
| **R** | Return to Town | 0 |

### Farming Tips 💡
1. **Plan ahead**: Cauliflower takes 6 days but gives the best profit
2. **Manage energy**: You only have 10 energy per day
3. **Watch the calendar**: You have 20 days to reach $100
4. **Optimize space**: Use all 24 available plots (excluding the house)
5. **Balance crops**: Mix quick and slow-growing crops for steady income

---

## 🏆 Winning & Losing

### Win Condition
- Have **$100 or more** by the end of **Day 20**
- Your profit (money - $100) is recorded on the high score board

### Lose Condition
- Have **less than $100** by the end of Day 20

---

## 💾 Save System

### How to Save
1. From the town menu, select option **9**
2. Game saves to `savegame.txt`
3. Game exits automatically after saving

### How to Load
1. From the main menu, select option **3**
2. Loads from `savegame.txt`
3. Continue where you left off!

---

## 📊 Game Statistics

Your stats are displayed at the top of each screen:

```
+--------------------------------------------------+
| Day 1             Energy: 10       Money: $20    |
| Your seeds:                                      |
|   Lettuce:           5                           |
+--------------------------------------------------+
```

---

## 🎯 Strategy Guide

### Early Game (Days 1-5)
- Buy **Lettuce** seeds for quick cash flow
- Plant immediately to maximize harvests
- Reinvest profits into more seeds

### Mid Game (Days 6-15)
- Transition to **Potato** for better profit margins
- Start planting **Cauliflower** if you have buffer money
- Keep some plots with quick crops for steady income

### Late Game (Days 16-20)
- Focus on **harvesting** existing crops
- Only plant if you have time to harvest
- Calculate if you'll reach $100 in time

---

## 📁 File Structure

```
sundrop_farm.py  # Main game file
savegame.txt              # Save file (created when you save)
scoreboard.txt            # High scores (created after winning)
README.md                 # This file
```

**Good luck, farmer! May your crops grow tall and your profits grow taller! 🌱💰**
