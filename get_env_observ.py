from gym import envs
import gym

class NullE:
    def __init__(self):
        self.observation_space = self.action_space = self.reward_range = "N/A"

envall = envs.registry.all()

table = "|Environment Id|Observation Space|Action Space|Reward\
Range|tStepL|Trials|rThresh\n" # |Local|nonDet|kwargs|
table += "|---|---|---|---|---|---|---|---|---|---|\n"

result = []
for e in envall:
    try:
        env = e.make()
    except:
        env = gym.make(e.id)
        #print e._entry_point
        #continue  #  Skip these for now
    #table += '| {}|{}|{}|{}|{}|{}|{}|\n'.format(e.id,   #|{}|{}|{}
    #   env.observation_space, env.action_space, env.reward_range,
    #   e.timestep_limit, e.trials, e.reward_threshold) # ,
       # getattr(e, 'local_only', -1), e.nondeterministic, getattr(e, 'kwargs',
       # ""))
    result.append([
        e.id,
        e._entry_point,
        env.observation_space, 
        env.action_space,
        env.reward_range,
        e.timestep_limit, 
        e.trials, 
        e.reward_threshold
    ])
#print table
for r in result:
    print r
#print len(result)
