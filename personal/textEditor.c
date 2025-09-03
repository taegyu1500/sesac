# include <stdio.h>
# include <stdlib.h>
# include <string.h>

#define BUFFER_SIZE 1000

struct TextEditor {
    char *content;
    int cursorPosition;
};

void openTextEditor(struct TextEditor *editor) {
    editor->content = malloc(BUFFER_SIZE * sizeof(char));
    if (!editor->content) exit(1);
    editor->content[0] = '\0';
    editor->cursorPosition = 0;
}

void closeTextEditor(struct TextEditor *editor) {
    free(editor->content);
}

void insertText(struct TextEditor *editor, const char *text) {
    size_t len = strlen(text);
    size_t cur = (size_t)editor->cursorPosition;
    size_t used = strlen(editor->content);
    if (cur > used) cur = used; // 안전
    if (used + len >= BUFFER_SIZE) {
        printf("Not enough space to insert text.\n");
        return;
    }
    // 꼬리 부분을 뒤로 밀어 삽입(겹침 안전)
    memmove(editor->content + cur + len, editor->content + cur, used - cur + 1); // +1 for '\0'
    memcpy(editor->content + cur, text, len);
    editor->cursorPosition = (int)(cur + len);
}

int getCursorPosition(struct TextEditor *editor) {
    return editor->cursorPosition;
}

int getTextLength(struct TextEditor *editor) {
    // ...existing code...
    return (int)strlen(editor->content); // 수정: 실제 텍스트 길이 반환
}

void moveCursor(struct TextEditor *editor, int position) {
    if (position >= 0 && position <= (int)strlen(editor->content)) {
        editor->cursorPosition = position;
        // 만약 이동 시 뒤를 잘라내길 원하면 아래 주석을 해제:
        // editor->content[position] = '\0';
    } else {
        printf("Invalid cursor position.\n");
    }
}

void deleteText(struct TextEditor *editor, int length) {
    if (length > 0 && length <= editor->cursorPosition) {
        editor->cursorPosition -= length;
        editor->content[editor->cursorPosition] = '\0';
    } else {
        printf("Invalid delete length.\n");
    }
}

void saveTextToFile(struct TextEditor *editor, const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file) {
        fwrite(editor->content, sizeof(char), editor->cursorPosition, file);
        fclose(file);
    } else {
        printf("Error opening file for writing.\n");
    }
}

void loadTextFromFile(struct TextEditor *editor, const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file) {
        size_t n = fread(editor->content, sizeof(char), BUFFER_SIZE - 1, file);
        editor->content[n] = '\0';               // 반드시 널 종료
        editor->cursorPosition = (int)strlen(editor->content);
        fclose(file);
    } else {
        printf("Error opening file for reading.\n");
    }
}
void writeTextToFile(struct TextEditor *editor, const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file) {
        fwrite(editor->content, sizeof(char), editor->cursorPosition, file);
        fclose(file);
    } else {
        printf("Error opening file for writing.\n");
    }
}

void showText(struct TextEditor *editor) {
    printf("Text Content:\n%s\n", editor->content);
}

int main() {
    struct TextEditor editor;
    openTextEditor(&editor);
    // 기존 파일이 있으면 불러오기 (덮어쓰기 방지)
    loadTextFromFile(&editor, "output.txt");

    while(1) {
        char command[100];
        printf("Enter command (insert, delete, move, save, load, exit): ");
        scanf("%s", command);

        if (strcmp(command, "insert") == 0) {
            char text[100];
            printf("Enter text to insert: ");
            scanf("%s", text);
            insertText(&editor, text);
        } else if (strcmp(command, "delete") == 0) {
            int length;
            printf("Enter length to delete: ");
            scanf("%d", &length);
            deleteText(&editor, length);
        } else if (strcmp(command, "move") == 0) {
            int position;
            printf("Enter new cursor position: ");
            scanf("%d", &position);
            moveCursor(&editor, position);
        } else if (strcmp(command, "save") == 0) {
            saveTextToFile(&editor, "output.txt");
        } else if (strcmp(command, "load") == 0) {
            loadTextFromFile(&editor, "output.txt");
        } else if (strcmp(command, "show") == 0) {
            showText(&editor);
        } else if (strcmp(command, "exit") == 0) {
            break;
        } else {
            printf("Unknown command.\n");
        }

        printf("Cursor Position: %d\n", getCursorPosition(&editor));
        printf("Text Length: %d\n", getTextLength(&editor));
    }
    return 0;
}