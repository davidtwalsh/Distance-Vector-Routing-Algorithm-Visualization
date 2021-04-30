# Distance-Vector-Routing-Algorithm-Visualization

## About The Program
This program serves to visualize what's going on during a distance vector routing algorithm between many connected nodes. The step-by-step visualizion, (mainGUI.py) allows the user to advance the algorithm at their own pace. Each time the advance button is pressed, the algorithm moves forward one step. Although it does a good job at visualizing each step of the algorithm, it doesn't do a good job at the highlighting the big picture because time is not simulated.

The real time visualization (mainGUITime.py) has basically the opposite effect of the step-by-step visualization. Although it does not do a good job at visualizing each step of the algorithm (because in reality many events are happening simultaneously), it does a great job at showing the big picture of the distance vector routing algorithm. Packets are simulated as colored circles moving along the links between the nodes in this simulation.

I hope that users can use both visualizations to get a better understanding of how the distance vector routing algorithm works. Please not that this python application requires pygame in order to run

The program is written entirely in Python 3.8.5 (other versions may work)
Dependencies:
* pygame v:1.9.6 (other versions may work)



The step-by-step visualization

![GiftStepbyStep](https://user-images.githubusercontent.com/46041406/116754482-cc437300-a9d6-11eb-81ec-8e9a400c9b42.gif)


The real-time visualization

![GifTime](https://user-images.githubusercontent.com/46041406/116754570-f301a980-a9d6-11eb-8446-b394fc8fb251.gif)
