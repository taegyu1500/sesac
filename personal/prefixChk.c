#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* my_string, const char* is_prefix) {
    int answer = 0;
    size_t prefix_len = strlen(is_prefix);
    if (strncmp(my_string, is_prefix, prefix_len) == 0) {
        answer = 1;
    }
    return answer;
}