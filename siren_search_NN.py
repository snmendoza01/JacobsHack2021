import os
import torch
from torch import nn

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")


params_dict = {
    'danceability': 0,
    'energy': 1,
    'loudness': 2,
    'key': 3,
    'speechiness': 4,
    'acousticness': 5,
    'instrumentalness': 6,
    'liveness': 7,
    'mode': None
}


class NeuralNetwork(nn.Module):
    """Build the Neural Network to be used for prediction
        Inherited from nn.Module
    """
    def __init__(self, dim: int):
        super(NeuralNetwork, self).__init__()
        self.dim = dim
        self.flatten = nn.Flatten()
        self.linear_tanh_relu_stack = nn.Sequential(
            nn.Linear(dim, 128),
            nn.Tanh(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 1),
        )
        return None


    def forward(self, x):
        return self.linear_tanh_relu_stack(x)


def optimize(model: NeuralNetwork, data: torch.Tensor):
    """Oprimize the weights of a model given a set of data

    Args:
        model (NeuralNetwork): Model to be optimized
        data (torch.Tensor): Data used for optimization

    Returns:
        None: The model is modified internally
    """
    learning_rate = 1e-3
    epochs = 5
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    for epoch in range(epochs):
        # print(data)
        for (x, y) in data:
            pred = model(x)
            loss = loss_fn(pred, y)

            # Backpropagation
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
        # loss = loss.item()
        # print(f"loss: {loss:>7f} \nEpoch: {epoch}")
        
    return None


def save_weights(my_model: NeuralNetwork, path: str):
    """Save the weights of an already optimized model

    Args:
        my_model (NeuralNetwork): Model with weights to be saved
        path (str): path to save the model's weights (usually with a .pt extension)

    Returns:
        None
    """
    torch.save(my_model.state_dict(), path)
    return None


def load_weights(new_model: NeuralNetwork, path: str):
    """Load weights into a model

    Args:
        new_model (NeuralNetwork): New model with non-optimized weights
        path (str): Path with the weights to be used

    Returns:
        None: Model is updated internally
    """
    new_model.load_state_dict(torch.load(path))
    return None


def properties_to_data(dict_data: dict):
    """Transform data in dict type to a tensor quantity for the model to process
        The components are assigned according to 'params_dict'

    Args:
        dict_data (dict): Data in dictionary

    Returns:
        torch.Tensor: Tensor data
    """
    tensor_data = torch.ones(len(dict_data))
    for elem in dict_data:
        idx = params_dict[elem]
        val = dict_data[elem]
        # print(f'idx: {idx} \nElements: {val}')
        if idx is not None:
            tensor_data[idx] = val
    return tensor_data


def test():
    
    # Create test data
    data = {
    'loudness': -4.71,
    'danceability': 0.47600000000000003,
    'energy': 0.7809999999999999,
    'key': 0,
    'speechiness': 0.10300000000000001,
    'acousticness': 0.0237,
    'instrumentalness': 0.0,
    'liveness': 0.114,
    'liveness': 0.175,
    'mode': 1
    }
    
    # Change data type from dict to Tensor
    x = (properties_to_data(data)) 
    y = torch.Tensor([8])  # Supposing the song has a rating of 8
    
    # Create a Neural Network
    model = NeuralNetwork(len(data))
    
    # Optimize the model with one piece of data
    optimize(model, [(x,y)])
    
    # save the 'optimized weights'
    save_weights(my_model=model,
        path='/Users/nicolasmendoza/Documents/Programming/JacobsHack/JacobsHack2021/weights.pt')
    
    # Tesy out prediction of model
    print(model(x))
    
    return None

test()