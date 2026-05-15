from algorithm_buggy import lru_page_replacement


def test_page_fault_count():

    pages = [1, 2, 3, 1, 4, 5]
    capacity = 3

    history, faults = lru_page_replacement(pages, capacity)

    # Số page fault đúng phải là 5
    assert faults == 5


def test_final_frames():

    pages = [1, 2, 3, 1, 4, 5]
    capacity = 3

    history, faults = lru_page_replacement(pages, capacity)

    final_frames = history[-1]["frames"]

    # Frame cuối cùng đúng của LRU
    assert final_frames == [5, 3, 4]


def test_history_length():

    pages = [1, 2, 3, 4]
    capacity = 2

    history, faults = lru_page_replacement(pages, capacity)

    # History phải lưu đủ số bước
    assert len(history) == 4


def test_no_shared_reference():

    pages = [1, 2, 3]
    capacity = 2

    history, faults = lru_page_replacement(pages, capacity)

    # Các frame history phải độc lập nhau
    assert history[0]["frames"] != history[-1]["frames"]


def test_hit_does_not_replace():

    pages = [1, 2, 1]
    capacity = 2

    history, faults = lru_page_replacement(pages, capacity)

    # Khi hit thì không thay page
    assert history[2]["replaced_index"] == -1


def test_empty_input():

    pages = []
    capacity = 3

    history, faults = lru_page_replacement(pages, capacity)

    assert history == []
    assert faults == 0


def test_single_frame():

    pages = [1, 2, 1, 2]
    capacity = 1

    history, faults = lru_page_replacement(pages, capacity)

    # Capacity = 1 thì lần nào đổi page cũng fault
    assert faults == 4