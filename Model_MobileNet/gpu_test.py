import torch
print(torch.cuda.is_available())  # Should be True
print(torch.version.cuda)  # Shows the CUDA version PyTorch is built with
