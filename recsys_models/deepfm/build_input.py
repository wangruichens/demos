import  tensorflow as tf
from tensorflow import logging,feature_column

logging.set_verbosity(logging.DEBUG)


categoryFeatureNa = '####'

def min_max_normalizer(min, max):
    def normalizer_fn(x):
        x = tf.clip_by_value(x, min, max)
        return (x - min) / (max - min)
    return normalizer_fn

def create_feature_columns(embed_size):
    linear_feature_columns = []
    embed_feature_columns = []

    u_id = feature_column.categorical_column_with_identity('u_id', 2000000, default_value=0)
    u_id = feature_column.embedding_column(u_id, embed_size)
    linear_feature_columns.append(u_id)
    embed_feature_columns.append(u_id)

    i_id = feature_column.categorical_column_with_identity('i_id', 1000000, default_value=0)
    # i_id = feature_column.embedding_column(i_id, 10)
    i_id = feature_column.embedding_column(i_id, embed_size)
    embed_feature_columns.append(i_id)
    linear_feature_columns.append(i_id)

    i_channel = feature_column.categorical_column_with_vocabulary_list(
        'i_channel',
        vocabulary_list=[
            categoryFeatureNa,
            "bendizhengwu", "caijing", "chongwu", "dongman", "fangchan",
            "guoji", "guonei", "jiaju", "jiankang", "jiaoyu",
            "junshi", "keji", "lishi", "lvyou", "nanchang",
            "qiche", "qinggan", "sannong", "shehui", "shishang",
            "tiyu", "vcaijing", "vgaoxiao", "vpaike", "vshishang",
            "vtiyu", "vyule", "vzixun", "weikandian", "xiaohua",
            "xingzuo", "xinwen", "youxi", "yuer", "yule",
            "ziran"
        ],
        dtype=tf.string,
        default_value=0,
    )
    linear_feature_columns.append(feature_column.indicator_column(i_channel))
    i_channel = feature_column.embedding_column(i_channel, embed_size)
    embed_feature_columns.append(i_channel)

    i_info_exposed_amt = feature_column.numeric_column('i_info_exposed_amt', default_value=0.0)
    i_info_exposed_amt = feature_column.bucketized_column(i_info_exposed_amt,
                                                          [1e-60, 1.0, 11.0, 36.0, 75.0, 132.0, 216.0, 340.0, 516.0,
                                                           746.0, 1064.0, 1680.0, 2487.0, 3656.0, 5138.0, 7837.0,
                                                           11722.0, 18993.0, 117513.0])
    linear_feature_columns.append(feature_column.indicator_column(i_info_exposed_amt))
    i_info_exposed_amt = feature_column.embedding_column(i_info_exposed_amt, embed_size)
    embed_feature_columns.append(i_info_exposed_amt)

    i_info_exposed_amt = feature_column.numeric_column('i_info_exposed_amt', default_value=0.0,
                                                       normalizer_fn=min_max_normalizer(0.0, 117513.00))
    linear_feature_columns.append(i_info_exposed_amt)

    i_info_clicked_amt = feature_column.numeric_column('i_info_clicked_amt', default_value=0.0)
    i_info_clicked_amt = feature_column.bucketized_column(i_info_clicked_amt,
                                                          [1e-60, 1.0, 5.0, 12.0, 23.0, 37.0, 57.0, 96.0, 139.0, 209.0,
                                                           299.0, 442.0, 647.0, 929.0, 1386.0, 1993.0, 3312.0, 17578.0])
    linear_feature_columns.append(feature_column.indicator_column(i_info_clicked_amt))
    i_info_clicked_amt = feature_column.embedding_column(i_info_clicked_amt, embed_size)
    embed_feature_columns.append(i_info_clicked_amt)

    i_info_clicked_amt = feature_column.numeric_column('i_info_clicked_amt', default_value=0.0,
                                                       normalizer_fn=min_max_normalizer(0.0, 17578.00))
    linear_feature_columns.append(i_info_clicked_amt)

    i_info_ctr = feature_column.numeric_column('i_info_ctr', default_value=0.0)
    i_info_ctr = feature_column.bucketized_column(i_info_ctr,
                                                  [1e-60, 0.05272500000000001, 0.098039, 0.122831, 0.139318, 0.154176,
                                                   0.166484, 0.175818, 0.184211, 0.19266100000000003, 0.20089, 0.2098,
                                                   0.218659, 0.227273, 0.236842, 0.25, 0.280294, 1.0])
    linear_feature_columns.append(feature_column.indicator_column(i_info_ctr))
    i_info_ctr = feature_column.embedding_column(i_info_ctr, embed_size)
    embed_feature_columns.append(i_info_ctr)

    i_info_ctr = feature_column.numeric_column('i_info_ctr', default_value=0.0,
                                               normalizer_fn=min_max_normalizer(0.0, 1.00))
    linear_feature_columns.append(i_info_ctr)

    i_cate_exposed_amt = feature_column.numeric_column('i_cate_exposed_amt', default_value=0.0)
    i_cate_exposed_amt = feature_column.bucketized_column(i_cate_exposed_amt,
                                                          [1e-60, 2620264.0, 2893466.0, 4885968.0, 5074062.0, 5648085.0,
                                                           9389498.0, 9900840.0, 10462611.0, 14308882.0, 17151668.0,
                                                           33770813.0])
    linear_feature_columns.append(feature_column.indicator_column(i_cate_exposed_amt))
    i_cate_exposed_amt = feature_column.embedding_column(i_cate_exposed_amt, embed_size)
    embed_feature_columns.append(i_cate_exposed_amt)

    i_cate_exposed_amt = feature_column.numeric_column('i_cate_exposed_amt', default_value=0.0,
                                                       normalizer_fn=min_max_normalizer(0.0, 33770813.00))
    linear_feature_columns.append(i_cate_exposed_amt)

    i_cate_clicked_amt = feature_column.numeric_column('i_cate_clicked_amt', default_value=0.0)
    i_cate_clicked_amt = feature_column.bucketized_column(i_cate_clicked_amt,
                                                          [1e-60, 315824.0, 454217.0, 739206.0, 994371.0, 1072646.0,
                                                           1255534.0, 1546660.0, 1613939.0, 2640503.0, 2841787.0,
                                                           6283496.0])
    linear_feature_columns.append(feature_column.indicator_column(i_cate_clicked_amt))
    i_cate_clicked_amt = feature_column.embedding_column(i_cate_clicked_amt, embed_size)
    embed_feature_columns.append(i_cate_clicked_amt)

    i_cate_clicked_amt = feature_column.numeric_column('i_cate_clicked_amt', default_value=0.0,
                                                       normalizer_fn=min_max_normalizer(0.0, 6283496.00))
    linear_feature_columns.append(i_cate_clicked_amt)

    i_category_ctr = feature_column.numeric_column('i_category_ctr', default_value=0.0)
    i_category_ctr = feature_column.bucketized_column(i_category_ctr,
                                                      [1e-60, 0.11518699999999997, 0.133717, 0.151292, 0.154258,
                                                       0.15621500000000002, 0.162051, 0.165686, 0.184536, 0.186063,
                                                       0.189913, 0.195971])
    linear_feature_columns.append(feature_column.indicator_column(i_category_ctr))
    i_category_ctr = feature_column.embedding_column(i_category_ctr, embed_size)
    embed_feature_columns.append(i_category_ctr)

    i_category_ctr = feature_column.numeric_column('i_category_ctr', default_value=0.0,
                                                   normalizer_fn=min_max_normalizer(0.0, 0.20))
    linear_feature_columns.append(i_category_ctr)

    c_uid_type_ctr_1 = feature_column.numeric_column('c_uid_type_ctr_1', default_value=0.0)
    c_uid_type_ctr_1 = feature_column.bucketized_column(c_uid_type_ctr_1,
                                                        [1e-60, 0.06666699999999999, 0.14285699999999998,
                                                         0.22222199999999998, 0.333333, 0.45, 0.6363640000000002, 1.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_ctr_1))
    c_uid_type_ctr_1 = feature_column.embedding_column(c_uid_type_ctr_1, embed_size)
    embed_feature_columns.append(c_uid_type_ctr_1)

    c_uid_type_ctr_1 = feature_column.numeric_column('c_uid_type_ctr_1', default_value=0.0,
                                                     normalizer_fn=min_max_normalizer(0.0, 1.00))
    linear_feature_columns.append(c_uid_type_ctr_1)

    c_uid_type_clicked_amt_1 = feature_column.numeric_column('c_uid_type_clicked_amt_1', default_value=0.0)
    c_uid_type_clicked_amt_1 = feature_column.bucketized_column(c_uid_type_clicked_amt_1,
                                                                [1e-60, 1.0, 2.0, 3.0, 6.0, 11.0, 351.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_clicked_amt_1))
    c_uid_type_clicked_amt_1 = feature_column.embedding_column(c_uid_type_clicked_amt_1, embed_size)
    embed_feature_columns.append(c_uid_type_clicked_amt_1)

    c_uid_type_clicked_amt_1 = feature_column.numeric_column('c_uid_type_clicked_amt_1', default_value=0.0,
                                                             normalizer_fn=min_max_normalizer(0.0, 351.00))
    linear_feature_columns.append(c_uid_type_clicked_amt_1)

    c_uid_type_exposed_amt_1 = feature_column.numeric_column('c_uid_type_exposed_amt_1', default_value=0.0)
    c_uid_type_exposed_amt_1 = feature_column.bucketized_column(c_uid_type_exposed_amt_1,
                                                                [1e-60, 1.0, 2.0, 3.0, 5.0, 7.0, 9.0, 12.0, 16.0, 23.0,
                                                                 41.0, 988.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_exposed_amt_1))
    c_uid_type_exposed_amt_1 = feature_column.embedding_column(c_uid_type_exposed_amt_1, embed_size)
    embed_feature_columns.append(c_uid_type_exposed_amt_1)

    c_uid_type_exposed_amt_1 = feature_column.numeric_column('c_uid_type_exposed_amt_1', default_value=0.0,
                                                             normalizer_fn=min_max_normalizer(0.0, 988.00))
    linear_feature_columns.append(c_uid_type_exposed_amt_1)

    c_uid_type_ctr_3 = feature_column.numeric_column('c_uid_type_ctr_3', default_value=0.0)
    c_uid_type_ctr_3 = feature_column.bucketized_column(c_uid_type_ctr_3, [1e-60, 0.012820999999999999, 0.058824, 0.1,
                                                                           0.14285699999999998, 0.2, 0.253968, 0.333333,
                                                                           0.4426229999999999, 0.6, 1.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_ctr_3))
    c_uid_type_ctr_3 = feature_column.embedding_column(c_uid_type_ctr_3, embed_size)
    embed_feature_columns.append(c_uid_type_ctr_3)

    c_uid_type_ctr_3 = feature_column.numeric_column('c_uid_type_ctr_3', default_value=0.0,
                                                     normalizer_fn=min_max_normalizer(0.0, 1.00))
    linear_feature_columns.append(c_uid_type_ctr_3)

    c_uid_type_clicked_amt_3 = feature_column.numeric_column('c_uid_type_clicked_amt_3', default_value=0.0)
    c_uid_type_clicked_amt_3 = feature_column.bucketized_column(c_uid_type_clicked_amt_3,
                                                                [1e-60, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 17.0, 30.0,
                                                                 1084.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_clicked_amt_3))
    c_uid_type_clicked_amt_3 = feature_column.embedding_column(c_uid_type_clicked_amt_3, embed_size)
    embed_feature_columns.append(c_uid_type_clicked_amt_3)

    c_uid_type_clicked_amt_3 = feature_column.numeric_column('c_uid_type_clicked_amt_3', default_value=0.0,
                                                             normalizer_fn=min_max_normalizer(0.0, 1084.00))
    linear_feature_columns.append(c_uid_type_clicked_amt_3)

    c_uid_type_exposed_amt_3 = feature_column.numeric_column('c_uid_type_exposed_amt_3', default_value=0.0)
    c_uid_type_exposed_amt_3 = feature_column.bucketized_column(c_uid_type_exposed_amt_3,
                                                                [1e-60, 1.0, 2.0, 4.0, 6.0, 9.0, 13.0, 17.0, 22.0, 28.0,
                                                                 36.0, 48.0, 68.0, 116.0, 2428.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_exposed_amt_3))
    c_uid_type_exposed_amt_3 = feature_column.embedding_column(c_uid_type_exposed_amt_3, embed_size)
    embed_feature_columns.append(c_uid_type_exposed_amt_3)

    c_uid_type_exposed_amt_3 = feature_column.numeric_column('c_uid_type_exposed_amt_3', default_value=0.0,
                                                             normalizer_fn=min_max_normalizer(0.0, 2428.00))
    linear_feature_columns.append(c_uid_type_exposed_amt_3)

    c_uid_type_ctr_7 = feature_column.numeric_column('c_uid_type_ctr_7', default_value=0.0)
    c_uid_type_ctr_7 = feature_column.bucketized_column(c_uid_type_ctr_7,
                                                        [1e-60, 0.033898000000000005, 0.061224, 0.090909, 0.124444,
                                                         0.162162, 0.208333, 0.266667, 0.333333, 0.433333, 0.575342,
                                                         1.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_ctr_7))
    c_uid_type_ctr_7 = feature_column.embedding_column(c_uid_type_ctr_7, embed_size)
    embed_feature_columns.append(c_uid_type_ctr_7)

    c_uid_type_ctr_7 = feature_column.numeric_column('c_uid_type_ctr_7', default_value=0.0,
                                                     normalizer_fn=min_max_normalizer(0.0, 1.00))
    linear_feature_columns.append(c_uid_type_ctr_7)

    c_uid_type_clicked_amt_7 = feature_column.numeric_column('c_uid_type_clicked_amt_7', default_value=0.0)
    c_uid_type_clicked_amt_7 = feature_column.bucketized_column(c_uid_type_clicked_amt_7,
                                                                [1e-60, 1.0, 2.0, 3.0, 5.0, 7.0, 11.0, 16.0, 24.0, 37.0,
                                                                 67.0, 1613.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_clicked_amt_7))
    c_uid_type_clicked_amt_7 = feature_column.embedding_column(c_uid_type_clicked_amt_7, embed_size)
    embed_feature_columns.append(c_uid_type_clicked_amt_7)

    c_uid_type_clicked_amt_7 = feature_column.numeric_column('c_uid_type_clicked_amt_7', default_value=0.0,
                                                             normalizer_fn=min_max_normalizer(0.0, 1613.00))
    linear_feature_columns.append(c_uid_type_clicked_amt_7)

    c_uid_type_exposed_amt_7 = feature_column.numeric_column('c_uid_type_exposed_amt_7', default_value=0.0)
    c_uid_type_exposed_amt_7 = feature_column.bucketized_column(c_uid_type_exposed_amt_7,
                                                                [1e-60, 2.0, 4.0, 7.0, 11.0, 16.0, 22.0, 30.0, 40.0,
                                                                 51.0, 65.0, 84.0, 110.0, 153.0, 256.0, 6136.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_exposed_amt_7))
    c_uid_type_exposed_amt_7 = feature_column.embedding_column(c_uid_type_exposed_amt_7, embed_size)
    embed_feature_columns.append(c_uid_type_exposed_amt_7)

    c_uid_type_exposed_amt_7 = feature_column.numeric_column('c_uid_type_exposed_amt_7', default_value=0.0,
                                                             normalizer_fn=min_max_normalizer(0.0, 6136.00))
    linear_feature_columns.append(c_uid_type_exposed_amt_7)

    c_uid_type_ctr_14 = feature_column.numeric_column('c_uid_type_ctr_14', default_value=0.0)
    c_uid_type_ctr_14 = feature_column.bucketized_column(c_uid_type_ctr_14,
                                                         [1e-60, 0.028777, 0.051282000000000015, 0.074205, 0.1,
                                                          0.130841, 0.166667, 0.212121, 0.266667, 0.333333, 0.425,
                                                          0.563265, 1.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_ctr_14))
    c_uid_type_ctr_14 = feature_column.embedding_column(c_uid_type_ctr_14, embed_size)
    embed_feature_columns.append(c_uid_type_ctr_14)

    c_uid_type_ctr_14 = feature_column.numeric_column('c_uid_type_ctr_14', default_value=0.0,
                                                      normalizer_fn=min_max_normalizer(0.0, 1.00))
    linear_feature_columns.append(c_uid_type_ctr_14)

    c_uid_type_clicked_amt_14 = feature_column.numeric_column('c_uid_type_clicked_amt_14', default_value=0.0)
    c_uid_type_clicked_amt_14 = feature_column.bucketized_column(c_uid_type_clicked_amt_14,
                                                                 [1e-60, 1.0, 2.0, 4.0, 6.0, 9.0, 14.0, 20.0, 31.0,
                                                                  47.0, 74.0, 134.0, 3407.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_clicked_amt_14))
    c_uid_type_clicked_amt_14 = feature_column.embedding_column(c_uid_type_clicked_amt_14, embed_size)
    embed_feature_columns.append(c_uid_type_clicked_amt_14)

    c_uid_type_clicked_amt_14 = feature_column.numeric_column('c_uid_type_clicked_amt_14', default_value=0.0,
                                                              normalizer_fn=min_max_normalizer(0.0, 3407.00))
    linear_feature_columns.append(c_uid_type_clicked_amt_14)

    c_uid_type_exposed_amt_14 = feature_column.numeric_column('c_uid_type_exposed_amt_14', default_value=0.0)
    c_uid_type_exposed_amt_14 = feature_column.bucketized_column(c_uid_type_exposed_amt_14,
                                                                 [1e-60, 1.0, 3.0, 7.0, 13.0, 20.0, 29.0, 42.0, 58.0,
                                                                  77.0, 100.0, 129.0, 167.0, 221.0, 308.0, 507.0,
                                                                  14466.0])
    linear_feature_columns.append(feature_column.indicator_column(c_uid_type_exposed_amt_14))
    c_uid_type_exposed_amt_14 = feature_column.embedding_column(c_uid_type_exposed_amt_14, embed_size)
    embed_feature_columns.append(c_uid_type_exposed_amt_14)

    c_uid_type_exposed_amt_14 = feature_column.numeric_column('c_uid_type_exposed_amt_14', default_value=0.0,
                                                              normalizer_fn=min_max_normalizer(0.0, 14466.00))
    linear_feature_columns.append(c_uid_type_exposed_amt_14)

    c_user_flavor = feature_column.numeric_column('c_user_flavor', default_value=0.0)
    c_user_flavor = feature_column.bucketized_column(c_user_flavor,
                                                     [1e-60, 0.0012, 0.0493, 0.0881, 0.1233, 0.1573, 0.1933, 0.2323,
                                                      0.2777, 0.3366, 0.4182, 0.5487, 0.8213, 4.7547])
    linear_feature_columns.append(feature_column.indicator_column(c_user_flavor))
    c_user_flavor = feature_column.embedding_column(c_user_flavor, embed_size)
    embed_feature_columns.append(c_user_flavor)

    c_user_flavor = feature_column.numeric_column('c_user_flavor', default_value=0.0,
                                                  normalizer_fn=min_max_normalizer(0.0, 4.75))
    linear_feature_columns.append(c_user_flavor)

    u_activetime_at1 = feature_column.numeric_column('u_activetime_at1', default_value=0.0)
    u_activetime_at1 = feature_column.bucketized_column(u_activetime_at1, [1e-60, 1.0, 2.0, 3.0, 6.0, 10.0, 8764.0])
    linear_feature_columns.append(feature_column.indicator_column(u_activetime_at1))
    u_activetime_at1 = feature_column.embedding_column(u_activetime_at1, embed_size)
    embed_feature_columns.append(u_activetime_at1)

    u_activetime_at1 = feature_column.numeric_column('u_activetime_at1', default_value=0.0,
                                                     normalizer_fn=min_max_normalizer(0.0, 8764.00))
    linear_feature_columns.append(u_activetime_at1)

    u_activetime_at2 = feature_column.numeric_column('u_activetime_at2', default_value=0.0)
    u_activetime_at2 = feature_column.bucketized_column(u_activetime_at2, [1e-60, 1.0, 3.0, 5.0, 8.0, 7849.0])
    linear_feature_columns.append(feature_column.indicator_column(u_activetime_at2))
    u_activetime_at2 = feature_column.embedding_column(u_activetime_at2, embed_size)
    embed_feature_columns.append(u_activetime_at2)

    u_activetime_at2 = feature_column.numeric_column('u_activetime_at2', default_value=0.0,
                                                     normalizer_fn=min_max_normalizer(0.0, 7849.00))
    linear_feature_columns.append(u_activetime_at2)

    u_activetime_at3 = feature_column.numeric_column('u_activetime_at3', default_value=0.0)
    u_activetime_at3 = feature_column.bucketized_column(u_activetime_at3, [1e-60, 1.0, 2.0, 3.0, 5.0, 4075.0])
    linear_feature_columns.append(feature_column.indicator_column(u_activetime_at3))
    u_activetime_at3 = feature_column.embedding_column(u_activetime_at3, embed_size)
    embed_feature_columns.append(u_activetime_at3)

    u_activetime_at3 = feature_column.numeric_column('u_activetime_at3', default_value=0.0,
                                                     normalizer_fn=min_max_normalizer(0.0, 4075.00))
    linear_feature_columns.append(u_activetime_at3)

    u_activetime_at4 = feature_column.numeric_column('u_activetime_at4', default_value=0.0)
    u_activetime_at4 = feature_column.bucketized_column(u_activetime_at4, [1e-60, 1.0, 2.0, 3.0, 5.0, 9.0, 10641.0])
    linear_feature_columns.append(feature_column.indicator_column(u_activetime_at4))
    u_activetime_at4 = feature_column.embedding_column(u_activetime_at4, embed_size)
    embed_feature_columns.append(u_activetime_at4)

    u_activetime_at4 = feature_column.numeric_column('u_activetime_at4', default_value=0.0,
                                                     normalizer_fn=min_max_normalizer(0.0, 10641.00))
    linear_feature_columns.append(u_activetime_at4)

    u_activetime_at5 = feature_column.numeric_column('u_activetime_at5', default_value=0.0)
    u_activetime_at5 = feature_column.bucketized_column(u_activetime_at5,
                                                        [1e-60, 1.0, 3.0, 6.0, 10.0, 17.0, 22105.0])
    linear_feature_columns.append(feature_column.indicator_column(u_activetime_at5))
    u_activetime_at5 = feature_column.embedding_column(u_activetime_at5, embed_size)
    embed_feature_columns.append(u_activetime_at5)

    u_activetime_at5 = feature_column.numeric_column('u_activetime_at5', default_value=0.0,
                                                     normalizer_fn=min_max_normalizer(0.0, 22105.00))
    linear_feature_columns.append(u_activetime_at5)

    i_mini_img_size = feature_column.numeric_column('i_mini_img_size', default_value=0.0)
    i_mini_img_size = feature_column.bucketized_column(i_mini_img_size, [1e-60, 2.0, 3.0, 5.0])
    linear_feature_columns.append(feature_column.indicator_column(i_mini_img_size))
    i_mini_img_size = feature_column.embedding_column(i_mini_img_size, embed_size)
    embed_feature_columns.append(i_mini_img_size)

    i_mini_img_size = feature_column.numeric_column('i_mini_img_size', default_value=0.0,
                                                    normalizer_fn=min_max_normalizer(0.0, 5.00))
    linear_feature_columns.append(i_mini_img_size)

    i_comment_count = feature_column.numeric_column('i_comment_count', default_value=0.0)
    i_comment_count = feature_column.bucketized_column(i_comment_count,
                                                       [1e-60, 1.0, 2.0, 3.0, 6.0, 13.0, 26.0, 64.0, 33236.0])
    linear_feature_columns.append(feature_column.indicator_column(i_comment_count))
    i_comment_count = feature_column.embedding_column(i_comment_count, embed_size)
    embed_feature_columns.append(i_comment_count)

    i_comment_count = feature_column.numeric_column('i_comment_count', default_value=0.0,
                                                    normalizer_fn=min_max_normalizer(0.0, 33236.00))
    linear_feature_columns.append(i_comment_count)

    u_brand = feature_column.categorical_column_with_vocabulary_list('u_brand',
                                                                     ['####', 'OPPO', 'HUAWEI', 'XIAOMI', 'VIVO',
                                                                      'HONOR', 'MEIZU', 'SAMSUNG', '360', 'GIONEE',
                                                                      'LEECO', 'NUBIA', 'SMARTISAN', 'LENOVO', 'ZTE',
                                                                      'COOLPAD', 'ONEPLUS', 'VOTO', '4G+', 'VIVI'],
                                                                     dtype=tf.string, default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(u_brand))
    u_brand = feature_column.embedding_column(u_brand, embed_size)
    embed_feature_columns.append(u_brand)

    u_operator = feature_column.categorical_column_with_vocabulary_list('u_operator', ['####', 'CM', 'CT', 'CU'],
                                                                        dtype=tf.string, default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(u_operator))
    u_operator = feature_column.embedding_column(u_operator, embed_size)
    embed_feature_columns.append(u_operator)

    u_age = feature_column.categorical_column_with_vocabulary_list('u_age',
                                                                   ['####', 'MID-AGE', 'UNKNOWN', 'YOUNG', 'ELDER',
                                                                    'YOUNGSTER', 'TEENAGE'], dtype=tf.string,
                                                                   default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(u_age))
    u_age = feature_column.embedding_column(u_age, embed_size)
    embed_feature_columns.append(u_age)

    u_marriage = feature_column.categorical_column_with_vocabulary_list('u_marriage',
                                                                        ['####', 'UNKNOWN', 'MARRIED', 'UNMARRIED'],
                                                                        dtype=tf.string, default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(u_marriage))
    u_marriage = feature_column.embedding_column(u_marriage, embed_size)
    embed_feature_columns.append(u_marriage)

    u_sex = feature_column.categorical_column_with_vocabulary_list('u_sex', ['####', 'MAN', 'WOMAN', 'UNKNOWN'],
                                                                   dtype=tf.string, default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(u_sex))
    u_sex = feature_column.embedding_column(u_sex, embed_size)
    embed_feature_columns.append(u_sex)

    u_sex_age = feature_column.categorical_column_with_vocabulary_list('u_sex_age',
                                                                       ['####', 'MAN_MID-AGE', 'MAN_UNKNOWN',
                                                                        'WOMAN_MID-AGE', 'MAN_YOUNG', 'WOMAN_YOUNG',
                                                                        'WOMAN_UNKNOWN', 'UNKNOWN_UNKNOWN', 'MAN_ELDER',
                                                                        'WOMAN_YOUNGSTER', 'MAN_YOUNGSTER',
                                                                        'WOMAN_ELDER', 'MAN_TEENAGE', 'WOMAN_TEENAGE',
                                                                        'UNKNOWN_MID-AGE', 'UNKNOWN_YOUNG',
                                                                        'UNKNOWN_YOUNGSTER'], dtype=tf.string,
                                                                       default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(u_sex_age))
    u_sex_age = feature_column.embedding_column(u_sex_age, embed_size)
    embed_feature_columns.append(u_sex_age)

    u_sex_marriage = feature_column.categorical_column_with_vocabulary_list('u_sex_marriage',
                                                                            ['####', 'MAN_UNKNOWN', 'WOMAN_UNKNOWN',
                                                                             'MAN_UNMARRIED', 'MAN_MARRIED',
                                                                             'WOMAN_MARRIED', 'UNKNOWN_UNKNOWN',
                                                                             'WOMAN_UNMARRIED'], dtype=tf.string,
                                                                            default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(u_sex_marriage))
    u_sex_marriage = feature_column.embedding_column(u_sex_marriage, embed_size)
    embed_feature_columns.append(u_sex_marriage)

    u_age_marriage = feature_column.categorical_column_with_vocabulary_list('u_age_marriage',
                                                                            ['####', 'MID-AGE_UNKNOWN',
                                                                             'UNKNOWN_UNKNOWN', 'YOUNG_UNKNOWN',
                                                                             'MID-AGE_MARRIED', 'YOUNG_MARRIED',
                                                                             'UNKNOWN_UNMARRIED', 'ELDER_UNKNOWN',
                                                                             'MID-AGE_UNMARRIED', 'YOUNG_UNMARRIED',
                                                                             'YOUNGSTER_UNKNOWN', 'TEENAGE_UNKNOWN',
                                                                             'ELDER_MARRIED', 'YOUNGSTER_MARRIED',
                                                                             'YOUNGSTER_UNMARRIED', 'TEENAGE_UNMARRIED',
                                                                             'ELDER_UNMARRIED', 'TEENAGE_MARRIED',
                                                                             'UNKNOWN_MARRIED'], dtype=tf.string,
                                                                            default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(u_age_marriage))
    u_age_marriage = feature_column.embedding_column(u_age_marriage, embed_size)
    embed_feature_columns.append(u_age_marriage)

    u_activelevel = feature_column.categorical_column_with_vocabulary_list('u_activelevel',
                                                                           ['####', 'c1', 'c2', 'c0', 'c3'],
                                                                           dtype=tf.string, default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(u_activelevel))
    u_activelevel = feature_column.embedding_column(u_activelevel, embed_size)
    embed_feature_columns.append(u_activelevel)

    i_hot_news = feature_column.categorical_column_with_vocabulary_list('i_hot_news', ['####', 'c0', 'c1'],
                                                                        dtype=tf.string, default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(i_hot_news))
    i_hot_news = feature_column.embedding_column(i_hot_news, embed_size)
    embed_feature_columns.append(i_hot_news)

    i_is_recommend = feature_column.categorical_column_with_vocabulary_list('i_is_recommend', ['####', 'c0', 'c1'],
                                                                            dtype=tf.string, default_value=0)
    linear_feature_columns.append(feature_column.indicator_column(i_is_recommend))
    i_is_recommend = feature_column.embedding_column(i_is_recommend, embed_size)
    embed_feature_columns.append(i_is_recommend)

    return linear_feature_columns, embed_feature_columns


feature_description = {
    'label': tf.FixedLenFeature((), tf.int64),

    "u_id": tf.FixedLenFeature(dtype=tf.int64, shape=(1)),
    "i_id": tf.FixedLenFeature(dtype=tf.int64, shape=(1)),

    "i_channel": tf.FixedLenFeature(dtype=tf.string, shape=(1)),

    "u_brand": tf.FixedLenFeature(dtype=tf.string, shape=(1)),
    "u_operator": tf.FixedLenFeature(dtype=tf.string, shape=(1)),
    "u_activelevel": tf.FixedLenFeature(dtype=tf.string, shape=(1)),

    "u_age": tf.FixedLenFeature(dtype=tf.string, shape=(1)),
    "u_marriage": tf.FixedLenFeature(dtype=tf.string, shape=(1)),
    "u_sex": tf.FixedLenFeature(dtype=tf.string, shape=(1),),
    "u_sex_age": tf.FixedLenFeature(dtype=tf.string, shape=(1)),
    "u_sex_marriage": tf.FixedLenFeature(dtype=tf.string, shape=(1)),
    "u_age_marriage": tf.FixedLenFeature(dtype=tf.string, shape=(1)),

    "i_hot_news": tf.FixedLenFeature(dtype=tf.string, shape=(1)),
    "i_is_recommend": tf.FixedLenFeature(dtype=tf.string, shape=(1)),

    "i_info_exposed_amt": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "i_info_clicked_amt": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "i_info_ctr": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),

    "i_cate_exposed_amt": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "i_cate_clicked_amt": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "i_category_ctr": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),

    "c_uid_type_ctr_1": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_clicked_amt_1": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_exposed_amt_1": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_ctr_3": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_clicked_amt_3": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_exposed_amt_3": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_ctr_7": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_clicked_amt_7": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_exposed_amt_7": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_ctr_14": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_clicked_amt_14": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "c_uid_type_exposed_amt_14": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),

    "c_user_flavor": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),

    "u_activetime_at1": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "u_activetime_at2": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "u_activetime_at3": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "u_activetime_at4": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "u_activetime_at5": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),

    "i_mini_img_size": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
    "i_comment_count": tf.FixedLenFeature(dtype=tf.float32, shape=(1)),
}

def parse_exmp(serial_exmp):
    features = tf.parse_single_example(serial_exmp, features=feature_description)
    labels = features.pop('label')
    return features, labels