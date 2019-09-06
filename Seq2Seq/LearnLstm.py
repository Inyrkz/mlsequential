import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)


class MyLstm(nn.Module):

    def __init__(self):
        super(MyLstm, self).__init__()

    def forward(self, *input):
        pass


lstm = nn.LSTM(3, 3)
# List of 5 random numbers forming the sequence.
inputs = [torch.randn(1, 3) for _ in range(5)]

# initialize the hidden state.
hidden = (torch.randn(1,1,3), torch.randn(1,1,3))
for i in inputs:
    # Step through the sequence one element at a time.
    # after each step, hidden contains the hidden state.
    out, hidden = lstm(i.view(1,1,-1), hidden)


# alternatively, we can do the entire sequence all at once.
# the first value returned by LSTM is al of the hidden states throughout
# the sequence. The second is just the most recent hidden state
# (compare the last slice of "out" with "hidden" below, they are the same)
# The reason for this is that:
# "out" will give you access to all hidden states in the sequence
# "hidden" will allow you to continue the sequence and backpropagate,
# by passing it as an argument to the lstm at a later time
# Add the extra 2nd dimension
inputs = torch.cat(inputs).view(len(inputs), 1, -1)
hidden = (torch.randn(1,1,3), torch.randn(1,1,3)) # clean out hidden state
out, hidden = lstm(inputs, hidden)
print(out)
print(hidden)
