import sys

from view.user import getUserById


userId = sys.argv[1]
getUserById(int(userId))