from tic_tac_toe import TicTacToeGame
import numpy as np
import random
import matplotlib.pyplot as plt


class Agent:
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=0.9):
        self.q_table = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma


    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0)


    def choose_action(self, state, valid_actions):
        if random.random() < self.epsilon:
            return random.choice(valid_actions)
        q_values = [self.get_q_value(state, action) for action in valid_actions]
        max_q = max(q_values)
        return valid_actions[q_values.index(max_q)]


    def update_q_value(self, state, action, reward, next_state, next_valid_actions):
        max_next_q = max([self.get_q_value(next_state, a) for a in next_valid_actions], default=0)
        old_q = self.get_q_value(state, action)
        self.q_table[(state, action)] = old_q + self.alpha * (reward + self.gamma * max_next_q - old_q)


class RandomOpponent:
    @staticmethod
    def choose_action(valid_actions):
        return random.choice(valid_actions)


def play_game(agent, opponent, game, train=True):
    game.__init__()
    state = tuple(tuple(row) for row in game.matrix)
    total_reward = 0

    while game.check_game:
        valid_actions = [(x, y) for x in range(3) for y in range(3) if game.matrix[x][y] == '0']
        
        if not valid_actions:
            break 

        action = agent.choose_action(state, valid_actions)
        game._step(action[0], action[1], 1)
        next_state = tuple(tuple(row) for row in game.matrix)
        reward = 1 if game._check_winner() else 0
        total_reward += reward

        if reward or not valid_actions:
            if train:
                agent.update_q_value(state, action, reward, next_state, [])
            break

        valid_actions = [(x, y) for x in range(3) for y in range(3) if game.matrix[x][y] == '0']
        if not valid_actions:
            break

        opp_action = opponent.choose_action(valid_actions)
        game._step(opp_action[0], opp_action[1], 2)
        if game._check_winner():
            reward = -1

        if train:
            agent.update_q_value(state, action, reward, next_state, valid_actions)
        state = next_state

    return total_reward


def train_agent(iterations=10000):
    agent = Agent()
    opponent = RandomOpponent()
    game = TicTacToeGame()

    rewards = []
    avg_rewards = []

    for i in range(iterations):
        reward = play_game(agent, opponent, game, train=True)
        rewards.append(reward)
        if (i + 1) % 100 == 0:
            avg_rewards.append(np.mean(rewards[-100:]))
            print(f"Итерация {i + 1}: средняя награда = {avg_rewards[-1]}")

    return avg_rewards


avg_rewards = train_agent()

plt.plot(avg_rewards)
plt.xlabel("Итерации (по 100 игр)")
plt.ylabel("Средняя награда")
plt.title("Зависимость награды от количества шагов обучения")
plt.show()
