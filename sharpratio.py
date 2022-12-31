import numpy as np

def calc_sharpe_ratio(returns, risk_free_rate):
  """
  Calculates the Sharpe ratio of an investment.
  
  Parameters:
  returns (numpy array): the returns of the investment
  risk_free_rate (float): the risk-free rate of return
  
  Returns:
  float: the Sharpe ratio of the investment
  """
  # Calculate the excess returns over the risk-free rate
  excess_returns = returns - risk_free_rate
  
  # Calculate the standard deviation of the excess returns
  std_excess_returns = np.std(excess_returns)
  
  # Calculate the Sharpe ratio
  sharpe_ratio = np.mean(excess_returns) / std_excess_returns
  
  return sharpe_ratio

# Example usage
returns = np.array([0.1, 0.2, 0.15, 0.3, 0.25])
risk_free_rate = 0.05
sharpe_ratio = calc_sharpe_ratio(returns, risk_free_rate)
print(f"The Sharpe ratio of the investment is {sharpe_ratio:.2f}")
