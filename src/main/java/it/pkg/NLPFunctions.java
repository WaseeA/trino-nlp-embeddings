package it.pkg;

import io.trino.spi.function.Description;
import io.trino.spi.function.ScalarFunction;
import io.trino.spi.function.SqlType;

public class NLPFunctions {

    @ScalarFunction("square")
    @Description("Returns the square of a number")
    @SqlType("double")
    public static double square(@SqlType("double") double value) {
        return value * value;
    }
}
