#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* solution(const char* myString) {
    if (myString == NULL) return NULL;

    size_t len = strlen(myString);
    char *answer = malloc((len + 1) * sizeof *answer);
    if (answer == NULL) return NULL;

    for (size_t i = 0; i < len; ++i) {
        answer[i] = (char) toupper((unsigned char)myString[i]);
    }
    answer[len] = '\0';  // 반드시 널 종료자 추가

    return answer;
}