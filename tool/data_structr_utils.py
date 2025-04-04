"""
@date: 2024/8/2
@author: tangle
"""
from collections.abc import Mapping


def update_nested_dicts(base_dict, update_dict):
    """
    Help function to avoid deleting keys that did not change in the update_dict
    @return The updated base dictionary
    """
    for key, value in update_dict.items():
        if isinstance(value, Mapping):
            base_dict[key] = update_nested_dicts(base_dict.get(key, {}), value)
        else:
            base_dict[key] = value
    return base_dict


if __name__ == '__main__':
    UNSUPPORTED = {'size': 0,
                   'pit': 0}
    import copy
    b = {
        'ns_fopt': {'LBAF4': copy.deepcopy(UNSUPPORTED)},
        'ns_opt': {
            'LBAF1': {
                'size': 4096,
                'pit': 0},
            'LBAF2': copy.deepcopy(UNSUPPORTED),  # must use copy to avoid error
            'LBAF3': copy.deepcopy(UNSUPPORTED),
        }
    }
    u = {'ns_opt': {
        'LBAF2': {'size': 4096,
                  'pit': 2},
        'LBAF3': {'size': 4096,
                  'pit': 1},
    }
    }
    b = update_nested_dicts(b, u)
    print(b)
