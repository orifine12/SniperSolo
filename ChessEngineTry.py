"""
trying out new  fresh code of chess engine - will contain: move log, and gamestate info.

"""

class GameState():
    def __init__(self):
        """""
        board is a 8x8 2d list, each list has 2 characthers,
         first is color and second is piece type

        """
        self.board = [
            ["BR","BN","Bb","BQ","BK","Bb","BN","BR"],
            ["BP","BP","BP","BP","BP","BP","BP","BP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["WP","WP","WP","WP","WP","WP","WP","WP"],
            ["WR","WN","Wb","WQ","WK","Wb","WN","WR"],
        ]
        self.whiteToMove = True
        self.moveLog = []