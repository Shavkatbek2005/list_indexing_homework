def main(l):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    l[1]=True
    l[0]=False
    return l
print(main([1,2,3,44,5,55]))