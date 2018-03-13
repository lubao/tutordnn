import gym
env = gym.make('SpaceInvaders-v0')
env.reset()
env.render()
print env.__dict__
print env.observation_space,\
    env.action_space,\
    env.reward_range,\
    env.env._action_set
