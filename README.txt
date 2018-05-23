To train:
   - python3 tools/train.py -c conf/train.cfg

To test:
   - python3 loop.py


To change training set:
either:
   - change data/train.txt
   - change conf/train.cfg line 7 (under DATASET)


To change test set:
   - change lists_f in loop.py (or containing_path in loop.py)

To change where test files are saved after recolor:
   - change output_dir in demo.py

To change model:
   - change model in demo.py

To create new priors based on training set:
   - run tools/create_prior_probs.py

To change priors:
   - copy prior file you want to prior_probs.npy
