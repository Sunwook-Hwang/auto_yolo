from auto_yolo import envs
from auto_yolo.models import air

readme = "Running AIR experiment."

distributions = [
    {'n_digits': 1,
     'scale_prior_mean': -2.9444389791664403,
     'scale_prior_std': 0.2,
     'shift_prior_std': 1.0},

    {'n_digits': 3,
     'scale_prior_mean': -2.197224577336219,
     'scale_prior_std': 0.2,
     'shift_prior_std': 1.0},

    {'n_digits': 5,
     'scale_prior_mean': -2.197224577336219,
     'scale_prior_std': 0.2,
     'shift_prior_std': 2.0},

    {'n_digits': 7,
     'scale_prior_mean': -1.3862943611198906,
     'scale_prior_std': 0.4,
     'shift_prior_std': 4.0},

    {'n_digits': 9,
     'scale_prior_mean': -0.4054651081081643,
     'scale_prior_std': 0.2,
     'shift_prior_std': 1.0}
]


for dist in distributions:
    n_digits = dist['n_digits']
    dist.update(
        min_digits=n_digits,
        max_digits=n_digits,
        max_time_steps=n_digits)


durations = dict(
    long=dict(
        max_hosts=1, ppn=16, cpp=1, gpu_set="0,1,2,3", wall_time="24hours",
        project="rpp-bengioy", cleanup_time="10mins",
        slack_time="10mins", n_repeats=6, step_time_limit="24hours"),

    build=dict(
        max_hosts=1, ppn=1, cpp=2, gpu_set="0", wall_time="20mins",
        project="rpp-bengioy", cleanup_time="2mins",
        slack_time="2mins", n_repeats=1, step_time_limit="2hours",
        config=dict(do_train=False), n_param_settings=1,),

    short=dict(
        max_hosts=1, ppn=3, cpp=2, gpu_set="0", wall_time="30mins",
        project="rpp-bengioy", cleanup_time="1mins",
        slack_time="1mins", n_repeats=1, config=dict(max_steps=100)),
)

config = dict(
    curriculum=[dict()],
    n_train=64000, run_all_time_steps=True,
    stopping_criteria="AP,max", threshold=0.99, patience=50000,
    render_hook=air.AIR_ComparisonRenderHook(),
)


envs.run_experiment(
    "air_run", config, readme, distributions=distributions,
    alg="air", task="arithmetic", durations=durations,
)
