import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    nplist = np.array(list)
    nplist = np.reshape(list, (3, 3))
    calculations = dict.fromkeys(["mean", "variance", "standard deviation", "max", "min", "sum"])
    means = [np.mean(nplist, axis=0).tolist(), np.mean(nplist, axis=1).tolist(), np.mean(np.reshape(nplist, (1, -1)).squeeze())]

    variances = [np.var(nplist, axis=0).tolist(), np.var(nplist, axis=1).tolist(), np.var(np.reshape(nplist, (1, -1)).squeeze())]

    stds = [np.std(nplist, axis=0).tolist(), np.std(nplist, axis=1).tolist(), np.std(np.reshape(nplist, (1, -1)).squeeze())]

    maxs = [np.max(nplist, axis=0).tolist(), np.max(nplist, axis=1).tolist(), np.max(np.reshape(nplist, (1, -1)).squeeze())]

    mins = [np.min(nplist, axis=0).tolist(), np.min(nplist, axis=1).tolist(), np.min(np.reshape(nplist, (1, -1)).squeeze())]

    sums = [np.sum(nplist, axis=0).tolist(), np.sum(nplist, axis=1).tolist(), np.sum(np.reshape(nplist, (1, -1)).squeeze())]

    calculations["mean"] = means
    calculations["variance"] = variances
    calculations["standard deviation"] = stds
    calculations["max"] = maxs
    calculations["min"] = mins
    calculations["sum"] = sums

    return calculations
