from api.apiFactory import ApiFactory

# print(f"轮播图：{ApiFactory.get_home_api().banner_api().json()}")
# #
# # print(f"专题栏：{ApiFactory.get_home_api().theme_api().json()}")
# #
# # print(f"最近新品：{ApiFactory.get_home_api().recent_product_api().json()}")

# print(f"商品分类：{ApiFactory.get_product_api().product_api().json()}")
# print(f'分类下商品：{ApiFactory.get_product_api().classify_product_api(3).json()}')
# print(f'商品信息：{ApiFactory.get_product_api().detail_product_api(5).json()}')

print(f'token：{ApiFactory.get_user_api().get_token_api().json()}')
