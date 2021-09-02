# Sub Project - 1

[TOC]

- pandas
- matplotlib
- seaborn
- folium

데이터 처리 관련 기술을 경험해 보는 서브 프로젝트

## 3-5. 음식점의 위치 분포를 지도에 나타내기

- folium 라이브러리를 사용합니다.
- GeoJson format으로 point를 Map 객체에 추가합니다.

```
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}
```

### df_to_geojson

- DataFrame 데이터를 geojson 포맷에 맞도록 변경하는 함수

```python
def df_to_geojson(df):
    geojson = {'type': 'FeatureCollection', 'features': []}

    for _, row in df.iterrows():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": []},
            "properties": {}
        }
        feature['geometry']['coordinates'] = [row['longitude'], row['latitude']]
        feature['properties']['tel'] = row['tel']
        feature['properties']['address'] = row['address']
        feature['properties']['area'] = row['area']

        geojson['features'].append(feature)
    return geojson
```

### show_stores_distribution_graph

- 진행 과정에 따라 조금씩 달라질 예정입니다.

```python
def show_stores_distribution_graph(dataframes):
    """
    Req. 1-3-5 각 음식점의 위치 분포를 지도에 나타냅니다.
    """
    df = dataframes["stores"]
    # 리뷰가 10개 이상 달린
    df = df[df['review_cnt'] > 10]
    m = folium.Map(
        location=[35.8, 127.6], tiles="OpenStreetMap", zoom_start=8
    )
    geo_json = df_to_geojson(df)
    folium.GeoJson(geo_json, name="geojson").add_to(m)

    # 스크롤 기능
    plugins.MousePosition().add_to(m)
    # 전체화면 기능
    plugins.Fullscreen(
        position='topright',
        title='확장하기',
        title_cancel='나가기',
        force_separate_button=True
    ).add_to(m)

    m.save('map.html')
```

### 진행과정

- 단순하게 point만 찍은 Map

```python
# 리뷰가 10개 이상 달린
    df = df[df['review_cnt'] > 10]
```

![image-20210901173002577](README.assets/image-20210901173002577.png)

## 4-1 유저와 음식점을 축으로 하고 평점을 값으로 갖는 행렬 저장

- Sparse
- 희소 행렬보다 더 메모리 효율이 좋은 CSR Matrix로 저장

`scipy.sparse.csr_matrix()` 를 써서 df를 Compressed Sparse Numpy Matrix로 바꾸는 작업

- 데이터 재구조화 (reshaping)
- data.pivot(index, columns, values)
- pd.pivot_table(data, index, columns, values, aggfunc)

기존의 데이터를 sparse matrix 에서 Compressed sparce array로 바꿔주기

### pivot_table의 NaN, 결측값 제거

```python
pivot_table = merge.pivot_table(index='user', columns='store', values='score', aggfunc=np.mean, fill_value=0)
print(pivot_table)

pivot_table2 = merge.pivot_table(index='user', columns='store', values='score', aggfunc=np.mean)
print(pivot_table2)

pitov_sparse = pivot_table2.astype(pd.SparseDtype('int', np.nan))
print(pitov_sparse)
```

![image-20210902120636191](../../2_최준원/sub1/sparse.assets/image-20210902120636191.png)

fill_value=0 또는 fillna(0)의 경우에만 제대로 결측값 변경에 성공한다.

https://rfriend.tistory.com/551
