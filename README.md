Following is the source code for the article "Prediction-based Resource Allocation using LSTM and maximum ﬂow and minimum cost algorithm" by Gyunam Park and [Minseok Song](http://mssong.postech.ac.kr) presented at the [1st International Conference on Process Mining](https://icpmconference.org) and submitted to the *information systems* (special issue).

The code provided in this repository can be readily used to optimize resource scheduling in non-clairvoyant online job shop environment

### Requirements:

- This code is written in Python3.6. In addition, you need to install a few more packages.

  - networkx
  - numpy
  - pandas
  - keras
  - tensorflow
  - PyProM

- To install,

  ```
  $ cd prediction_based_resource_allocation
  $ pip install -r requirements.txt
  $ cd ..
  $ git clone https://github.com/gyunamister/PyProM.git
  ```



### Implementation:

- **Evaluation**
  - On artificial log,
    - experiments for RQ1 and RQ2:  Type `$ sh exp_1.sh` to optimize resource allocation with the proposed method and `$ sh exp_1-baseline.sh` to optimize resource allocation with the baseline approach.
    - experiments for RQ3: Type `sh exp_2.sh` to optimize resource allocation with the proposed method by varing the prediction accuracy.
  - On real-life log,
    - experiments for RQ1 and RQ2: Type `$ sh exp_3.sh` to optimize resource allocation with the proposed method and `$ sh exp_3-baseline.sh` to optimize resource allocation with the baseline approach.
- **Brief Explanation**
  - The logs are listed in "./sample_data". The artificial log is generated by simulating a business process in an emergency department. Detailed implementation for the simulation is in data/log_generator.py
  - Phase 1 of our method (*prediction model construction*) is implemented in "prediction/model.py". Configuration is set on "prediction/config.py" and the training is done by `python train.py`. The resulting prediction model is saved in a directory "./prediction/checkpoints".
  - Phase 2 of our method (prediction model construction) is implemented in optimizer/suggested.py, while the baseline method is implemented in optimizer/baseline.py


  ### Environment:
  
  - conda create env -n seminar python=3.6
  - conda activate seminar
  - pip install -r requirements.txt
  - cd .. 
  - git clone https://github.com/gyunamister/PyProM.git
  - cd PyProM
  - pip install . 
  - cd ..
  - cd seminarcode

# env: sem6clone > sem6 
  