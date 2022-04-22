import FinanceDataReader as fdr
beforewar = fdr.DataReader('271060', '2020-11-01', '2021-03-31')
beforewar
## csv 파일로 저장
beforewar.to_csv('./beforewar.csv')


import FinanceDataReader as fdr
afterwar = fdr.DataReader('271060', '2021-11-01', '2022-03-31')
afterwar
## csv 파일로 저장
afterwar.to_csv('./afterwar.csv')




