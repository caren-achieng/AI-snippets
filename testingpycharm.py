import gym

ics_env = gym.make('CartPole-v0')

# print(ics_env.action_space)

# for(int i=0; i < 50; i++)
#     {}

for episode in range(1, 171):
    score = 0
    state = ics_env.reset()
    done = False

    while not done:
        ics_env.render()
        action = ics_env.action_space.sample()
        newState, reward, done, info = ics_env.step(action)
        score += reward

    print("Episode: {}, Score: {}".format(episode, score))
