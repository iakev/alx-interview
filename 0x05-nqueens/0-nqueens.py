#!/usr/bin/python3
"""
Contains a n implementation of backtracking
to solve the N-queens problem
"""
import sys


def backtrack(chess, partial_candidate, nqueens, set_count, solutions):
    """
    The backtracking algorithm
    """
    if reject(chess, partial_candidate, set_count, nqueens):
        return
    if accept(chess, partial_candidate, nqueens, set_count):
        output(partial_candidate ,solutions)
    child_extension =  first(chess, partial_candidate, nqueens)
    while child_extension is not None:
        backtrack(chess, child_extension, nqueens, set_count, solutions)
        chess, child_extension = next_alt(chess, child_extension, nqueens, solutions)

def root():
    """
    initialises search tree and returns the
    first partial candidate at root of search tree
    """
    chess = [[-1 for _ in range(n)] for _ in range(n)]
    partial_candidate = []
    chess[0][0] =  1
    nqueens["queens"] += 1
    partial_candidate.append([0,0])
    return chess, partial_candidate

def reject(chess, partial_candidate, set_count, nqueens):
    """
    Returns true if the current potential candidate has no
    ability to be a valid solutiun to the CSP
    """
    correct_count = set_count >= n ** 2
    if not check_constraints(chess, partial_candidate, set_count):
        return True
    if check_constraints(chess, partial_candidate, set_count) and (correct_count and nqueens["queens"] != n):
        return True
    return False

def accept(chess, partial_candidate, nqueens, set_count):
    """
    returns True if partial_candidate is a complete and valid
    solutions else returns False
    """
    if nqueens["queens"] == n:
        if check_constraints(chess, partial_candidate, set_count):
            return True
    return False

def output(partial_candidate, solutions):
    """
    Assigns the partial_candidate as one of the soutions
    """
    solutions.append(partial_candidate)

def first(chess, partial_candidate, nqueens):
    """
    Returns the first child of partial_candidate and if
    no possible child value returns a None
    """
    coord = None
    for i in range(n):
        for j in range(n):
            if chess[i][j] == -1:
                chess[i][j] = 1
                nqueens["queens"] += 1
                coord = [i,j]
                break
        break
    if coord:
        partial_candidate.append(coord)
        return partial_candidate
    return coord

def next_alt(chess, partial_candidate, nqueens, solutions):
    """
    Return sibling of partial_candidate or alternative
    to partial_candidate
    """
    try:
        coord = partial_candidate[-1]
        i = coord[0]
        j = coord[1]
    except Exception as e:
        return None
    # reset chess
    if chess:
        new_candidate = []
        chess = [[-1 for _ in range(n)] for _ in range(n)]
        nqueens["queens"] = 0
        if solutions:
            solutions = []
    k = i
    m = j + 1
    if k  < n:
        if m < n:
            chess[k][m] = 1
            nqueens["queens"] += 1
            new_candidate.append([k, m])
        if m == n:
            m = 0
            k = k + 1 if k + 1 < n else None
            if not k:
                return None
            chess[k][m] = 1
            nqueens["queens"] += 1
            new_candidate.append([k, m])
    else:
        return None
    
    return chess, new_candidate




def check_constraints(chess, partial_candidate, set_count):
    """
    checks that the current soln(partial_candidate)
    satisfies the constraints, returns True if passed
    otherwise False
    """
    if len(partial_candidate) != 0:
        coord = partial_candidate[-1]
        i = coord[0]
        j = coord[1]
        # same row constraint
        for k in range(j + 1, n):
            if chess[i][k] == -1:
                chess[i][k] = 0
                set_count += 1
            if chess[i][k] == 1:
                return False
        # same column constraint
        for m in range(i + 1, n):
            if chess[m][j] == 0:
                chess[m][j] = 0
                set_count += 1
            if chess[m][j] == 1:
                return False
        # same diagonal right
        k = i - 1
        m = j - 1
        while k >= 0 and m >= 0:
            if chess[k][m] == -1:
                chess[k][m] = 0
                set_count += 1
            if chess[k][m] == 1:
                return False
            k -= 1
            m -= 1
        k = i + 1
        m = j + 1
        while k < n and m < n:
            if chess[k][m] == -1:
                chess[k][m] = 0
                set_count += 1
            if chess[k][m] == 1:
                return False
            k += 1
            m += 1
        # same diagonal left
        k = i + 1
        m = j - 1
        while k < n and m >= 0:
            if chess[k][m] == -1:
                chess[k][m] = 0
                set_count += 1
            if chess[k][m] == 1:
                return False
            k += 1
            m -= 1
        k = i - 1
        m = j + 1
        while k >= 0 and m < n:
            if chess[k][m] == -1:
                chess[k][m] = 0
                set_count += 1
            if chess[k][m] == 1:
                return False
            k -= 1
            m += 1
        return True
    else:
        return False 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception as e:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens = {"queens": 0}
    set_count = 0
    solutions = []
    chess, partial_candidate = root()
    backtrack(chess, partial_candidate, nqueens, set_count, solutions)
