#include <iostream>
#include <iomanip>
#include "nr.h"

int main(void) {
    int n1=(-1);
    Vec_DP x1(3);
    Vec_DP x2(2);
    FILE* fp;
    fp = fopen("result1.csv", "w+");             // 출력할 엑셀 파일
    NR::sobseq(n1,x1);
    NR::sobseq(n1,x2);
    std::cout << fixed << setprecision(5);      // 소수점 5번째 자리까지 출력
    std::cout << "3-D sobol sequence" << std::endl;
    for (int i = 0; i < 32; ++i) {
        NR::sobseq(3, x1);
        std::cout << setw(1) << i+1 << "\t" << x1[0] << "   " << x1[1];
        std::cout << "   " << x1[2] << std::endl;
        fprintf(fp, "%d, %.5f, %.5f, %.5f \n", i+1, x1[0], x1[1], x1[2]);  // 엑셀 파일 출력
    }
    fclose(fp);
    fp = fopen("result2.csv", "w+");
    std::cout << "2-D sobol sequence" << std::endl;
    for (int i = 0; i < 1024; ++i) {
        NR::sobseq(2, x2);
        std::cout << i+1 << "\t" << x2[0] << "   " << x2[1] << std::endl;
        fprintf(fp, "%d, %.5f, %.5f \n", i+1, x2[0], x2[1]);
    }
    fclose(fp);
    return 0;
}
