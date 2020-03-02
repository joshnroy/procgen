from procgen import ProcgenEnv
import numpy as np

num_envs = 9
venv = ProcgenEnv(num_envs=num_envs, env_name="maze", start_level=1543, num_levels=1)

venv.reset()

while True:
    venv.render()
    venv.step(np.array([np.random.randint(15) for _ in range(num_envs)]))
