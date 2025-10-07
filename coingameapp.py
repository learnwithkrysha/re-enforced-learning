import streamlit as st
import numpy as np
import random

st.title("Coin Game RL: Collect Coins to Reach 5")

# Parameters
learning_rate = st.sidebar.slider("Learning Rate", 0.01, 1.0, 0.1)
discount = st.sidebar.slider("Discount Factor", 0.1, 1.0, 0.9)
epsilon = st.sidebar.slider("Exploration (epsilon)", 0.0, 1.0, 0.2)
episodes = st.sidebar.slider("Number of Episodes", 1, 100, 20)

# Initialize Q-table: states 0-5 coins, actions: collect 1 or 2 coins
Q = [[0, 0] for _ in range(6)]

# Run Simulation
if st.button("Run Coin Game Simulation"):
    output = ""
    for episode in range(episodes):
        state = 0
        output += f"\nEpisode {episode + 1}\n"
        while state < 5:
            # Display current coins
            coins_display = ['C'] * state + ['-'] * (5 - state)
            output += "".join(coins_display) + "\n"

            # Choose action: epsilon-greedy
            if random.random() < epsilon:
                action = random.choice([0, 1])
            else:
                action = 0 if Q[state][0] > Q[state][1] else 1

            # Take action
            if action == 0:
                next_state = min(state + 1, 5)
            else:
                next_state = min(state + 2, 5)

            # Reward
            reward = 1 if next_state == 5 else 0

            # Update Q-value
            Q[state][action] += learning_rate * (reward + discount * max(Q[next_state]) - Q[state][action])

            state = next_state

    # Display simulation output
    st.text(output)

    # Show final Q-values
    st.subheader("Final Q-values")
    for s in range(6):
        st.write(f"Coins: {s}, Q-values: {Q[s]}")

    # Show learned policy
    policy = ["Collect 1" if Q[s][0] > Q[s][1] else "Collect 2" for s in range(5)]
    st.subheader("Learned Policy")
    st.write(policy)