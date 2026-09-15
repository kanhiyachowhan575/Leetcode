class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        def multiply(A, B):
            return [
                [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
            ]

        def matrix_power(M, p):
            result = [[1, 0], [0, 1]]
            base = M
            while p > 0:
                if p % 2 == 1:
                    result = multiply(result, base)
                base = multiply(base, base)
                p //= 2
            return result

        T = [[1, 1], [1, 0]]
        return matrix_power(T, n)[0][1]