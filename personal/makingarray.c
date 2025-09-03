#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n, int k) {
    if (k == 0) return NULL; // 보호 코드
    size_t size = (size_t)(n / k);            // 예: 10/3 -> 3
    int* answer = malloc(size * sizeof *answer);
    if (answer == NULL) {
        return NULL;
    }

    for (size_t i = 0; i < size; ++i) {
        answer[i] = (int)(k * (i + 1));      // i=0 -> k*1 = 3, i=1 -> 6, i=2 -> 9
    }

    return answer;
}