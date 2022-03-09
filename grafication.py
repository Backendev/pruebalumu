import matplotlib
import matplotlib.pyplot as plt

def generate_grafics(time_results):
    list_times_mode_count = len(time_results)
    list_times_mode_1 = [v['mode_1']['time'] for v in [kv for ki,kv in time_results.items()]]
    list_times_mode_2 = [v['mode_2']['time'] for v in [kv for ki,kv in time_results.items()]]
    list_times_mode_3 = [v['mode_3']['time'] for v in [kv for ki,kv in time_results.items()]]

    plt.plot([i for i in range(0,list_times_mode_count)],list_times_mode_1, label='Mode 1')
    plt.plot([i for i in range(0,list_times_mode_count)],list_times_mode_2, label='Mode 2')
    plt.plot([i for i in range(0,list_times_mode_count)],list_times_mode_3, label='Mode 3')
    plt.xlabel('Inputs')
    plt.ylabel('Time')
    plt.title("Complexity Time-inputs Modes")
    plt.legend()
    plt.savefig('time_inputs_all_modes.png')

    fig_1 = plt.figure("Complexity foreach mode")
    fig_1.subplots_adjust(hspace=0.5,wspace=0.5)
    ax = fig_1.add_subplot(2,2,1)
    ax.plot([i for i in range(0,list_times_mode_count)],list_times_mode_1, label='Mode 1')
    ax.set_ylabel('Time')
    ax.set_xlabel('Inputs')
    ax.set_title("Mode 1")


    ax = fig_1.add_subplot(2,2,2)
    ax.plot([i for i in range(0,list_times_mode_count)],list_times_mode_2, label='Mode 2')
    ax.set_ylabel('Time')
    ax.set_xlabel('Inputs')
    ax.set_title("Mode 2")


    ax = fig_1.add_subplot(2,2,3)
    ax.plot([i for i in range(0,list_times_mode_count)],list_times_mode_3, label='Mode 3')
    ax.set_ylabel('Time')
    ax.set_xlabel('Inputs')
    ax.set_title("Mode 3")


    plt.savefig('time_inputs_foreach_modes.png')