import numpy as np
import pandas as pd
import statsmodels.api as sm


churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']
factor_cut = pd.cut(churn.total_charges, 5, precision=2)

dependent_variable = churn['churn01']
independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()


def inverse_logit(model_formula):
    from math import exp
    return (1.0 / (1.0 + exp(-model_formula))) * 100.0


at_means = float(logit_model.params[0]) + \
           float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
           float(logit_model.params[2]) * float(churn['custserv_calls'].mean()) + \
           float(logit_model.params[3]) * float(churn['total_charges'].mean())

cust_serv_mean = float(logit_model.params[0]) + \
                 float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
                 float(logit_model.params[2]) * float(churn['custserv_calls'].mean()) + \
                 float(logit_model.params[3]) * float(churn['total_charges'].mean())

cust_serv_mean_minus_one = float(logit_model.params[0]) + \
                           float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
                           float(logit_model.params[2]) * float(churn['custserv_calls'].mean() - 1.0) + \
                           float(logit_model.params[3]) * float(churn['total_charges'].mean())

new_observations = churn.ix[churn.index.isin(range(10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)

"""
Optimization terminated successfully.
         Current function value: 0.363480
         Iterations 7
[0.25, 0.09, 0.08, 0.2, 0.12, 0.1, 0.49, 0.03, 0.22, 0.24]
"""