# model_definition.py
import argparse
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class GCNModel(nn.Module):
    def __init__(self, input_dim, hidden_dims, output_dim, dropout_rate=0.5):
        super(GCNModel, self).__init__()
        dims = [input_dim] + hidden_dims + [output_dim]
        self.convs = nn.ModuleList()
        self.dropouts = nn.ModuleList()
        for i in range(len(dims)-2):
            self.convs.append(GCNConv(dims[i], dims[i+1]))
            self.dropouts.append(nn.Dropout(p=dropout_rate))
        self.final_conv = GCNConv(dims[-2], dims[-1])

    def forward(self, x, edge_index):
        for conv, dropout in zip(self.convs, self.dropouts):
            x = conv(x, edge_index)
            x = F.relu(x)
            x = dropout(x)
        x = self.final_conv(x, edge_index)
        return x

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dim', type=int, required=True)
    parser.add_argument('--hidden_dims', type=str, required=True)  # "64,64,32,32"
    parser.add_argument('--output_dim', type=int, required=True)
    parser.add_argument('--dropout_rate', type=float, default=0.5)
    parser.add_argument('--gcn_model', type=str, required=True)
    args = parser.parse_args()

    hidden_dims = [int(x) for x in args.hidden_dims.split(',')]

    model = GCNModel(args.input_dim, hidden_dims, args.output_dim, args.dropout_rate)
    os.makedirs(os.path.dirname(args.gcn_model), exist_ok=True)
    torch.save(model.state_dict(), args.gcn_model)
    print(f"Model saved to {args.gcn_model}")
