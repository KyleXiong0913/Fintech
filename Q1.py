import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

class Portfolio:
	u_d = 0;
	delta_d = 0;
	goal_y = 0;
	C = 0;
	Confidence_level = 0;

	def __init__(self, u_d, delta_d, goal_y, C, Confidence_level):
		slef.u_d = u_d
		self.delta_d = delta_d
		self.goal_y = goal_y
		self.C = C
		self.Confidence_level = Confidence_level

	def get_Output(self):
		Z = norm.ppf((1 - self.Confidence_level)/2, loc = 0, scale = 1)
		n = self.goal_y - dt.date.today().year
		delta_c = math.sqrt(math.log(self.delta_d^2/(1+self.u_d)^2+1))
		u_c = math.log(1 + self.u_d) - delta_c^2/2
		delta_TAV = delta_c/(n^0.5)
		return Z, n, u_c, delta_c, delta_TAV;

	def get_DiscreteValue(self, n):
		Z, n, u_c, delta_c, delta_TAV = self.get_Output();
		upperBoundDiscreteValuesArray = math.exp(u_c+Z*delta_TAV)*n
		medianBoundDiscreteValuesArray = math.exp(u_c*n)
		lowerBoundDiscreteValuesArray = math.exp(u_c-Z*delta_TAV)*n
		return upperBoundDiscreteValuesArray, medianBoundDiscreteValuesArray, lowerBoundDiscreteValuesArray

	def get_AdjustedAnnualReturn(self, n):
		upper, median, lower = self.get_DiscreteValue(self, n)
		UpperAdjustedAnnualisedReturn = math.pow(upper,1/n)-1
		MedianAdjustedAnnualisedReturn = math.pow(median,1/n)-1
		LowerAdjustedAnnualisedReturn = math.pow(lower,1/n)-1
		return UpperAdjustedAnnualisedReturn, MedianAdjustedAnnualisedReturn, LowerAdjustedAnnualisedReturn

	def get_ProjectedValue(self, n):
		Upper, Median, Lower = get_AdjustedAnnualReturn(self, n)
		projectedAmtUpperDiscreteValuesArray = scipy.fv(pv-initial_investment, PMT-Annual_Investment/C, n-goal_year*C, Upper/C, PMT Start Period);
		projectedAmtMedianDiscreteValuesArray = scipy.fv(pv-initial_investment, PMT-Annual_Investment);
		projectedAmtLowerDiscreteValuesArra = scipy.fv(pv-initial_investment, PMT-Annual_Investment/C, n-goal_year*C, Lower/C, PMT Start Period);
		return projectedAmtLowerDiscreteValuesArra, projectedAmtMedianDiscreteValuesArray, projectedAmtMedianDiscreteValuesArray