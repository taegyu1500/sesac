#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int* solution(int num_list[], size_t num_list_len, int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    if (num_list == NULL || num_list_len == 0) {
        return malloc(0);
    }

    size_t take = (size_t)n;
    if(take > num_list_len) take = num_list_len;

    int *answer = (int*)malloc(take * sizeof *answer);
    if (answer == NULL) {
        return NULL;
    }

    for (size_t i = 0; i < take; ++i) {
        answer[i] = num_list[i];
    }

    return answer;
}