from keterpencilan.dijkstra import *

def test_shortest_path_with_empty_node(): #Test
        DK = []
        graf ={}
        kamus_1 = {}
        kamus_2 = {}
        kota_awal = None
        expected = None
        current = shortest_path(graf,kota_awal,DK,kamus_1,kamus_2)
        assert  expected == current

def test_shortest_path_with_a_node(): #Test
        DK = ['Yakarta']
        graf ={}
        kamus_1 = {'Yakarta':0}
        kamus_2 = {0:'Yakarta'}
        kota_awal = 'Yakarta'
        expected = None
        current = shortest_path(graf,kota_awal,DK,kamus_1,kamus_2)
        assert  expected == current

def test_calculate_keterpencilan(): #Test
    graf = {'Yakarta': [['Yenpasar', 4], ['Yontianak', 1]], 
            'Yenpasar': [['Yakarta', 4], ['Yontianak', 2], ['Yurabaya', 7]], 
            'Yontianak': [['Yakarta', 1], ['Yenpasar', 2], ['Yurabaya', 3]], 
            'Yurabaya': [['Yenpasar', 7], ['Yontianak', 3], ['Yakassar', 9]], 
            'Yakassar': [['Yurabaya', 9]]}
    DK = ['Yakarta', 'Yontianak', 'Yenpasar', 'Yurabaya', 'Yakassar']
    kamus_1 = {'Yakarta': 0, 'Yontianak': 1, 'Yenpasar': 2, 'Yurabaya': 3, 'Yakassar': 4}
    kamus_2 = {0: 'Yakarta', 1: 'Yontianak', 2: 'Yenpasar', 3: 'Yurabaya', 4: 'Yakassar'}
    expected = [[9, 'Yurabaya'], [12, 'Yontianak'], [13, 'Yakarta'], [14, 'Yakassar'], [14, 'Yenpasar']]
    current = calculate_keterpencilan(graf,DK,kamus_1,kamus_2)
    assert  expected == current
