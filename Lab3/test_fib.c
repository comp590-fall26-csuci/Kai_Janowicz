#include "utest.h"
#include "fibonacci.h"

UTEST_MAIN();

UTEST(fib,fib10) {
	ASSERT_EQ(1,fibonacci(1));
	ASSERT_EQ(1,fibonacci(2));
	ASSERT_EQ(2,fibonacci(3));
	ASSERT_EQ(3,fibonacci(4));
	ASSERT_EQ(5,fibonacci(5));
	ASSERT_EQ(8,fibonacci(6));
	ASSERT_EQ(13,fibonacci(7));
	ASSERT_EQ(21,fibonacci(8));
	ASSERT_EQ(34,fibonacci(9));
	ASSERT_EQ(55,fibonacci(10));
	
};

UTEST(gold,gold10){

	double g = 1.618034;
	EXPECT_NEAR(g,golden_ratio_approx(10), 0.0001f);
};

