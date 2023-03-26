import numpy as np

from config.logistic_regression_config import cfg
from datasets.digits_dataset import Digits
from models.logistic_regression_model import LogReg
from utils.enums import SetType
from utils.visualisation import Visualisation

train = Digits(cfg)(SetType.train)
valid = Digits(cfg)(SetType.valid)
test = Digits(cfg)(SetType.test)
log_reg = LogReg(cfg, Digits(cfg).k, Digits(cfg).d)
log_reg.train(np.array(train['inputs']), np.array(train['targets'].iloc[:, 0].astype(int)), train['onehotencoding'],
              np.array(valid['inputs']), np.array(valid['targets'].iloc[:, 0].astype(int)), valid['onehotencoding'])
Visualisation.target_func(log_reg.BASK_UP)
