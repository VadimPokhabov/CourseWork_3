from src.utils import filter_list_only_executed, modify_date, mask_card_number, mask_amount_number, sort_date_operations


def test_sort_date_operations():
    assert sort_date_operations(
        [{"date": "2018-03-23T10:45:06.972075"},
         {"date": "2019-04-04T23:20:05.206878"},
         {"date": "2019-03-23T01:09:46.296404"},
         {"date": "2018-12-20T16:43:26.929246"},
         {"date": "2019-07-12T20:41:47.882230"}]) == [{"date": "2019-07-12T20:41:47.882230"},
                                                      {"date": "2019-04-04T23:20:05.206878"},
                                                      {"date": "2019-03-23T01:09:46.296404"},
                                                      {"date": "2018-12-20T16:43:26.929246"},
                                                      {"date": "2018-03-23T10:45:06.972075"}]


def test_modify_date():
    """Тест функции modify_date"""
    assert modify_date([{"date": "2018-03-23T10:45:06.972075"}]) == ['23.03.2018']


def test_is_ex_operations():
    """Тест функции is_ex_operations"""
    test_list = [{"state": "EXEC", "date": "2019-07-03T18:35:29.512364"},
                 {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]
    assert filter_list_only_executed(test_list) == [
        {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]


def test_mask_card_number():
    """Тест функции mask_card_number"""
    assert mask_card_number([{"from": "Visa Classic 2842878893689012",
                              "description": "Перевод организации"}]) == ['Visa Classic 2842 87** **** 9012']


def test_mask_amount_number():
    """Тест функции mask_amount_number"""
    assert mask_amount_number([{"to": "Счет 46765464282437878125"}]) == ['**7812']
