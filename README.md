# Human-Mood-Encoder
This project converts a person's daily lifestyle signals into a numerical Mood Score.

# Project 1 — Human Mood Encoder



It is my first foundational AI systems project where I implement everything **from scratch without any libraries**.

The goal is to understand how real-world data is transformed into numerical signals and combined into a decision.

---

## Concept

Human reality can be represented as numbers.

Inputs:

- Sleep hours
- Coffee consumption
- Work completion
- Social interaction

Output:

- Mood Score (0–100)

This follows the basic AI pipeline:

Reality → Features → Model → Score

---

## Features Used

| Feature | Range | Meaning |
|--------|------|--------|
| Sleep Hours | 0–12 | Rest quality indicator |
| Coffee Cups | 0–10 | Stress / stimulation signal |
| Work Done | 0–100 | Productivity satisfaction |
| Social Interaction | 0–10 | Emotional health signal |

---

## System Design

### Step 1 — Input Collection

The program collects numerical lifestyle data from the user.

### Step 2 — Normalization

All inputs are scaled to a 0–1 range so different units can be compared fairly.

Example:

sleep_norm = sleep_hours / 12

This is a standard preprocessing technique used in machine learning.

---

### Step 3 — Weighted Scoring

Each feature is assigned an importance value (weight).

Formula:

mood =

sleep * 0.35  
+ work * 0.35  
+ social * 0.20  
- coffee * 0.10

This is a **linear model**:

score = Σ (weight × feature)

---

### Step 4 — Output

The score is converted into a percentage (0–100).

---

## Key AI Concepts Learned

- Feature Engineering
- Normalization
- Weighted Sum
- Linear Models
- Signal Processing
- Decision Systems

This project represents a basic artificial neuron computation.

---

## Why This Project Matters

This simple system demonstrates how:

- Fitness apps estimate wellness
- Productivity tools measure performance
- Mental health systems quantify lifestyle

Most real AI systems start as weighted decision engines before becoming complex models.

---

## Future Improvements

- Add mood categories (Bad / Neutral / Good / Excellent)
- Store daily data
- Learn weights automatically from past mood feedback
- Build a personal life analytics dashboard

---

## Goal

This project is part of my journey to become an **AI Systems Engineer** by building foundational systems from first principles.
