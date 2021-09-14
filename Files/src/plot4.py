from post_process_ok2 import postProcess
import matplotlib.pyplot as plt
import numpy as np

# # Meta-World button topdown:
# testHM_ev_0_01 = 'DCOACH_HM-True_e-0.01_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testHM_ev_0_1  = 'DCOACH_HM-True_e-0.1_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testHM_ev_1    = 'DCOACH_HM-True_e-1.0_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
#
#
# testNOHM_ev_0_01_15001    = 'DCOACH_HM-False_e-0.01_B-15001_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
#
# testNOHM_ev_1_15001     = 'DCOACH_HM-False_e-1.0_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown2_rep-{}.csv'
# testNOHM_tr_1_15001     = 'DCOACH_HM-False_e-1.0_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown2_rep-{}.csv'
#
# testNOHM_ev_0_01 = 'DCOACH_HM-False_e-0.01_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_ev_0_1  = 'DCOACH_HM-False_e-0.1_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_ev_1    = 'DCOACH_HM-False_e-1.0_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
#
# testNOHM_tr_0_01    = 'DCOACH_HM-False_e-0.01_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_tr_0_1    = 'DCOACH_HM-False_e-0.1_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_tr_1    = 'DCOACH_HM-False_e-1.0_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
#
# testHM_tr_0_01    = 'DCOACH_HM-True_e-0.01_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testHM_tr_0_1    = 'DCOACH_HM-True_e-0.1_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testHM_tr_1    = 'DCOACH_HM-True_e-1.0_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
#
# testNOHM_ev_0_01 = 'DCOACH_HM-False_e-0.01_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_ev_0_01_15001    = 'DCOACH_HM-False_e-0.01_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep3-{}.csv'
# path_ev = './results/'
# path_tr = './results/'
# #tests_Evaluation = [testHM_ev_0_01 , testHM_ev_0_1, testHM_ev_1, testNOHM_ev_0_01, testNOHM_ev_0_1, testNOHM_ev_1, testNOHM_ev_0_01_15001, testHM_ev_0_01_15001]
# tests_Evaluation = [testNOHM_ev_0_01_15001,testNOHM_ev_0_01  ]
# tests_Training =   [testHM_tr_0_01]


# Meta-World hockey:
testHM_ev_0_01 = 'DCOACH_HM-True_e-0.01_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep-{}.csv'
testHM_ev_0_1  = 'DCOACH_HM-True_e-0.1_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep-{}.csv'
testHM_ev_1    = 'DCOACH_HM-True_e-1.0_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep-{}.csv'


testNOHM_ev3_0_01_100 = 'DCOACH_HM-False_e-0.01_B-100_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_ev3_0_01_500 = 'DCOACH_HM-False_e-0.01_B-500_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_ev3_0_01_1000 = 'DCOACH_HM-False_e-0.01_B-1000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_ev3_0_01_5000 = 'DCOACH_HM-False_e-0.01_B-5000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_ev3_0_01_10000 = 'DCOACH_HM-False_e-0.01_B-10000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_ev3_0_01_15000 = 'DCOACH_HM-False_e-0.01_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'


testHM_ev3_1_500 = 'DCOACH_HM-True_e-1.0_B-500_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testHM_ev3_0_1_500 = 'DCOACH_HM-True_e-0.1_B-500_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testHM_ev3_0_01_500 = 'DCOACH_HM-True_e-0.01_B-500_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_ev3_1_500 = 'DCOACH_HM-False_e-1.0_B-500_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_ev3_0_1_500 = 'DCOACH_HM-False_e-0.1_B-500_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_ev3_0_01_500 = 'DCOACH_HM-False_e-0.01_B-500_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'



testNOHM_tr3_0_01 = 'DCOACH_HM-False_e-0.01_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_tr3_0_01_100 = 'DCOACH_HM-False_e-0.01_B-100_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_tr3_0_01_500 = 'DCOACH_HM-False_e-0.01_B-500_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_tr3_0_01_1000 = 'DCOACH_HM-False_e-0.01_B-1000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_tr3_0_01_5000 = 'DCOACH_HM-False_e-0.01_B-5000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'
testNOHM_tr3_0_01_10000 = 'DCOACH_HM-False_e-0.01_B-10000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep3-{}.csv'







testNOHM_ev_0_01 = 'DCOACH_HM-False_e-0.01_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep-{}.csv'
testNOHM_ev_0_1  = 'DCOACH_HM-False_e-0.1_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep-{}.csv'
testNOHM_ev_1    = 'DCOACH_HM-False_e-1.0_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep-{}.csv'

testHM_tr_1    = 'DCOACH_HM-True_e-0.1_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-hockey_rep-{}.csv'

path_ev = './results/'
path_tr = './results/'
#tests_Evaluation = [testNOHM_ev3_0_01_100, testNOHM_ev3_0_01_500, testNOHM_ev3_0_01_1000, testNOHM_ev3_0_01_5000, testNOHM_ev3_0_01_10000, testNOHM_ev3_0_01_15000]
#tests_Evaluation = [testHM_ev3_1_500, testHM_ev3_0_1_500, testHM_ev3_0_01_500, testNOHM_ev3_1_500, testNOHM_ev3_0_1_500, testNOHM_ev3_0_01_500]
tests_Evaluation = [testHM_ev_1, testHM_ev_0_1, testHM_ev_0_01, testNOHM_ev_1, testNOHM_ev_0_1, testNOHM_ev_0_01]


tests_Training =   [testNOHM_tr3_0_01_100]

# # KUKA park results
# path_ev = './results/kuka-park/'
# path_tr = './results/kuka-park/'
#
# test_kuka_park_ev    = 'DCOACH_HM-True_e-0.3_B-10000_Eval-True_tau-0.0001_lr-0.003_HMlr-0.0003_task-kuka-park-cardboard_rep-{}.csv'
# test_kuka_park_tr    = 'DCOACH_HM-True_e-0.3_B-10000_Eval-False_tau-0.0001_lr-0.003_HMlr-0.0003_task-kuka-park-cardboard_rep-{}.csv'
#
# tests_Evaluation = [test_kuka_park_ev]
# tests_Training =   [test_kuka_park_tr]


# # KUKA football results
# path_ev = './results/kuka-football/'
# path_tr = './results/kuka-football/'
#
# test_kuka_football_ev    = 'DCOACH_HM-True_e-0.5_B-10000_Eval-True_tau-0.0001_lr-0.003_HMlr-0.003_task-kuka-football_rep-{}.csv'
# test_kuka_football_tr    = 'DCOACH_HM-True_e-0.5_B-10000_Eval-False_tau-0.0001_lr-0.003_HMlr-0.003_task-kuka-football_rep-{}.csv'
#
# tests_Evaluation = [test_kuka_football_ev]
# tests_Training =   [test_kuka_football_tr]


# Meta-World hockey BUFFER comparison:


# testNOHM_ev_0_01_500 = 'DCOACH_HM-False_e-0.01_B-500_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_ev_0_01_1000  = 'DCOACH_HM-False_e-0.01_B-1000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_ev_0_01_5000    = 'DCOACH_HM-False_e-0.01_B-5000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_ev_0_01_10000    = 'DCOACH_HM-False_e-0.01_B-10000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_ev_0_01_15000    = 'DCOACH_HM-False_e-0.01_B-15000_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
#
#
# testNOHM_ev_0_01_15001    = 'DCOACH_HM-False_e-0.01_B-15001_Eval-True_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testNOHM_tr_0_01_15001    = 'DCOACH_HM-False_e-0.01_B-15001_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
# testHM_tr_1    = 'DCOACH_HM-True_e-0.1_B-15000_Eval-False_tau-1e-05_lr-0.005_HMlr-0.001_task-button_topdown_rep-{}.csv'
#
# path_ev = './results/'
# path_tr = './results/'
# tests_Evaluation = [testNOHM_ev_0_01, testNOHM_ev_0_01_15001]
# tests_Training =   [testNOHM_tr_0_01_15001]


cm = 1/2.54

fig, axs= plt.subplots(2, figsize=(17*cm, 17*cm))
ax2 = axs[0].twiny()
ax3 = axs[1].twiny()

mujoco_timestep = 0.0125




# %%%%%%%%%%%%%%%%%%%%%%%%
# TRAINING PLOT: FEEDBACK
# %%%%%%%%%%%%%%%%%%%%%%%%

for test_tr in tests_Training:


    timesteps_processed_list, return_processed_list,  minutes_processed_list, feedback_processed_list, tau, e, human_model, pl_ag_processed_list, pl_hm_processed_list, buffer_size = postProcess(test_tr, path_tr)

    a = np.array(feedback_processed_list)
    feedback_mean = np.mean(a, axis=0)

    a = np.array(minutes_processed_list)
    minutes_list = np.mean(a, axis=0)

    a = np.array(pl_ag_processed_list)
    pl_ag_list = np.mean(a, axis=0)

    a = np.array(pl_hm_processed_list)
    pl_hm_list = np.mean(a, axis=0)

    a = np.array(timesteps_processed_list)
    timesteps_list = np.mean(a, axis=0)
    simulated_time = timesteps_list * mujoco_timestep / 60


    print('feedback_mean', feedback_mean)
    print('minutes_list ', minutes_list )

    if human_model == "yes" and e == 0.01:
        colorPlot = '#150E56'  # blue
    if human_model == "yes" and e == 0.1:
        colorPlot = '#2978B5'  # green
    if human_model == "yes" and e == 1:
        colorPlot = '#8AB6D6'  # violet

    if human_model == "no" and e == 0.01:
        colorPlot = '#BE0000'  # orange
    if human_model == "no" and e == 0.1:
        colorPlot = '#FF6B6B'  # red
    if human_model == "no" and e == 1:
        colorPlot = '#FDD2BF'  # brown

    axs[1].plot(simulated_time, feedback_mean, linewidth=2.0, color=colorPlot, zorder=0)
    axs[1].set_ylabel('Accumulated feedback')
    axs[1].set_xlabel('min')
    axs[1].set_title('Training of task: Meta-World hockey')

    ax3.xaxis.set_ticks_position('bottom')
    ax3.xaxis.set_label_position('bottom')
    ax3.spines['bottom'].set_position(('outward', 40))
    ax3.set_xlabel('time steps')

    if e == 0.01 and buffer_size == 100:

        feedback_100 = np.interp(100, feedback_mean, timesteps_list)
        feedback_500 = np.interp(500, feedback_mean, timesteps_list)
        feedback_1000 = np.interp(1000, feedback_mean, timesteps_list)
        feedback_5000 = np.interp(5000, feedback_mean, timesteps_list)
        feedback_10000 = np.interp(10000, feedback_mean, timesteps_list)
        feedback_15000 = np.interp(15000, feedback_mean, timesteps_list)



        ax3.axvline(x=feedback_100, linestyle='--', color='#150E56', label="100")
        ax3.axvline(x=feedback_500, linestyle='--', color='#2978B5', label="500")
        ax3.axvline(x=feedback_1000, linestyle='--', color='#8AB6D6', label="1000")
        ax3.axvline(x=feedback_5000, linestyle='--', color='#BE0000', label="5000")
        ax3.axvline(x=feedback_10000, linestyle='--', color='#FF6B6B', label="10000")
        ax3.axvline(x=feedback_15000, linestyle='--', color='#FDD2BF', label="15000")

        ax2.axvline(x=feedback_100, linestyle='--', color='#150E56', label="100")
        ax2.axvline(x=feedback_500, linestyle='--', color='#2978B5', label="500")
        ax2.axvline(x=feedback_1000, linestyle='--', color='#8AB6D6', label="1000")
        ax2.axvline(x=feedback_5000, linestyle='--', color='#BE0000', label="5000")
        ax2.axvline(x=feedback_10000, linestyle='--', color='#FF6B6B', label="10000")
        ax2.axvline(x=feedback_15000, linestyle='--', color='#FDD2BF', label="15000")




    ax3.plot(timesteps_list, feedback_mean, color=colorPlot, alpha=0)
    ax3.legend(loc='lower right', title="Accumulated feedback: ", bbox_to_anchor=(1.5, 0.2),
                  ncol=1)
    plt.xticks(rotation=5)




# %%%%%%%%%%%%%%%%%%%%%%%%
# EVALUATION PLOT: SUCCESS
# %%%%%%%%%%%%%%%%%%%%%%%%

for test_ev in tests_Evaluation:

    if "Eval-True" in test_ev :
        evaluation = "True"
    else:
        evaluation = "False"

    if "hockey" in test_ev :
        task = "Hockey"
    if "button" in test_ev :
        task = "Button"
    if "reach" in test_ev :
        task = "Reach"
    if "kuka" in test_ev :
        task = "kuka"




    timesteps_processed_list, return_processed_list, minutes_processed_list, feedback_processed_list, tau, e, human_model, pl_ag_processed_list, pl_hm_processed_list, buffer_size = postProcess(test_ev, path_ev)


    a = np.array(return_processed_list)
    return_mean = np.mean(a, axis =0)
    return_std = np.std(a, axis=0)

    a = np.array(timesteps_processed_list)
    timesteps_list = np.mean(a, axis=0)
    simulated_time = timesteps_list * mujoco_timestep /60

    a = np.array(minutes_processed_list)
    minutes_list = np.mean(a, axis=0)





    print('minutes list: ', len(minutes_list))
    print("return_mean: ", len(return_mean))
    print("timesteps_list: ", len(timesteps_list))

    z = np.polyfit(simulated_time, return_mean, 20)

    p = np.poly1d(z)
    print("---------")
    print("p: ", z)
    # ,





    # if human_model == "yes" and e == 0.01:
    #     colorPlot = '#150E56'  # blue
    # if human_model == "yes" and e == 0.1:
    #     colorPlot = '#2978B5'  # green
    # if human_model == "yes" and e == 1:
    #     colorPlot = '#8AB6D6'  # violet
    #
    # if human_model == "no" and e == 0.01:
    #     colorPlot = '#BE0000'  # orange
    # if human_model == "no" and e == 0.1:
    #     colorPlot = '#FF6B6B'  # red
    # if human_model == "no" and e == 1:
    #     colorPlot = '#FDD2BF'  # brown


    if human_model == "yes" and e == 0.01 and buffer_size == 500:
        colorPlot = '#150E56'  # blue
    if human_model == "yes" and e == 0.1 and buffer_size == 500:
        colorPlot = '#2978B5'  # green
    if human_model == "yes" and e == 1 and buffer_size == 500:
        colorPlot = '#8AB6D6'  # violet

    if human_model == "no" and e == 0.01 and buffer_size == 500:
        colorPlot = '#BE0000'  # orange
    if human_model == "no" and e == 0.1 and buffer_size == 500:
        colorPlot = '#FF6B6B'  # red
    if human_model == "no" and e == 1 and buffer_size == 500:
        colorPlot = '#FDD2BF'  # brown

    # if human_model == "no" and e == 0.01 and buffer_size == 100:
    #     colorPlot = '#72956c'  # blue
    # if human_model == "no" and e == 0.01 and buffer_size == 500:
    #     colorPlot = '#517b5c'  # green
    # if human_model == "no" and e == 0.01 and buffer_size == 1000:
    #     colorPlot = '#2f604b'  # violet
    #
    # if human_model == "no" and e == 0.01 and buffer_size == 5000:
    #     colorPlot = '#ffb600'  # orange
    # if human_model == "no" and e == 0.01 and buffer_size == 10000:
    #     colorPlot = '#ff7900'  # red
    # if human_model == "no" and e == 0.01 and buffer_size == 15000:
    #     colorPlot = '#ff4800'  # brown









    e = '{:,g}'.format(e)
    buffer_size = '{:,g}'.format(buffer_size)


    #return_mean = np.average(return_processed_list, axis=0)
    #return_std = np.std(return_processed_list, axis=0)




    axs[0].plot(simulated_time, return_mean, linewidth=0.1, zorder=0, color=colorPlot)
    axs[0].plot(simulated_time, p(simulated_time), linewidth=2.0, color=colorPlot, zorder=1, label='H: ' + human_model + ', Buffer size: ' + str(buffer_size) + ', e: ' + str(e))
    #axs[0].fill_between(minutes_list, return_mean - return_std, return_mean + return_std, alpha=0.02, color=colorPlot)


    #plt.xlabel("Time steps")
    #plt.ylim(0, 1.2)
    axs[0].set_ylabel('% of success')
    axs[0].set_xlabel('min')

    axs[0].set_title('Evaluation of task: Meta-World hockey')
    axs[0].legend(loc="lower right")
    axs[0].legend(loc='lower right', bbox_to_anchor=(1.5, 0.2),
              ncol=1)




    # ax2.set_frame_on(True)
    # ax2.patch.set_visible(False)
    ax2.xaxis.set_ticks_position('bottom')
    ax2.xaxis.set_label_position('bottom')
    ax2.set_xlabel('time steps')
    ax2.spines['bottom'].set_position(('outward', 40))
    plt.rc('legend', fontsize=8)  # legend fontsize




    ax2.plot(timesteps_list, p(simulated_time), color=colorPlot, alpha=0)
    plt.xticks(rotation=5)





axs[0].grid(linestyle='--')
axs[1].grid(linestyle='--')


#fig.subplots_adjust(hspace=0.2, top=0.95, bottom=0.075) # Space between the subplots
fig.subplots_adjust(hspace=0.65, bottom=0.15,  top=0.96, right=0.6) # Space between the subplots

plt.show()