

import sys
from os.path import dirname
print(sys.path)
sys.path.append(dirname(__file__))
#sys.path.append('/Users/vincenzo/CERM/secondary_structure_predictor_v0_1')

print("///", dirname(__file__))
print(sys.path)
import torch
import os

#import secondaryStructurePredictor
#from secondaryStructurePredictor import secStructPredictor
from secondaryStructurePredictor.secStructPredictor import *

def test_prediction():
	main()


def main():
	if len(sys.argv) <= 1:
		aa_sequence = "ACDEFGHIKLMNPQRSTVWY"
	else:
		aa_sequence = sys.argv[1].upper()

	print(aa_sequence)

	struct_types = get_struct_types()

	rnn = get_model_architecture()
	configuration = get_model_configuration()
	rnn.load_state_dict(configuration)

	out_idxs = predictSecStructure(rnn, aa_sequence)
	predicted = [struct_types[j] for j in out_idxs]
	print("aminoacids : ",list(aa_sequence))
	print("sec. struct: ", predicted)


if __name__ == '__main__':
    main()