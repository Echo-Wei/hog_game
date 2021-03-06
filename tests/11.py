test = {
  'name': 'Question 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> swap_strategy(3, 21, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(30, 54, 7, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(6, 22, 100, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(48, 45, 1, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(36, 43, 10, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(36, 43, 1, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(6, 68, 6, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(51, 9, 1, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(swap_strategy)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> swap_strategy(10, 9, 5, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(10, 0, 3, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(44, 67, 8, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(27, 20, 10, 6)
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
