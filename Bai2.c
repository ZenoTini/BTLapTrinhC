#include <stdio.h>
#include <math.h>

int isPerfectSquare(int number) {
    int squareRoot = sqrt(number);
    return (squareRoot * squareRoot == number);
}

void countAndPrintPerfectSquares(int n) {
    int count = 0;
    printf("\nCac so chinh phuong nho hon %d la:\n", n);
    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            printf("%d ", i);
            count++;
        }
    }
    printf("\nTong so chinh phuong: %d\n", count);
}

int main() {
    int n;
    printf("Nhap so nguyen duong n: ");
    scanf("%d", &n);
    countAndPrintPerfectSquares(n);

    return 0;
}