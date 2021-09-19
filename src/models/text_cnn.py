import torch
import torch.nn as nn
import torch.nn.functional as F

class TextCNN(nn.Module):
    """
    An implement of TextCNN
    """
    def __init__(self, args):
        super(TextCNN, self).__init__()

        N = args.vocab_size
        D = args.embed_dim
        C = args.class_num
        Ci = 1
        Co = args.kernel_num
        Ks = args.kernel_sizes

        Ks = Ks.replace('[', '').replace(']', '').split(",") if isinstance(Ks, str) else Ks
        
        self.embed = nn.Embedding(N, D)
        self.convs = nn.ModuleList([nn.Conv2d(Ci, Co, (K, D)) for K in Ks])
        self.dropout = nn.Dropout(args.dropout_rate)
        self.fc = nn.Linear(len(Ks) * Co, C)

        self.embed.weight.requires_grad = args.static
    
    def forward(self, input):
        """
        Args:
            input: B * L, id style torch tensor
        """
        x = self.embed(input)  # B * L * D
        x = x.unsqueeze(1) # B * 1 * L * D
        x = [F.relu(conv(x)).squeeze(3) for conv in self.convs] # [(B * Co * L), ..] * len(Ks)
        x = [F.max_pool1d(y, y.size(2)).squeeze(2) for y in x]  # [(B * Co), ..] * len(Ks)
        x = torch.cat(x, 1)
        x = self.dropout(x)
        logit = self.fc(x)
        return logit
