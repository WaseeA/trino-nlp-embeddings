package com.example.trino.plugin;

import io.trino.spi.function.Description;
import io.trino.spi.function.ScalarFunction;
import io.trino.spi.function.SqlType;
import io.trino.spi.type.DoubleType;

public class TestScalar {

    @ScalarFunction("square")
    @Description("Returns the square of a number")
    @SqlType(DoubleType.NAME)
    public static double square(@SqlType(DoubleType.NAME) double value) {
        return value * value;
    }
}
