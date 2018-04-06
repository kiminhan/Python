import numpy as np
import pandas as pd
import statsmodels.api as sm

churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']

# print(churn['churn01'])
#
dependent_variable = churn['churn01']

independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()
print(logit_model)
# print("\nQuantities you can extract from the result:\n%s" % dir(logit_model))
# print("\nCoefficients:\n%s" % logit_model.params)
# print("\nCoefficient Std Errors:\n%s" % logit_model.bse)
#
# """
# Optimization terminated successfully.
#          Current function value: 0.363480
#          Iterations 7
#                            Logit Regression Results
# ==============================================================================
# Dep. Variable:                churn01   No. Observations:                 3333
# Model:                          Logit   Df Residuals:                     3329
# Method:                           MLE   Df Model:                            3
# Date:                Thu, 08 Mar 2018   Pseudo R-squ.:                  0.1216
# Time:                        09:46:20   Log-Likelihood:                -1211.5
# converged:                       True   LL-Null:                       -1379.1
#                                         LLR p-value:                 2.234e-72
# ==================================================================================
#                      coef    std err          z      P>|z|      [0.025      0.975]
# ----------------------------------------------------------------------------------
# const             -7.2205      0.394    -18.309      0.000      -7.993      -6.448
# account_length     0.0012      0.001      0.927      0.354      -0.001       0.004
# custserv_calls     0.4443      0.037     12.129      0.000       0.373       0.516
# total_charges      0.0729      0.005     13.448      0.000       0.062       0.084
# ==================================================================================
#
# Quantities you can extract from the result:
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cache', '_data_attr', '_get_endog_name', '_get_robustcov_results', 'aic', 'bic', 'bse', 'conf_int', 'cov_kwds', 'cov_params', 'cov_type', 'df_model', 'df_resid', 'f_test', 'fittedvalues', 'get_margeff', 'initialize', 'k_constant', 'llf', 'llnull', 'llr', 'llr_pvalue', 'load', 'mle_retvals', 'mle_settings', 'model', 'nobs', 'normalized_cov_params', 'params', 'pred_table', 'predict', 'prsquared', 'pvalues', 'remove_data', 'resid_dev', 'resid_generalized', 'resid_pearson', 'resid_response', 'save', 'scale', 'summary', 'summary2', 't_test', 'tvalues', 'use_t', 'wald_test', 'wald_test_terms']
#
# Coefficients:
# const            -7.220520
# account_length    0.001222
# custserv_calls    0.444323
# total_charges     0.072914
# dtype: float64
#
# Coefficient Std Errors:
# const             0.394363
# account_length    0.001317
# custserv_calls    0.036633
# total_charges     0.005422
# dtype: float64
# """