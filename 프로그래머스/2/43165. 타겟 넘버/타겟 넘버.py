def solution(numbers, target):
    def dfs(i, current_sum):
        # base case: 모든 숫자를 처리했으면
        if i == len(numbers):
            return 1 if current_sum == target else 0
        # +인 경우 & –인 경우 재귀 호출
        cnt = dfs(i + 1, current_sum + numbers[i])
        cnt += dfs(i + 1, current_sum - numbers[i])
        return cnt

    return dfs(0, 0)
