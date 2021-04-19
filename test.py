# import requests
#
# url = "https://deepmemo.a-bank.com.ua/prolog/conveyor/v0.2/siem_ccstat/siem_ccstat_search_all"
#
# responsesss = requests.post(url, json={'ekb_id':'1800847610','card':''})
# ccstat = responsesss.json()
# ccstat = ccstat["body"]["ccstat"][0]
#
#
# def cycleccstat(Mass):
#     New_mass = []
#     for keys1 in Mass:
#         params = keys1['ccstat']
#         New_mass.append(params)
#     return New_mass
#
# def Convertobj(Mass):
#     paramters = cycleccstat(Mass)
#     return paramters
# a = Convertobj(ccstat)
# # print(a)
# # for i in a:
# #     print(i)
# # print(a)
# #
# # asv = []
# # for keys1 in ccstat:
# #     param =  keys1['ccstat']
# #     asv.append(param)
# #     # print(param[0]['id'])
# # for i in asv:
# #     print(i)
# #     for j in i:
# #         print(j)
#
# # print(asv)
#     # for i in range(ccstat[param]):
#     #     print(i)
#     #     for keys in range(len(ccstat[keys1][i])):
#     #         asv.append(ccstat[keys1][i][keys])
# # print(asv)
