/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package it.pkg;

import io.airlift.slice.Slice;
import io.airlift.slice.Slices;
import io.trino.spi.function.Description;
import io.trino.spi.function.ScalarFunction;
import io.trino.spi.function.SqlType;
import io.trino.spi.type.StandardTypes;

public class NLPFunctions
{
    private NLPFunctions()
    {
        throw new UnsupportedOperationException("This is a utility class and cannot be instantiated");
    }

    @ScalarFunction("square")
    @Description("Returns the square of a number")
    @SqlType("double")
    public static double square(@SqlType("double") double value)
    {
        return value * value;
    }

    @ScalarFunction("run_py")
    @Description("Runs the Python Script")
    @SqlType(StandardTypes.VARCHAR)
    public static Slice run_py(@SqlType(StandardTypes.VARCHAR) Slice scriptPath)
    {
        return Slices.utf8Slice("Helo there!");
    }
}
