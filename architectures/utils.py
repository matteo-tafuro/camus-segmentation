from .unet import UNet
from .anamnet import AnamNet
from .lvnet import LVNet

def get_model(model, **kwargs):
    """
    Function to get the model. `model` must be either 'unet', 'laddernet', 'enet', 'segnet', 'lednet', 'anamnet', or 'lvnet'.
    Inputs:
        model - String, name of the model
        kwargs - Keyword arguments for the model
    Outputs:
        model - PyTorch model
    """

    assert model.lower() in ["unet", "anamnet", "lvnet"], "Model must be either 'unet', ..."
    
    if model == "unet":
        return UNet(n_channels=1, n_classes=4, scaling=2, **kwargs)
    elif model == "laddernet":
        pass #TBA
    elif model == "enet":
        pass #TBA
    elif model == "segnet":
        pass #TBA
    elif model == "lednet":
        pass #TBA
    elif model == "anamnet":
        return AnamNet()
    elif model == "lvnet":
        return LVNet()
    else:
        raise NotImplementedError("Model not implemented.")
    