#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmp_strptr(const void *a, const void *b) {
    const char *const *pa = a;
    const char *const *pb = b;
    return strcmp(*pa, *pb);
}

char** solution(const char* my_string) {
    size_t len = strlen(my_string);
    char** answer = malloc(len * sizeof *answer);
    if (answer == NULL) {
        return NULL;
    }

    for (size_t i = 0 ; i < len; ++i) {
        answer[i] = strdup(my_string + i);
        if (answer[i] == NULL) {
            // 실패 시 이미 할당된 메모리 정리
            for (size_t j = 0; j < i; ++j) free(answer[j]);
            free(answer);
            return NULL;
        }
    }

    qsort(answer, len, sizeof *answer, cmp_strptr);
    return answer;
}