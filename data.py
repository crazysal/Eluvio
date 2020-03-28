from torch.utils.data import  DataLoader
from torchtext.data import  Dataset

class textDataLoader(DataLoader):
	"""class for textDataLoader
	   for now wrapper on default 
	   can add custom sampler etc later.
	"""
	def __init__(self, *args, **kwargs):
		super(textDataLoader, self).__init__(*args, **kwargs) 
		
class textDataSet(Dataset):
	"""class for textDataSet
	   for now wrapper on default 
	   can add custom sampler etc later.
	"""
	def __init__(self, examples, fields, filter_pred=None): 
			[('time_created', data.Field()), ('date_created', data.Field()),\
			('up_votes', data.Field()),('down_votes', data.Field()),('title', data.Field()),\
			('over_18', data.Field()),('author', data.Field()),('category',, data.Field())]

			
