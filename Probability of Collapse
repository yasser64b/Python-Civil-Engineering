class P_Col(object):
    ''' This function takes the Collapse margin ratio (CMR) and uncertainity standard deviation(uncertainity, Beta)
    and returns the Probabilty of collapse in Percentage ''' 
    def __init__ (self, CMR, beta):
        self.CMR=CMR
        self.beta=beta
    def CollapseP(self):
        import numpy as np 
        from scipy.stats import lognorm
        P=lognorm.cdf((1/self.CMR),self.beta,0)
        return P

A=P_Col(1.2,0.2)
Prob=A.CollapseP()
print('The probability of collapse is %f percent' % (Prob*100)) 
