from acquire import acquire
from prepare import prepare, prepare_explore

def wrangle():
    '''
    Returns train, validate, & test encoded ready for modeling
    '''
    train, validate, test = prepare(acquire())
    return train, validate, test

def wrangle_explore():
    '''
    Returns train, validate, & test NOT ENCODED ready for exploration
    '''
    train, validate, test = prepare_explore(acquire())
    return train, validate, test