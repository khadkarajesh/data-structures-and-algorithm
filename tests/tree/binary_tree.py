import pytest

from tree.binary_tree import BinaryTree, create_tree


@pytest.fixture
def binary_tree():
    node = create_tree(sorted([15, 10, 8, 12, 20, 16, 25]))
    binary_tree = BinaryTree(node)
    return binary_tree


def test_create_binary_tree(binary_tree):
    assert binary_tree.in_order() == sorted([15, 10, 8, 12, 20, 16, 25])


def test_pre_order(binary_tree):
    assert binary_tree.pre_order() == [15, 10, 8, 12, 20, 16, 25]


def test_in_order(binary_tree):
    assert binary_tree.in_order() == [8, 10, 12, 15, 16, 20, 25]


def test_post_order(binary_tree):
    assert binary_tree.post_order() == [8, 12, 10, 16, 25, 20, 15]


def test_search(binary_tree):
    assert not binary_tree.search(3)
    assert binary_tree.search(8)
    assert not binary_tree.search(None)
