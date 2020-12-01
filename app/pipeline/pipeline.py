from preprocessing import preprocessing
from utils import utils
from model import model

@utils.printing_progress
def pipeline(to = 400):
	data = preprocessing.preprocess(to)
	model.model(data)

pipeline()



